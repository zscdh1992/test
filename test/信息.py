a = 0
students = input('输入学生年龄信息:')
# print(students)
infos = students.split(';')
# print(infos)
for info in infos:
    if a < len(infos)-1:
        person = infos[a].split(',')
        name = person[0].strip()
        age = person[1].strip()
        print('{:<20}：{:0>2};'.format(name,age))
        a+=1
# name_age = '{:<20}：{:0>2};'.format(name,age)
# infos.append(name_age)
# for info in infos:
#     if a < len(infos):
#         print(infos[a])
#         a+=1