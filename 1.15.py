#类 class
"""
class Person:
def __init__(self, name, hight, wight):
    self.name = name
    self.hight = hight
    self.wight = wight
   
    def print_name(self):
        print(self.name)

    def print_hight(self):
        print(self.hight)

    def print_wight(self):
        print(self.wight)

PersonA = Person("tony", 178, 145)
PersonA.display_name()
PersonB = Person("kevin", 183, 140)
PersonB.display_name()
"""
class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)
    
PersonA = Person("tony")
PersonA.print_name()

#tony的最高分
class Student:
    	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

	def get_course(self):
		return max(self.score)

Tony = Student('Tony', 20, [69, 88, 100])
print(Tony.get_course())

#杯子的容量
class bottle:
    	def __init__(self,capacity):
		self.capacity = capacity
	def introduce(self):
		return self.capacity

a = bottle(600)
print(a.introduce())

#食物的热量
class food:
    	def __init__(self,caloric):
		self.caloric = caloric
	def introduce(self):
		return self.caloric

milk = food('200')
print(milk.introduce())

#扑克牌
class Poker :
    	def __init__(self,colour,num):
		self.colour = colour
		self.num = num
	def play(self):
		print(f"打出一张{self.colour}{self.num}")
p = Poker("黑桃","A")
p.play()

#水果
class Fruit:
    	def __init__(self,kind,weight):
		self.kind = kind
		self.weight = weight
	def introduce(self):
		print(f"这是一个{self.weight}的{self.kind}")
apple = Fruit("苹果","30g")
apple.introduce()

#成绩单
class SchoolReport:
    	def __init__(self,report):
		self.report = report
	def MaxScore(self):
		return max(self.report)
Class1 = SchoolReport([81, 76, 69, 66, 62, 87, 90, 89])
print(Class1.MaxScore())

#继承
class Car:
    def __init__(self, brand):
        self.brand = brand

    def car_brand(self):
        print(self.brand)

class Audi(Car):
    def __init__(self, type):
        self.brand = "Audi"
        self.type = type

    def car_type(self):
        print(self.type)

CarA = Car("BMW")
CarA.car_brand()
CarB = Audi("A4")
CarB.car_brand()
CarB.car_type()

#矩形
class rectangle:
    	def __init__(self,length,width):
		self.length = length
		self.width = width
	def area(self):
		print(self.length*self.width)
class square(rectangle):
	def __init__(self,length):
		self.length = length
		self.width = length

figur1 = rectangle(4,6)
figur1.area()
figur2 = square(5)
figur2.area()

#手机系统
class OS:
    	def __init__(self,brand):
		self.brand = brand
	def introduce(self):
		print(self.brand)

class IOS(OS):
	def __init__(self,version):
		self.brand = 'IOS'
		self.version = version
	def introduce(self):
		print(self.brand+self.version)

PhoneA = OS('Android')
PhoneA.introduce()
PhoneB = IOS('13')
PhoneB.introduce()