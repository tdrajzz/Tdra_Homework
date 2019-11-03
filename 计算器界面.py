import tkinter as tk 

form1=tk.Tk()
form1.title("计算器")
form1.geometry("300x400+200+100")
#第一部分
entry1=tk.Entry(form1,fg="black",bg="white")
entry1.grid(row=0,column=0,sticky=tk.EW,ipady=5) 
#第二部分
#创建frame控件
f1=tk.Frame(form1)
f1.grid(row=1,column=0)
#开始创建按钮
#按钮文本的列表
fh=[7,8,9,"x" ,4,5,6,"-",1,2,3,"+",0,".","清空","退格"]
#行
ri=0
#列
ci=0
#通过循环遍历出所有的按钮
for v in fh:
    if(ci!=0 and ci % 4 == 0):
        ri+=1 #换行
        ci=0 #列重新赋值
    btn1=tk.Button(f1,font=("微软雅黑",20),text=v,width=4)
    btn1.grid(row=ri,column=ci)
    ci+=1
btnEqual=tk.Button(f1,font=("微软雅黑",20),text="=",width=6)
btnEqual.grid(row=ri+1,column=0,columnspan=4,sticky=tk.EW)
form1.mainloop()
