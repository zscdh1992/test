def getName(srcStr):
     return srcStr.replace(',','').split(' ')


name = getName('A old lady come in, the name is Mary, level 94454')
print(name[-3])