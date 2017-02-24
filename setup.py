from setuptools import setup

setup(name="A3Mei_Fangxue_15210672",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Mei Fangxue",
      author_email="sanchiyou@msn.cn",
      licence="GPL3",
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
          }
      #Github  https://github.com/Aprilmei/Assignment3.git
      )