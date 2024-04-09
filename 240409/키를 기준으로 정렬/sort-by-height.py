class Student():
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight

    def printStudent(self):
        print(self.name,self.tall, self.weight)

num = int(input()) #총 입렵받을 명 수
student_list = []
for _ in range(num):
    name, tall, weight = input().split()
    student_list.append(Student(name, int(tall), int(weight)))

student_list = sorted(student_list,key=lambda x : x.tall)
for i in range(len(student_list)):
    student_list[i].printStudent()