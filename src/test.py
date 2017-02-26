##test.py
import sys
from A3.light_test import *
 
from nose.tools import *

def test_calculate():
    eq_(calculate(2,3), 6, 'calculation is incorrect')

def test_read_url():
    


def test_version():
    eq_(sys.version_info[0], 3, 'Python is not version 3')


def read_url(link):
    req = urllib.request.urlopen(link)
    content = req.read().decode('utf-8')
    content_lines=content.splitlines() 
    return content_lines


def read_command(command,x):
    global light #2d list for light 
    x1=x[0]
    y1=x[1]
    x2=x[2]
    y2=x[3]
    if(x1>x2):
        x1,x2=x2,x1
    if(y1>y2):
        y1,y2=y2,y1
    x2+=1
    y2+=1
    #this is the control the light 
    #print(command,x1,x2,y1,y2)
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
    for i in range(N):
        for j in range(N):
            number+=light[i][j]
    return number

def test_switch_light():
    
    eq_(test_switch_light()[0], 3, 'Python is not version 3')






