class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        return f"Hi, I'm {self.name}. I'm {self.age} years old and studying {self.course}."

    def update_course(self, new_course):
        self.course = new_course
        return f"{self.name} has switched to {new_course}."

# Creating two objects (students)
student1 = Student("David", 20, "Computer Science")
student2 = Student("Sarah", 19, "Engineering")

print(student1.introduce())
print(student2.introduce())

# Updating course
print(student1.update_course("Artificial Intelligence"))
print(student1.introduce())
