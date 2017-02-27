from setuptools import setup

setup(name="ledtester",
      version="0.2",
      description="Led test for science building",
      url="",
      author="Mei Fangxue",
      author_email="sanchiyou@msn.cn",
      licence="GPL3",
      package=['ledtester'],
      entry_points={
          'console_scripts':['led_tester=ledtester.light:switch_light']
          }
      #Github  https://github.com/Aprilmei/Assignment3.git
      )