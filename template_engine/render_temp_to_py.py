#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

# 渲染函数

def render_function(context, do_dots):
    c_user_name = context['user_name']
    c_product_list = context['product_list']
    c_format_price = context['format_price']

    result = []
    append_result = result.append  # 将方法赋值给另外的变量
    extend_result = result.extend
    to_str = str

    extend_result([
        '<p>Welcome,', to_str(c_user_name),
        '!</p>\n<p>Products:</p>\n<ul>\n'
    ])
    for c_product in c_product_list:
        extend_result([
            '\n  <li>',
            to_str(do_dots(c_product, 'name')),
            ':\n         ',
            to_str(c_format_price(do_dots(c_product, 'price'))),
            '<li>\n'
        ])

    append_result('\n<ul>\n')
    return ''.join(result)


# 模板引擎的核心
class Templite:
    pass


# 模板引擎对象
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
        pass
