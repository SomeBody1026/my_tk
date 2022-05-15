import tkinter as tk
from tkinter import ttk

from db import db
"""
        
"""







class InsertFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        # tk.Label(self, text='插入页面').pack()
        self.name = tk.StringVar()
        self.chinese = tk.StringVar()
        self.math = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()
    def create_page(self):
        tk.Label(self).grid(row=0, pady=10)  # 10像素
        tk.Label(self, text='姓名').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2, pady=10)
        tk.Label(self, text='语文').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.chinese).grid(row=2, column=2, pady=10)
        tk.Label(self, text='数学').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.math).grid(row=3, column=2, pady=10)
        tk.Label(self, text='英语').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.english).grid(row=4, column=2, pady=10)
        tk.Button(self, text='录入', command=self.record_info).grid(row=5, column=2, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=6, column=2, pady=10, stick=tk.E)

    def record_info(self):
        stu = {
            'name': self.name.get(),
            'chinese': self.chinese.get(),
            'math': self.math.get(),
            'english': self.english.get(),
        }
        self.name.set('')
        self.chinese.set('')
        self.math.set('')
        self.english.set('')
        db.insert(stu)
        self.status.set('录入成功')

class DeleteFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.username = tk.StringVar()
        self.status = tk.StringVar()
        tk.Label(self, text='根据名字删除数据').pack()
        tk.Entry(self, textvariable=self.username).pack()
        tk.Button(self, text='删除', command=self.delete).pack()
        tk.Label(self, textvariable=self.status).pack()

    def delete(self):
        username = self.username.get()
        flag, message = db.delete_by_username(username)
        self.status.set(message)


class UpdateFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        # tk.Label(self, text='修改页面').pack()
        self.name = tk.StringVar()
        self.chinese = tk.StringVar()
        self.math = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, pady=10)  # 10像素
        tk.Label(self, text='姓名').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2, pady=10)
        tk.Label(self, text='语文').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.chinese).grid(row=2, column=2, pady=10)
        tk.Label(self, text='数学').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.math).grid(row=3, column=2, pady=10)
        tk.Label(self, text='英语').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.english).grid(row=4, column=2, pady=10)
        tk.Button(self, text='查询', command=self.search_user).grid(row=5, column=1, pady=10)
        tk.Button(self, text='修改', command=self.change_user).grid(row=5, column=2, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=6, column=2, pady=10, stick=tk.E)

    def search_user(self):

        flag, info = db.search_by_username(self.name.get())
        if flag:
            self.name.set(info['name'])
            self.chinese.set(info['chinese'])
            self.math.set(info['math'])
            self.english.set(info['english'])
        else:
            self.status.set(info)

    def change_user(self):
    # def record_info(self):
        stu = {
            'name': self.name.get(),
            'chinese': self.chinese.get(),
            'math': self.math.get(),
            'english': self.english.get(),
        }
        self.name.set('')
        self.chinese.set('')
        self.math.set('')
        self.english.set('')
        db.update(stu)
        self.status.set('修改成功')

class SearchFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        # tk.Label(self, text='查询').pack()
        self.table_view = tk.Frame()
        self.table_view.pack()
        self.create_page()

    def create_page(self):
        columns = ('name', 'chinese', 'math', 'english')
        columns_values = ('姓名', '语文', '数学', '英语')
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('name', width=80, anchor='center')  # anchor 对齐方式
        self.tree_view.column('chinese', width=80, anchor='center')  # anchor 对齐方式
        self.tree_view.column('math', width=80, anchor='center')  # anchor 对齐方式
        self.tree_view.column('english', width=80, anchor='center')  # anchor 对齐方式
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('chinese', text='语文')
        self.tree_view.heading('math', text='数学')
        self.tree_view.heading('english', text='英语')
        self.tree_view.pack(fill=tk.BOTH, expand=True)  # 调用了pack以后就布局了  BOTH表示上下
        self.show_data_frame()

        tk.Button(self, text='刷新', command=self.show_data_frame).pack(anchor=tk.E, pady=5)

    def show_data_frame(self):
        # 删除旧的节点
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        students = db.all()
        print(students)
        for index, stu in enumerate(students):
            self.tree_view.insert('', index + 1, values=(
                stu['name'], stu['chinese'], stu['math'], stu['english']
            ))


class AboutFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        tk.Label(self, text='关于作品：本作品由tkinter制作').pack()
        tk.Label(self, text='关于作者：薛瑄').pack()
        tk.Label(self, text='版权所有：123456').pack()