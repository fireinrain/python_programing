# 持久储存记录
# 初始化将储存文件，pickle和shelve的数据

# 记录
bob={'name':'bob smith','age':42,'pay':30000,'job':'dev'}
sue={'name':'sue jones','age':45,'pay':40000,'job':'hdw'}
tom={'name':'Tom','age':50,'pay':0,'job':None}

# 数据库
db={}
db['bob']=bob
db['sue']=sue
db['tom']=tom

# 作为脚本运行
if __name__=='__main__':
    for key in db:
        print(key,'=>',db[key])
