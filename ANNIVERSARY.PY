#如何要求输入一个日期
#str=7.15
#要求输入：
str=float(input("输入一个日期："))
#input函数得到一个字符串，我们把他转换成浮点型  应为后面用作比较的7.15， 6.6是浮点型，
if str == 7.15:           
    print('LOVE DAY')        
elif str == 6.6:
    print('GAO KAO')
elif str == 6.18:
    print ('first night')
elif str == 8.30:           
    print('22BRITHDAY')
else:
    print ('You are die！')     