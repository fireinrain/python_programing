import shelve
from person import Person
from manager import Manager

# 实例化
bob = Person('bob smith', 42, 30000, 'software')
sue = Person('sue jones', 42, 40000, 'hardware')
tom = Manager('tom doe',50,50000)

# 数据持久化
db=shelve.open('class.shelve')
db['bob']=bob
db['sue']=sue
db['tom']=tom
db.close()
