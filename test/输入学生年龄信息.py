infos = []
a = 0
while True:
    name = input('请输入学生姓名(如需退出，请输入EXIT!)：')
    if name =='EXIT':
        break
    else:
        age = input('请输入学生年龄：')
        name_age = '{:<20}：{:0>2};'.format(name,age)
        infos.append(name_age)
for info in infos:
    if a < len(infos):
        print(infos[a])
        name_age = '{:<20}：{:0>2};'.format(name, age)
        a+=1

# for info in infos:
#     if info == 'exit' or info == 'EXIT':
#         break
#     print(infos)
