import os,sys
from http.server import HTTPServer,CGIHTTPRequestHandler

# 存放html和cgi脚本文件的目录所在
webdir='.'
# 端口号
port=80
# 在html根目录下运行
os.chdir(webdir)
serveraddr=("",port)
serverobj=HTTPServer(serveraddr,CGIHTTPRequestHandler)
# 永久守护进程
serverobj.serve_forever()
