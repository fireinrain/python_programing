import sys
# 简单的文件过滤
# 和简单的文本处理
def filter_files(name,function):
    input=open(name,'r')
    output=open(name+'.out','w')
    for line in input:
        output.write(function(line))
    input.close()
    output.close()

def filter_stream(function):
    while True:
        line=sys.stdin.readline()
        if not line:break
        print(function(line),end="")

if __name__=="__main__":
    filter_stream(lambda line:line)