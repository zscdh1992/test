# a=2 b=2
# a='欢迎哈哈哈'
# print('XX'+a,'!')
# a='欢迎哈哈哈'
# b=4
# a=4
# a+=1
# print(a[1:4], a[-4:-1])
# print(a[1:4]not in a[-4:-1])
# str1 = "name is tom"
# print(str1)
# print(type(len(str1)))
# print(str1.index('n'))
# print(str1[0:])
# print(str1[0:-4])
# print(str1[:-1])
# print(str1[str1.index("i")])
# print(type(str1.index("i")+2))
# int1 = str1[str1.index("i")+2]
# print(str1[str1.index("i"):str1.index("i")+2])
# print(str1[str1.index("i")]:str1[str1.index("i")+2])
# alist = [1,1,2,3,5,[10,20]]
# blist = [233]
# print(alist[-1])
# alist[-1].append(6)
# print(alist[-1])
# alist[-1].insert(1,10)
# print(alist[-1])
# alist.extend(blist)
# alist.remove(1)
# print(alist)
# print(alist.pop(1))
# print(alist)

# tu1 = ([1,2],[2,3])
#
# print(type(tu1[0]))

# def fun1():
#     return 101
# def fun():
#         print(fun1())
# fun()
# x = 100
# if x<1:
#  print(100)
#         and 1==1\
#         and 1==1:
#     print(2)
# elif x>2:
#     a = int(input("请输入："))
#     print(a+1)
# else:
#     print(4)
# 判断号码
# def check_tel():

CN_mobile = [134,135,136,137,138,139,147,148,150,151,152,157,158,159,165,172,178,182,183,184,187,188,198]
CN_union = [130,131,132,145,146,155,156,166,175,176,185,186]
CN_dianxin = [133,149,153,173,175,177,180,189,191,199]
virtual = [167,170,171]
virtual_CN_mobile = [1703,1705,1706]
virtual_CN_union = [1704, 1707, 1708,1709,1710]
virtual_CN_dianxin = [1700, 1701, 1702]
tel = input('请输入想要查询运行商的手机号码：')
if len(tel) == 11:
    if tel.isdigit():
        first_three = int(tel[0:3])
        first_four = int(tel[0:4])
        if first_three in CN_mobile:
            print('此号码:'+tel+'的运营商是中国移动！')
        elif first_three in CN_union:
                print('此号码:'+ tel+'的运营商是中国联通！')
        elif first_three  in CN_dianxin:
                print('此号码:'+ tel+'的运营商是中国电信！')
        elif first_three in virtual:
            if first_four in virtual_CN_mobile:
                print('此号码:' + tel + '的虚拟运营商是中国移动！')
            elif first_four in virtual_CN_dianxin:
                print('此号码:' + tel + '的虚拟运营商是中国电信！')
            elif first_three in virtual or first_four in virtual_CN_union:
                print('此号码:' + tel + '的虚拟运营商是中国联通！')
        else:
            print('此号码:'+ tel+'暂无归属运行商！')
    else:
        print('存在非法字符,请输入纯数字！')

else:
    print('请输入正确的11位手机号码！')

# # check_tel()
#


# def func(a,b):
#  return a,b,a+b
#
# SumData = func(1,2)
# print(SumData)
