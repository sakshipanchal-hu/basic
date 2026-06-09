class animal:
    def fun1(self):
        print("Animal makes sound.")

class cat(animal):
    def fun2(self):
        print("cat meows")

class kitten(cat):
    def fun3(self):
        print("cat baby")

obj = kitten();
obj.fun1()
obj.fun2()
obj.fun3()



class Grandparent:
    def fun1(self):
        print("I am the Grandparent.")

class Parent(Grandparent):
    def fun2(self):
        print("I am the Parent.")

class Child(Parent):
    def fun3(self):
        print("I am the Child.")

obj = Child()
obj.fun1()
obj.fun2()
obj.fun3()