from tkinter import *
from tkinter.messagebox import showerror
import shelve

shelvename='class-shelve'
fieldnames=('name','age','job','pay')

def makeWidgets():
    global entries
    window = Tk()
    window.title('people shelve')
    form=Frame(window)
    form.pack()
    entries={}
    for (ix,label) in enumerate(('key',)+fieldnames):
        lab=Label(form,text=label)
        ent=Entry(form)
        lab.grid(row=ix,column=0)
        ent.grid(row=ix,column=1)
        entries[label]=ent
    Button(window,text="查询",command=fetchRecord).pack(side=LEFT)
    Button(window, text="添加", command=updateRecord).pack(side=LEFT)
    Button(window, text="退出", command=window.quit).pack(side=RIGHT)
    return window

def fetchRecord():
    key=entries['key'].get()
    try:
        # 获取数据并在gui中显示
        record=db[key]
    except:
        showerror(title='error',message='没有此人的信息')
    else:
        for field in fieldnames:
            entries[field].delete(0,END)
            entries[field].insert(0,repr(getattr(record,field)))

def updateRecord():
    key=entries['key'].get()
    if key in db:
        record=db[key]
    else:
        from person import Person
        record=Person(name='?',age='?')
    for field in fieldnames:
        setattr(record,field,eval(entries[field].get()))
    db[key]=record

# if __name__=='__main__':

db=shelve.open(shelvename)
window=makeWidgets()
print(db)
window.mainloop()
db.close()