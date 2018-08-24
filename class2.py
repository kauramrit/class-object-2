#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

class circle():
    def __init__(self,r):
        self.radius=r
    def getArea(self):
        area=3.14*self.radius*self.radius
        print("area:",area)
    def getCircumference(self):
        circum=2*3.14*self.radius
        print("circumference:",circum)
a=circle(3)
a.getArea()
a.getCircumference()


#Q.2- Create a Student class and initialize it with name and roll number. Make methods to : 
#1. Display - It should display all informations of the student. 
#2. setAge - It should assign age to student
#3. setMarks - It should assign marks to the student.

class Student():
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def display(self):
        print('name:{},rollno:{}'.format(self.name,self.rno))
    def setAge(self,age):
        self.age=age
        print('age:',self.age)
    def setMarks(self,marks):
        self.marks = marks
        print('marks:',self.marks)
a=Student('amrit',1099)
a.display()
a.setAge(19)
a.setMarks(80)

#Q.3- Create a Temprature class and create two methods: 
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class Temprature():
    def  convertFahrenhiet(self,celsius):
        fahre=celsius*(9/5)+32
        print("Fahrenheit:",fahre)
    def convertCelsius(self,farenhiet):
        cel=farenhiet-32*(5/9)
        print("Celsius:",cel)
t=Temprature()
t.convertFahrenhiet(23)
t.convertCelsius(45)


#Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
#Make methods to 
#1. Display-Display the details. 
#2. Add- Add the movie details.

class MovieDetails():
    def __init__(self,artistname,yr_release,rating):
        self.artistname=artistname
        self.yr_release=yr_release
        self.rating=rating
    def display(self):
        print('Artistname:{},yr_release:{},rating:{}'.format(self.artistname,self.yr_release,self.rating))
    def Add(self,add):
        self.add=add
        print("add movie name:",self.add)
m=MovieDetails('ranveer singh',2017,5)
m.display()
m.Add('padmavat')
       
#Q.5- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.

class Animal():
    def animal_attribute(self):
        print("animal")

class Tiger(Animal):
    def Tiger_attribute(self):
        print("tiger")

a=Tiger()
a.animal_attribute()

#Q.6- What will be the output of following code. 

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print a.f(), b.f()
print a.g(), b.g()

output will be error-->becoz print statement doesnt contain open and closing bracket

#Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area.Create class rectangle and square which inherits shape and access the method Area.

class Shape():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def Area(self):
        area=self.length*self.breadth
        print("area:",area)
class rectangle(Shape):
    def rec(self):
        print("rectangle")
class square(Shape):
    def sq(self):
        print("square")
a=Shape(2,5)
b=rectangle(2,5)
b.Area()
c=square(2,5)
c.Area()
    

              
              
              

