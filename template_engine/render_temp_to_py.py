#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
import re
# 渲染函数
class TempliteSyntaxError(ValueError):
    """Raised when a template has a syntax error."""
    pass

# def render_function(context, do_dots):
#     c_user_name = context['user_name']
#     c_product_list = context['product_list']
#     c_format_price = context['format_price']
#
#     result = []
#     append_result = result.append  # 将方法赋值给另外的变量
#     extend_result = result.extend
#     to_str = str
#
#     extend_result([
#         '<p>Welcome,', to_str(c_user_name),
#         '!</p>\n<p>Products:</p>\n<ul>\n'
#     ])
#     for c_product in c_product_list:
#         extend_result([
#             '\n  <li>',
#             to_str(do_dots(c_product, 'name')),
#             ':\n         ',
#             to_str(c_format_price(do_dots(c_product, 'price'))),
#             '<li>\n'
#         ])
#
#     append_result('\n<ul>\n')
#     return ''.join(result)



class CodeBuilder:
    """负责生成规范的python代码"""

    def __init__(self, indet=0):
        self.code = []
        self.indent_level = indet  # indet python 代码的缩进级别

    def add_line(self, line):
        """为当前的Python代码添加新的行"""
        self.code.extend(" " * self.indent_level, line, "\n")

    # 定义标准的python缩进
    INDENT_STEP = 4

    def indet(self):
        """增加当前行的缩进"""
        self.indent_level += self.INDENT_STEP

    def dedent(self):
        """减少当前行的缩进"""
        self.indent_level -= self.INDENT_STEP

    def add_section(self):
        """一个中转的对象，用于保留一个参考位置"""
        section = CodeBuilder(self.indent_level)
        self.code.append(section)
        return section

    def __str__(self):
        """将code列表的内容拼接返回"""
        return "".join(str(c) for c in self.code)

    def get_globals(self):
        """
        执行字符串python代码，返回一个包含全局内容的字典
        :return:
        """
        assert self.indent_level == 0
        #获取python代码的字符串
        python_source = str(self)
        #执行，并返回包含定义的东西的字典
        global_namespace = {}
        exec(python_source,global_namespace)
        return global_namespace


# 模板引擎的核心类
class Templite:
    """
    模板引擎核心：编译和渲染
    """
    def __init__(self,text,*contexts):
        """
        对于给定的文本，构造一个模板对象

        :param text:
        :param contexts: 一个字典，保存的值用来将来的渲染
        t = Templite(template_text)
        t = Templite(template_text, context1)
        t = Templite(template_text, context1, context2)
        """
        self.context = {}
        for context in contexts:
            self.context.update(context)

        self.all_vars = set()
        self.loop_vars = set()

        code = CodeBuilder()
        code.add_line("def render_function(context,do_dots):")
        code.indet()
        vars_code = code.add_section()
        code.add_line("result = []")
        code.add_line("append_result = result.append")
        code.add_line("extend_result = result.extend")
        code.add_line("to_str = str")

        #缓冲输出字符串
        buffered = []
        def flush_output():
            if len(buffered) == 1:
                code.add_line("append_result(%s)" % buffered[0])
            elif len(buffered) > 1:
                code.add_line("extend_result([%s])" % ", ".join(buffered))


        #检查合理的嵌套
        ops_stack = []
        tokens = re.split(r"(?s)({{.*?}}|{%.*?%}|{#.*?#})",text)
        for token in tokens:
            if token.startswith('{#'):
                continue
            elif token.startswith("{{"):
                expr = self._expr_code(token[2:-2].strip())
                buffered.append("to_str(%s)" % expr)

            elif token.startswith("{%"):
                flush_output()
                words = token[2:-2].strip().split()

                if words[0] == "if":
                    if len(words) != 2:
                        self._syntax_error("don't unserstand if",token)
                    ops_stack.append('if')
                    code.add_line("if %s" % self._expr_code(words[1]))
                    code.indent()
                elif words[0] == "for":
                    if len(words) != 4 or words[2] != "in":
                        self._syntax_error("don't understand for",token)
                    ops_stack.append('for')
                    self._variable(words[1],self.loop_vars)
                    code.add_line(
                        "for c_%s in %s:" %(
                            words[1],
                            self._expr_code(words[3])
                        )
                    )
                    code.indet()

                elif words[0].startswith("end"):
                    if len(words) != 1:
                        self._syntax_error("don't understand end",token)
                    end_what = words[0][3:]
                    if not  ops_stack:
                        self._syntax_error("too many ends",token)
                    start_what = ops_stack.pop()
                    if start_what != end_what:
                        self._syntax_error("mismatched end tag",token)
                    code.dedent()
                else:
                    self._syntax_error("don't understand tag",words[0])
            else:
                if token:
                    buffered.append(repr(token))

        if ops_stack:
            self._syntax_error("unmatched action tag",ops_stack[-1])

        flush_output()

        for var_name in self.all_vars - self.loop_vars:
            vars_code.add_line("c_%s = context[%r]" % (var_name,var_name))

        code.add_line("result ''.join(result)")
        code.indet()
        self._render_function = code.get_globals()['render_function']

    def _expr_code(self,expr):
        """对表达式生成对应的Python表达"""
        if "|" in expr:
            pipes = expr.split("|")
            code = self._expr_code(pipes[0])
            for func in pipes[1:]:
                self._variable(func,self.all_vars)
                code = "c_%s(%s)" % (func,code)
        elif "." in expr:
            dots = expr.split(".")
            code = self._expr_code(dots[0])
            args = ", ".join(repr(d) for d in dots[1:])
            code = "do_dots(%s,%s)" % (code,args)
        else:
            self._variable(expr,self.all_vars)
            code = "c_%s" % expr
        return code

    def _syntax_error(self,msg,thing):
        raise TempliteSyntaxError("%s:%r" % (msg,thing))

    def _variable(self,name,vars_set):
        if not re.match(r"[_a-zA-Z][_a-zA-Z0-9]*$",name):
            self._syntax_error("not a valid name",name)
        vars_set.add(name)

    def render(self,context = None):
        render_context = dict(self.context)
        if context:
            render_context.update(context)
        return self._render_function(render_context,self._do_dots)

    def _do_dots(self,value,*dots):
        for dot in dots:
            try:
                value = getattr(value,dot)
            except AttributeError:
                value = value[dot]
            if callable(value):
                value = value()
        return value


