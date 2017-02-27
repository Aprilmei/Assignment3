'''
Created on 27 Feb 2017

@author: April
'''

import urllib.request
import re
import argparse
from sklearn.metrics.cluster.unsupervised import check_number_of_labels
from _ast import Num


light=[0]
N=0
# request
def read_url(link):
    req = urllib.request.urlopen(link)
    content = req.read().decode('utf-8')
    content_lines=content.splitlines() 
    return content_lines


def read_command(command,x):
    global light #2d list for light 
    x1=x[0]
    y1=x[1]
    x2=x[2]+1
    y2=x[3]+1
   
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
    #print(calculate_light())
    return light

def calculate_light():
    global light
    number=0
    for i in range(N):
        for j in range(N):
            number+=light[i][j]
    return number

def check_command(num_list):
    for i in range(len(num_list)):
        if(num_list[i]<0):
            num_list[i]=0
        if(num_list[i]>N):
            num_list[i]=N-1
    return num_list

def switch_light(link):
    
    global light
    global N
    buffer=read_url(link)
    firstLine = buffer[0]
    N=int(firstLine)
    light=[ [0]*N for _ in range(N) ]
    for line in buffer[1:]:
    # process line   
        numbers_line=re.findall("[-\d]+", line)
        numbers_line= [int(e) for e in numbers_line]
        #print(numbers_line)
        Not_consistent=False
        if(numbers_line[0]>numbers_line[2] or numbers_line[1]>numbers_line[3]):
            Not_consistent=True
        if(len(numbers_line)!=4 or Not_consistent):
            continue
        check_command(numbers_line)
        values = line.strip().split()           
        if(values[0]=='switch'):
            values[0]='switch'
        elif(values[0]=='turn' and values[1]=='off'):
            values[0]='off'
        elif(values[0]=='turn' and values[1]=='on'):
            values[0]='on'
        read_command(values[0],numbers_line)
    print(link ,calculate_light())
    return 


uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt"
switch_light(uri)
'''
uri_a = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt"
uri_b = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt"

uri_d = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt"


switch_light(uri_a)
switch_light(uri_b)

switch_light(uri_d)
'''



