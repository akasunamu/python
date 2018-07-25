#前面看到了一个问题，当box=list , tuple ,dictionay 的时候都可以成功运行，此程序通过实验验证crop的实现方法。
#例子：     
# box={100:0,100:1,500:2,500:3}
# box={0:100,1:100,2:500,3:500}
# box=[100,100,500,500]
# box=(100,100,500,500)

# 函数原型： im=crop(box)
# 猜想1： 通过 index来获取每个值（0，1，2，3）
# 实验1：
expNum=int(input("enter the num :"))

if expNum==1:
    print("实验1，通过下表获得每个值")
    box={100:0,100:1,500:2,500:3}
    x1,y1,x2,y2=box[0],box[1],box[2],box[3]
    print("当box={100:0,100:1,500:2,500:3} x1,y1,x2,y2=",x1,y1,x2,y2)


    box={0:100,1:100,2:500,3:500}
    x1,y1,x2,y2=box[0],box[1],box[2],box[3]
    print("当box={0:100,1:100,2:500,3:500} x1,y1,x2,y2=",x1,y1,x2,y2)

    box=[100,100,500,500]
    x1,y1,x2,y2=box[0],box[1],box[2],box[3]
    print("当box=[100,100,500,500] x1,y1,x2,y2=",x1,y1,x2,y2)

    box=(100,100,500,500)
    x1,y1,x2,y2=box[0],box[1],box[2],box[3]
    print("当box=(100,100,500,500) x1,y1,x2,y2=",x1,y1,x2,y2)

# 结论1：实验不正确，第1组经测试成功裁剪，在这里运行失败

# 实验2：通过迭代起访问
if expNum==2:
    print("实验2，通过下表获得每个值")
    box={100:0,30:1,700:2,300:3}
    it=iter(box)
    x1,y1,x2,y2=next(it),next(it),next(it),next(it)
    print("当box={100:0,100:1,500:2,500:3} x1,y1,x2,y2=",x1,y1,x2,y2)


    box={0:100,1:100,2:500,3:500}
    it=iter(box)
    x1,y1,x2,y2=next(it),next(it),next(it),next(it)
    print("当box={0:100,1:100,2:500,3:500} x1,y1,x2,y2=",x1,y1,x2,y2)

    box=[100,100,500,500]
    it=iter(box)
    x1,y1,x2,y2=next(it),next(it),next(it),next(it)
    print("当box=[100,100,500,500] x1,y1,x2,y2=",x1,y1,x2,y2)

    box=(100,100,500,500)
    it=iter(box)
    x1,y1,x2,y2=next(it),next(it),next(it),next(it)
    print("当box=(100,100,500,500) x1,y1,x2,y2=",x1,y1,x2,y2)

#  enter the num :2
#  实验2，通过下表获得每个值
#  当box={100:0,100:1,500:2,500:3} x1,y1,x2,y2= 100 30 700 300
#  当box={0:100,1:100,2:500,3:500} x1,y1,x2,y2= 0 1 2 3
#  当box=[100,100,500,500] x1,y1,x2,y2= 100 100 500 500
#  当box=(100,100,500,500) x1,y1,x2,y2= 100 100 500 500
#  测试成功！答案符合预期