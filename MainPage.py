import tkinter as tk
from views import AboutFrame, UpdateFrame, InsertFrame, SearchFrame, DeleteFrame

class MainPage:
    def __init__(self, master: tk.Tk):  # 静态的类型注解
        self.root = master
        self.root.title('用户信息管理系统 V0.0.1')
        self.root.geometry('600x400')
        self.create_page()

    def create_page(self):
        self.about_frame = AboutFrame(self.root)
        # self.about_frame = tk.Frame(self.root)  # 布局到当前的页面上
        # tk.Label(self.about_frame, text='关于作品：本作品由tkinter制作').pack()
        # tk.Label(self.about_frame, text='关于作者：薛瑄').pack()
        # tk.Label(self.about_frame, text='版权所有：123456').pack()

        self.update_frame = UpdateFrame(self.root)
        # self.update_frame = tk.Frame(self.root)
        # tk.Label(self.update_frame, text='修改页面').pack()
        self.insert_frame = InsertFrame(self.root)
        self.search_frame = SearchFrame(self.root)
        self.delete_frame = DeleteFrame(self.root)

        menubar = tk.Menu(self.root)
        menubar.add_command(label='录入', command=self.show_insert)
        menubar.add_command(label='删除', command=self.show_delete)
        menubar.add_command(label='修改', command=self.show_update)
        menubar.add_command(label='查询', command=self.show_search)
        menubar.add_command(label='关于', command=self.show_about)
        self.root['menu'] = menubar

    def show_about(self):
        self.insert_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.update_frame.pack_forget()
        self.search_frame.pack_forget()
        self.about_frame.pack()


    def show_update(self):
        self.insert_frame.pack_forget()
        self.delete_frame.pack_forget()

        self.search_frame.pack_forget()
        self.about_frame.pack_forget()
        self.update_frame.pack()

    def show_insert(self):

        self.delete_frame.pack_forget()
        self.update_frame.pack_forget()
        self.search_frame.pack_forget()
        self.about_frame.pack_forget()
        self.insert_frame.pack()

    def show_search(self):
        self.insert_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.update_frame.pack_forget()
        self.search_frame.pack()
        self.about_frame.pack_forget()

    def show_delete(self):
        self.insert_frame.pack_forget()
        self.delete_frame.pack()
        self.update_frame.pack_forget()
        self.search_frame.pack_forget()
        self.about_frame.pack_forget()



if __name__ == '__main__':
    root = tk.Tk()
    MainPage(master=root)
    root.mainloop()
