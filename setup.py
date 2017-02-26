from setuptools import setup
import sys

egg_path='/home/ubuntu/anaconda3/envs/venv3/lib/python3.6/site-packages/A3-0.1-py3.6.egg'

sys.path.append(egg_path)

setup(name="A3Mei_Fangxue_15210672",
      version="0.2",
      description="Led test for science building",
      url="",
      author="Mei Fangxue",
      author_email="sanchiyou@msn.cn",
      licence="GPL3",
      package=['A3'],
      entry_points={
          'console_scripts':['led_tester=A3.light_test:switch_light']
          }
      #Github  https://github.com/Aprilmei/Assignment3.git
      )