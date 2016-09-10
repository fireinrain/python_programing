from tkinter import *

class WidgetsDemo:
    def __init__(self):
        window=Tk()#创建窗口
        window.title('窗口程序')   #设置标题

        # 创建框架
        frame1=Frame(window)
        # 把框架放在Window中
        frame1.pack()

        self.v1=IntVar()
        # 创建一个复选框如果选中则self.v1为1否则为0，当点击cbtbold时触发函数
        cbtBold=Checkbutton(frame1,text='Bold',variable=self.v1,command=self.processCheckbutton)

        self.v2=IntVar()
        # 创建两个单选按钮放置在frame1中按钮文本分别是red和yellow，背景色分别是红色和黄色
        # 当rbred按钮选中时self。v2为1当rbyellow被选中时self。v2为2按钮点击触发事件
        rbRed=Radiobutton(frame1,text='Red',bg='red',variable=self.v2,value=1,command=self.processRadiobutton)
        rbYellow=Radiobutton(frame1,text='Yellow',bg='yellow',variable=self.v2,value=2,command=self.processRadiobutton)

        # grid布局
        cbtBold.grid(row=1,column=1)
        rbRed.grid(row=1,column=2)
        rbYellow.grid(row=1,column=3)

        # 创建框架2
        frame2=Frame(window)
        # 将框架2放入window中
        frame2.pack()

        # 创建标签
        label=Label(frame2,text='enter your name:')
        # 创建的entry，内容是和self.name关联
        self.name=StringVar()
        entryName=Entry(frame2,textvariable=self.name)
        # 创建按钮点击触发事件
        btGetName=Button(frame2,text='get name',command=self.processButton)

        # 创建消息
        message=Message(frame2,text='this is a widgets demo')

        # grid布局
        label.grid(row=1, column=1)
        entryName.grid(row=1, column=2)
        btGetName.grid(row=1, column=3)
        message.grid(row=1, column=4)

        # 创建格式化文本
        text=Text(window)
        text.pack()
        text.insert(END,'tip\n the best way to learn tkinter is to read')
        text.insert(END,'these carefully designed examples and use them')
        text.insert(END,'to create your applications')

        # 监听事件直到window被关闭
        window.mainloop()
    #     复选框点击事件
    def processCheckbutton(self):
        print('check button is :'+('checked' if self.v1.get()==1 else 'unpacked'))

    #单选按钮点击事件

    def processRadiobutton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow")
               + " is selected.")
        # getname 按钮点击函数
    def processButton(self):
        print("Your name is " + self.name.get())

if __name__=='__main__':
    demo=WidgetsDemo
    demo()