#计数循环
"""
Number = [1, 2, 3, 4, 5]
for i in Number:
    print(i)
print(i)


#累加

List = [34,6,27,90]
Sum = 0
for Price in List:
    Sum = Sum + Price
    print(Sum)
print(Sum)


#遍历一个字符串里的每个单个字符

word = "incredible"
for i in word:
    print(i)


for letter in "incredible":
    print(letter)


#while循环

Number = [1, 2, 3, 4, 5]
j = 0
while j < 5:    #注：这里是5
    print(Number[j])
    j = j + 1



Number = [1, 2, 3, 4, 5]
j = 0
while j < 4:    #注：这里是4，否则越界
    j = j + 1
    print(Number[j])


#continue 结束本次迭代（小循环）

Number = [1, 2, 3, 4, 5, 6, 7, 8, 9]        #母版程序
for i in Number:                            #打印出大于5的数
    if i <= 5:
        continue
    print(i)

Number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in Number:
    if i <= 5:
        continue
    print(i)        #按顺序执行处于同一级的print()语句
print(i)            #print()与for循环同级，只有当for循环结束以后，才按顺序执行print()，打印出for循环结束时最终i的值。

Number = [1, 2, 3, 4, 5, 6, 7, 8, 9]        
for i in Number:
    if i <= 5:
        continue
        print(i)
    print(i)

Number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in Number:
    if i <= 5:
        continue
        print(i)
 

#break 跳出整个大循环 

Number = [1, 2, 3, 4, 5, 6, 7, 8, 9]        #母版程序
for i in Number:                            #打印出小于等于5的数
    if i > 5:
        break
    print(i)

Number = [1, 2, 3, 4, 5, 6, 7, 8, 9]       #母版程序 
for i in Number:
    if i > 5:
        break
        print(i)

Number = [1, 2, 3, 4, 5, 6, 7, 8, 9]        #母版程序
j = 0
while j < 9:
    if Number[j] > 5:
        j = j + 1
        continue
    print(Number[j])
    j = j + 1


#过滤器

Number = [35, 73, 1, 785, 8]
for i in Number:
    if i < 10:
        continue
    print(i)


#筛出满足条件的前3个数据

Number = [13, 6, 35, 8, 24, 11, 57, 46, 23]
j = 0
for i in Number:
    if i <= 10:
        continue
    print(i)
    j = j + 1
    if j == 3:
        break


#range  list里有“右-左+1”个数，遵循“左开右闭”原则

a = range(11)
print(list(a))

a = range(1,10)
print(list(a))

a = range(0)
print(list(a))

#range()  （范围）

Sum = 0                     #从1到100的累加
for i in range(101):
    Sum = Sum + i
print(Sum)

Sum = 0                     #从1到100中的偶数的累加
for i in range(101):
    if i % 2 == 0:
        Sum = Sum + i
print(Sum)

List = []                   #写出一个从1到100里偶数的列表
for i in range(101):
    if i % 2 ==0:
        List.append(i)
print(List)


#len()  （长度）

Number = [1, 2, 3, 4, 5, 6, 7, 8, 9]        
j = 0
while j < len(Number):
    if Number[j] > 5:
        j = j + 1
        continue
    print(Number[j])
    j = j + 1

List = [12, 63, 57, 33, 64, 18, 30]        #奇偶数的分类
even = []
odd = []
while len(List) > 0:
    num = List.pop()
    if num % 2 == 0:
        even.append(num)
    else :
        even.append:
        odd.append(num)
print(even)
print(odd)

List = [12, 63, 57, 33, 64, 18, 30]        #奇偶数的分类和累加
n = 0
EvenSum = 0
OddSum = 0
while n < len(List):
    if List[n] % 2 == 0:
        EvenSum = EvenSum + List[n]
    else :
        OddSum =OddSum + List[n]
    n = n + 1
print(EvenSum)
print(OddSum)

numbers = [12, 63, 57, 33, 64, 18]          #分类放置
n = 0
List1 = []
List2 = []
while n < 6:
    number = numbers.pop()
    if number < 35:
        List1.append(number)
    else :
        List2.append(number)
    n = n + 1
print(List1)
print(List2)


#tuple 元组

EvenNumber = (2, 4, 6, 8, 10)
print(EvenNumber)
print(EvenNumber[0])

# 注：Python在输出只有一个元素的元组时，必须在元素后方加一个逗号，不然这个字段会被认定为其他数据来处理，运行时就会报错

#切片  遵左开右闭原则

SomeNumber = (1,5,3,8,4,9,10)
print(SomeNumber[1:3])
print(SomeNumber[:5])
print(SomeNumber[4:])


#list与tuple的嵌套:用两次索引

BigCityList = [1, "Beijing", ("ShangHai", "GuangZhou", "ShenZhen")]
print(BigCityList[2])
print(BigCityList[2][0])

BigCityList = (1, "Beijing", ["ShangHai", "GuangZhou", "ShenZhen"])
print(BigCityList[2])
print(BigCityList[2][0])
"""

#字典 dict  储存方式：键值key（键）-value（值）
Hit = {"apple":100, "milk":150}
print(Hit.keys())
print(Hit.values())
print(Hit["apple"])

Hit["apple"] = 120        #修改元素
print(Hit["apple"])

Hit["banana"] = 200       #添加元素
print(Hit["banana"])
print(Hit)




