import cgi
# 解析表单数据
form=cgi.FieldStorage()
# 生成响应头部
print('Content-type:text/html\n')
# 生成响应网页主体
print("<title>reply page</title>")
if not 'user' in form:
    print("<h1>你是谁？</h1>")
else:
    print('<h1>hello<i>%s</i></h1>' % cgi.escape(form['user'].value))