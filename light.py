import sys

#from src.led_tester import *
N=1000
light= [ [0]*N for _ in range(N) ]
def read_command(command,x,y):
    global light #2d list for light 
    x1=x[0]
    y1=x[1]
    x2=y[0]+1
    y2=y[1]+1
    #this is the control the light 
    for i in range(x1,x2):
        number=0
        for j in range(y1,y2):
            if(light[i][j]==0):
                if(command=='off'):
                    light[i][j]=0;
                else:
                    light[i][j]=1;
            else:
                if(command=='on'):
                    light[i][j]=1;
                else:
                    light[i][j]=0;
            number+=1
    
    return light

def calculate_light():
    global light
    number=0
    for i in range(1000):
        for j in range(1000):
            number+=light[i][j]
    print(number)

line1='switch'
a=[322, 558]
c=[977, 958]
read_command(line1, a, c)
calculate_light()


