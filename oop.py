class Person:
  def __init__(self,name,age,gender):
    self.name=name
    self.age=age
    self.gender=gender
  def introduce(self):
    print(f"My name is {self.name} my age is {self.age} i indentify as {self.gender}")

obj=Person("tam",21,"female")
obj.introduce()
