# use readlines to read a line a time
import os

def read_command(command,x,y):
    global light #2d list for light 
    x1=x[0]
    y1=x[1]
    x2=y[0]+1
    y2=y[1]+1
    #this is the control the light 
    print(command,x1,x2,y1,y2)
    for i in range(x1,x2):
        for j in range(y1,y2):
            if(light[i][j]==0):
                if(command=='off'):
                    light[i][j]=0;
                elif(command=='switch'):
                    light[i][j]=1;
                else:
                    light[i][j]=1;
            elif(light[i][j]==1):
                if(command=='on'):
                    light[i][j]=1;
                elif(command=='switch'):
                    light[i][j]=0;   
                else:
                    light[i][j]=0;
    
    return light

def calculate_light():
    global light
    number=0
    for i in range(1000):
        for j in range(1000):
            number+=light[i][j]
    print(number)
    
filename = "input_assign3.txt"
        
# read the whole file into a buffer
buffer =open(filename,'r', encoding='UTF-8');

firstLine = buffer.readline()
print(firstLine)
N=int(firstLine)
light=[ [0]*N for _ in range(N) ]
for line in buffer:
    # process line   
    #print(line)
    xn=[0]*2
    yn=[0]*2    
    values = line.strip().split()           
    if(values[0]=='switch'):
        x=values[1].split(',')
        y=values[3].split(',')
        xn= [int(e) for e in x]
        yn= [int(e) for e in y]
    elif(values[0]=='turn' and values[1]=='off'):
        values[0]='off'
        x=values[2].split(',')
        y=values[4].split(',')
        xn= [int(e) for e in x]
        yn= [int(e) for e in y]
    elif(values[0]=='turn' and values[1]=='on'):
        values[0]='on'
        x=values[2].split(',')
        y=values[4].split(',')
        xn= [int(e) for e in x]
        yn= [int(e) for e in y]        
    read_command(values[0],xn,yn)
calculate_light()
buffer.close();

