#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

# 该方法来渲染字符串模板问题在于
# 模板字符串参与python代码逻辑
# 往后的扩展必然会遇到很多麻烦


# 页面主体html字符串
PAGE_HTML = """
      <p>Welcome,{name}!</p>
      <p>Products:</p>
      <ul>{products}</ul>
    """

# 产品字符串
PRODUCT_HTML = "<li>{productname}:{price}</li>\n"


def make_page(username,products):
    product_html = ""
    for product_name,price in products:
        product_html+=PRODUCT_HTML.format(
            productname = product_name,price = price
        )
    html = PAGE_HTML.format(name=username,products=product_html)
    return html

