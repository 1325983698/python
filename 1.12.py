#if判断
"""
myweight = 55
canride = True
if myweight > 90:
    canride = False
    print ('超重')
print(canride)
"""

#if-else 语句
"""
MyAge = 18
YourAge = 20
if MyAge < YourAge:
    print("you are older than me")
else:
    print("you are not older than me")
"""

#elif 语句
"""
MyAge = 20
YourAge = 20
if MyAge < YourAge:
    print("you are older than me")
elif MyAge == YourAge:
    print("we have the same age")
else:
    print("I am older than you")
"""


"""
weather = "晴天"
if weather == "晴天":   
    print("Ok")
else:
    print("No")
"""

#列表、列表的修改
"""
Fruit = ["apple" ,"banana", "orange"]
print(Fruit[2])
Fruit[2] = "grape"
print(Fruit[2])
"""

#访问字符串中的数据
"""
poem = "无边落木萧萧下"
print(poem[3])
poem[3] = "叶"    #通过索引改变一个字符串里的字符会报错
print(poem[3])
"""

#列表的添加 append
"""
Fruit = ["apple" ,"banana", "orange"]
Fruit.append("grape")
print(Fruit)
"""

#列表的插入 insert
"""
Number = [1, 2, 3, 4]
Number.insert(0,100)
print(Number[1])
print(Number)
Number.insert(5,200)    #插入的位置是插入后所在的位置
print(Number)
"""

#列表的弹出 （列表操作）pop
"""
Number = [1, 2, 3, 4, 5]
print(Number)
Number.pop(1)
print(Number)
LastData = Number.pop()
print(Number)
print(LastData)
"""

#列表的弹出 （python通用)del
Number = [1, 2, 3, 4, 5]
print(Number)
del(Number[1])
print(Number)
