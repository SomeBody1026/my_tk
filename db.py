import json
class MysqlDatabases:
    def __init__(self):
        with open('users.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.users = json.loads(text)
        self.students = json.loads(open('students.json', mode='r', encoding='utf-8').read())

    def check_login(self, username, password):
        for user in self.users:
            if username == user['username']:
                if password == user['password']:
                    return True, '登录成功'
                else:
                    return False, '密码不正确'
        return False, '用户不存在'

    def all(self):  # 查询使用
        return self.students

    def insert(self, student):
        self.students.append(student)
    def delete_by_username(self, name):
        for student in self.students:
            pass
            if student['name'] == name:
                self.students.remove(student)
                return True, f'{name} 删除成功'
        return False, f'姓名{name}不存在'

    def search_by_username(self, name):
        for student in self.students:
            if student['name'] == name:
                return True, student
        return False, f'姓名{name}不存在'

    def update(self, stu):
        for student in self.students:
            if student['name'] == stu['name']:
                student.update(stu)
                return True, f'{stu["name"]} 修改成功'
        return False, f'{stu["name"]} 不存在'


db = MysqlDatabases()


if __name__ == '__main__':
    res = db.check_login('admin', '123456')
    print(res)
    print(db.all())

