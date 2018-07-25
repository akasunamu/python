def check(x,y):
    if 5*x*x/4+abs(x)*y*3+5*y*y<1280:
        return True
    else:
        return False

for y in range(-30,30):
    for x in range(-50,50):
        if check(x,y):
            print("love"[(x+y)%4],end='')           
        else:
            print(" ",end='')
    print('')


    