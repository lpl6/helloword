# num=eval(input("请输入您的号码："))
# if num==987654:
#     print("恭喜您，中将了")
# if num!=987654:
#     print("很遗憾，没中奖")
print('-----------布尔类型')
n=98
if n%2:
    print(n)
if not n%2:
    print(n)
x=input('请输入一个字符串')
if x:
    print('不是一个空字符串')
if not x:
    print('是一个空字符串')
#如果if后只有一句语句块，可以直接写在冒号后
a=5
b=10
if a<b:max=a