from node import Node 
from linkedListStack import LinkedListStack
from arrayStack import ArrayStack

class Course:
  def __init__(self ,class_name , students=[]):
    self.class_name = class_name
    self.students = students
  
  def addStudent(self, name):
    self.students.append(name)

  def __str__(self):
    return f"{self.class_name} Students = {self.students}"
    
def main ():
  math = Course('math')
  english = Course('english')
  math.addStudent('ahmad')
  english.addStudent('mohammed')
  print(math)
  print(english)


if __name__ == '__main__':
  main()