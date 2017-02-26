from setuptools import setup

setup(name="A3",
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