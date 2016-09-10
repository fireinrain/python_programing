"""
用自定义格式将内存数据库的对象保存在文件在文件中；
假定数据不试用’endrec,‘enddb’和‘=》；
假定数据库是字典的字典，警告使用eval()可能会存在危险，因为他会将字符串当成代码来执行
也可以使用eval（）一次创建一条字典记录
对于print(key,file=dbfile)也可以使用dbfile.write(key+'\n')
"""
dbfilename='people-file'
ENDDB='enddb'
ENDREC='endrec'
RECSEP='=>'

def storeDbase(db,dbfilename=dbfilename):
    "将数据库格式化保存为普通文件"
    dbfile=open(dbfilename,'w')
    for key in db:
        print(key,file=dbfile)
        for(name,value) in db[key].items():
            print(name+RECSEP+repr(value),file=dbfile)
        # str()一般是将数值转成字符串。 repr()是将一个对象转成字符串显示，
        # 注意只是显示用，有些对象转成字符串没有直接的意思。
        # 如list,dict使用str()是无效的，但使用repr可以，这是为了看它们都有哪些值，为了显示之用。

        print(ENDREC,file=dbfile)
    print(ENDDB,file=dbfile)
    dbfile.close()
def loadDbase(dbfilename=dbfilename):
    "解析数据，重新构建数据库"
    dbfile=open(dbfilename)
    import sys
    sys.stdin=dbfile
    db={}
    key=input()
    while key != ENDDB:
        rec={}
        field=input()
        while field != ENDREC:
            name,value=field.split(RECSEP)
            rec[name]=eval(value)
            field=input()
        db[key]=rec
        key=input()
    return db
if __name__=='__main__':
    from initdata import db
    storeDbase(db)
