a=[1,2,3,4,5,6,7,8,9,10]
print("list a is",a)
a2d=[a,a,a,a]
print("list a2d is ")
print(a2d)
N=6;
a2d2=[ list(range(i*N, i*N + N)) for i in range(N) ]
print(a2d2[1])
        

N = 6
a2d = [ [0]*N for _ in range(N) ]
print(a2d)

# use readlines to read a line a time
filename = "data/data.txt"
with open(filename) as f:
    for line in f.readlines():
        # process line        
        values = line.strip().split()
        
# read the whole file into a buffer
buffer = open(filename).read()

for line in buffer.split('\n'):
    # process line
    

# request


def read_uri(fname):
    if fname.startswith('http'):
        # use urllib.request.urlopen(uri)
    else:
        # use open(uri)
    return ...

#this one is for the input and output 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input help')
args = parser.parse_args()

filename = args.input