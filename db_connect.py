import MySQLdb
from apiLib import  *
import datetime,sys

cm = CourseMgr()

retObj,sessionid = cm.login('auto','sdfsdfsdf')

curTime = '{0:%Y-%m-%d_%H:%M:%S}'.format(datetime.datetime.now())

courseName = f'python_{curTime}'


# 先添加一个课程
addRetObj = cm.add_course(courseName,
                     'Python语言',
                     1)

assert addRetObj['retcode'] == 0

courseId = addRetObj['id']

# 再添加老师
tm = TeacherMgr(sessionid)

teachername =   f'zyz_{curTime}'
addTeacherRet = tm.add_teacher(
    teachername,
    'xinz',
    '新增老师',
    '新增老师描述',
    [{"id":courseId,"name":courseName}],
    1

)


if addTeacherRet['retcode'] == 0:
    print('===> 添加老师返回结果retcode为0，通过')
else:
    print('===> 添加老师返回结果retcode不为0，不通过！！！')
    sys.exit(2)


# 检查是否添加成功
listRetObj = tm.list_teacher(1,20)

expected = {
            "username": teachername,
            "realname": "新增老师",
            "display_idx": 1,
            "courses": [
                {
                    "course_id": courseId
                }
            ],
            "id": addTeacherRet['id'],
            "desc": "新增老师描述"
        }


if listRetObj['retlist'].count(expected) == 1:
    print('===> 返回结果包含添加老师1次，通过')
else:
    print('===> 返回结果包含添加老师不是1次，不通过！！！')
    sys.exit(2)



print('\n ======== 用例011,执行通过 ======== \n')



db = MySQLdb.Connect(host ='192.168.100.9',user='songqin',
                     passwd='songqin',db='plesson',charset='utf8',port=3306)

cousor =db.cursor()

sqlStr1='''
select  * from  sq_teacher
'''
cousor.execute(sqlStr1)
data = cousor.fetchall()

for values in data:
    print(values)


cousor.close()
db.close()