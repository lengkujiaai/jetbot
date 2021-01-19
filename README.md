### author lengkujiaai@126.com

# 本程序是对nvidia jetbot的修改版

1、nvidia jetbot是调用的两轮小车，靠左右两个轮子的差速实现转向，在有些小车上面效果不好

2、本jetbot增加了对舵机的调用，是四轮小车，靠舵机改变前面两个轮子的方向，靠后侧两个同轴轮子驱动前进

3、目前已经调通basic_motion、teleopration、object_following的舵机版，效果不错，road_following和collision_avoidance的效果还不好，等调好后及时更新

4、我的舵机的三根线，黄色线连jetson nano的37号pin，红色线连的4号pin，黑色线连的39号pin

5、舵机的信号线也可以连其它的pin，40根针脚中有22个可以使用，但注意把pwm.py文件中的37做对应的修改

6、不建议把舵机的红色、黑色线连到nano上，这样可能导致供电不足而断电


# 看看我的小车 
![image](https://github.com/lengkujiaai/jetbot/blob/master/readme_image/steering_jetbot.png)

# JetBot

<!--[<img src="https://img.shields.io/discord/553852754058280961.svg">](https://discord.gg/Ady6NtF) -->

> Looking for a quick way to get started with JetBot?  Many third party kits are [now available](https://jetbot.org/master/third_party_kits.html)!

<img src="../..//wiki/images/jetson-jetbot-illustration_1600x1260.png" height="256">



To get started, read the [JetBot documentation](https://jetbot.org).

## Get involved
欢迎把任何的想法和建议发我邮箱

<!--* Join the [chat server](https://discord.gg/Ady6NtF)-->
* Ask a question and discuss JetBot related topics on the [JetBot GitHub Discussions](https://github.com/NVIDIA-AI-IOT/jetbot/discussions)
* Report a bug by [creating an issue](https://github.com/NVIDIA-AI-IOT/jetbot/issues)
* Share your project or ask a question on the [Jetson Developer Forums](https://devtalk.nvidia.com/default/board/139/jetson-embedded-systems/)

![image](https://github.com/lengkujiaai/jetbot/blob/master/readme_image/zhangzong.png)
