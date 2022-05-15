import tkinter as tk
from tkinter import messagebox
from db import db
from MainPage import MainPage

class loginPage:

    def __init__(self, master):

        # root = tk.Tk()  # root可以理解为一个本子
        self.root = master
        self.root.geometry('300x180')
        self.root.title('登录页')

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.page = tk.Frame(self.root)  # page可以理解为一页纸， 然后把操作放到page上
        self.page.pack()
        tk.Label(self.page).grid(row=0, column=0)  # 标签
        tk.Label(self.page, text='账户：').grid(row=1, column=1)  # 标签
        tk.Entry(self.page, textvariable=self.username).grid(row=1, column=2)  # 输入框

        tk.Label(self.page, text='密码：').grid(row=2, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.password).grid(row=2, column=2)



        tk.Button(self.page, text='登录', command=self.login).grid(row=3, column=1, pady=10)
        tk.Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=2)



    def login(self):
        name = self.username.get()
        pwd = self.password.get()
        print(name, pwd)
        flag, message = db.check_login(name, pwd)
        if flag:
            print('登录成功')
            # 撕毁第一页纸，翻到第二页纸
            self.page.destroy()  # 把页面的数据销毁，但是页面还在
            MainPage(self.root)
        else:
            messagebox.showwarning(title='warning', message=message)

        # if name == 'admin' and pwd == '123456':
        #     print('ok')
        # else:
        #     messagebox.showwarning(title='警告', message='登陆失败')
if __name__ == '__main__':
    root = tk.Tk()
    login = loginPage(master=root)
    root.mainloop()
