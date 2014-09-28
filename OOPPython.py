# @tiggreen
# Some guide to a great Python style design.

class Person:
	def __init__(self, age,name):
		print("Calling parent's constructor")
		self.name = name
		self.salary = salary
		Employee.empCount += 1
	
	def parentMethod(self):
		print("Calling parent's method")

"""
class Employee(Person, World)
This would mean that Employee class is a subclass for
Person and World classes. 
"""

class Employee(Person):
	'This is a regular class doc for Employee class.'
	
	empCount = 0
	
	def __init__(self,salary):
		print("calling child's constructor")
		self.salary = salary
		Employee.empCount += 1
		
	def childMethod(self):
		print("Calling child's method")
		
	#using decorator for display count method.
	@staticmethod
	def displayCount(self):
		print("Number of employees is: " + str(Employee.empCount))
		
	#A variant of the static method is the class method. 
	@classmethod
	def displayCount2(cls):
		print("number of employees is:" + str(cls.empCount))
		
	def __del__(self):
		class_name = self.__class__.__name__
		print(class_name, "destroyed")
	
    # @abstractmethod
    # def vehicle_type():
    #     """"Return a string representing the type of vehicle this is."""
    #     pass

def main():
	four_nones = [None] * 4
	
	ten_zeros = [0] * 10
	
	ll = [ [0 for __ in range(5)] for __ in range(4)]
	
	letter = ['T', 'i', 'g', 'r', 'a', 'n']
	st = ' '.join(letter)
	print(st)
	print(four_nones)
	e = Employee(100)
	e.childMethod()
	e.parentMethod()
	
	a = [3, 4, 5, 12]
	b = [i for i in a if i > 4]
	print(b)
	
	# with open('Node.py') as f:
	# 	for line in f:
	#         print(line)

	#print(e.salary)

main()