#定义一个用于存放学员信息的列表变量
stulist=[
    {'name':'zhangxiaogang','age':20,'classid':'pyton01'},
    {'name':'wanppeng','age':26,'classid':'pyton02'},
    {'name':'lixia','age':19,'classid':'pyton08'}]

#定义一个学生信息的输出函数
def showstu(stulist):
    ...
    '学员信息的输出函数'
    ...

    if len(stulist)==0:
        print('=========== 没有学员信息可以输出！===========')
        return
    print('|{0:<10}| {1:<20}| {2:<20}| {3:<20}|'.format('sid','name','age','classid'))
    print('-' *40)
    for i in range(len(stulist)):
        print('|{0:<10}| {1:<20}| {2:<20}| {3:<20}|'.format(i+1,stulist[i]['name'],stulist[i]['age'],stulist[i]['classid']))

while True:
    # 输出初始界面
    print('=' *12,'学员管理系统','=' *14)
    print('{0:1} {1:13} {2:15}'.format(' ', '1. 查看学员信息','2.添加学员信息'))
    print('{0:1} {1:13} {2:15}'.format(' ', '3. 删除学员信息','4.退出系统'))
    print('='*40)
    key = input('请输入对应读选择：')
    # 根据键盘值，判断并执行对应的操作
    if key == '1':
        print('=' *12,'学员信息浏览','='*14)
        showstu(stulist)
        input('按回车继续：')

    elif key == '2':
        print('=' *12,'学员信息添加','='*14)
        stu={}
        stu['name']=input('请输入要添加的姓名：')
        stu['age'] = input('请输入要添加的年龄：')
        stu['classid'] = input('请输入要添加的班级号：')
        stulist.append(stu)
        showstu(stulist)
        input('按回车继续：')

    elif key == '3':
        print('=' *12,'学员信息删除','='*14)
        showstu(stulist)
        sid = input('请删除你要删除的信息ID号：')
        del stulist[int(sid)-1]
        input('按回车继续：')
    elif key == '4':
        print('=' *12,'再见','='*14)
        break
    else:
        print('=========无效的键盘输入！==========')