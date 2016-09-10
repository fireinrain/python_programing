import os
print('set env...',end="")
# 输出当前的shell变量值
print(os.environ['USERNAME'])

# 在后台运行os.putenv
os.environ['USERNAME']='刘钊样'
os.system('python echoenv.py')

# 传递新的值
os.environ['USERNAME']='mayuyu'
os.system('python echoenv.py')

os.environ['USERNAME']=input('?')
print(os.popen('python echoenv.py').read())