# # 模板引擎对象
# templite = Templite("""
#     <h1>Hello {{name|upper}}!</h1>
#     {% for topic in topics %}
#         <p>You are interested in {{topic}}.</p>
#     {% endfor %}
#     '''
#
# """, {'upper': str.upper}, )
#
# # 用上面的对象来渲染一些数据
# text = templite.render({
#     'name': "liuzhaoyang",
#     'topics': ['Python', 'meizi', 'programmer'],
# })


# 模板引擎主要是将模板解析成python代码
# 在这里先建立一个codebuilder类
# 负责生成格式规范的Python代码
class CodeBuilder:
    """负责生成规范的python代码"""

    def __init__(self, indet=0):
        self.code = []
        self.indent_level = indet  # indet python 代码的缩进级别

    def add_line(self, line):
        """为当前的Python代码添加新的行"""
        self.code.extend([" " * self.indent_level, line, "\n"])

    # 定义标准的python缩进
    INDENT_STEP = 4

    def indet(self):
        """增加当前行的缩进"""
        self.indent_level += self.INDENT_STEP

    def dedent(self):
        """减少当前行的缩进"""
        self.indent_level -= self.INDENT_STEP

    def add_section(self):
        """一个中转的对象，用于保留一个参考位置"""
        section = CodeBuilder(self.indent_level)
        self.code.append(section)
        return section

    def __str__(self):
        """将code列表的内容拼接返回"""
        return "".join(str(c) for c in self.code)

    def get_globals(self):
        """
        执行字符串python代码，返回一个包含全局内容的字典
        :return:
        """
        assert self.indent_level == 0
        # 获取python代码的字符串
        python_source = str(self)
        #执行，并返回包含定义的东西的字典
        global_namespace = {}
        exec(python_source,global_namespace)
        return global_namespace


if __name__ == "__main__":
    templite = Templite("""
        <h1>Hello {{name|upper}}!</h1>
        {% for topic in topics %}
            <p>You are interested in {{topic}}.</p>
        {% endfor %}
        '''

    """, {'upper': str.upper}, )

    # 用上面的对象来渲染一些数据
    text = templite.render({
        'name': "liuzhaoyang",
        'topics': ['Python', 'meizi', 'programmer'],
    })
    print(text)