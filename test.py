import sys
from nose.tools import *
from src.led_tester import *

def test_readfile():
    filename ="input_assign3.txt"
    buffer= read_file(filename=filename);
    eq_()
    
    
def test_calculate():
    line1='turn on'
    a=(100,300)
    c=(500,800)
    read_command(line1, a, c)
    eq_(read_command(line1,a,c), 6000, 'calculation is incorrect')
