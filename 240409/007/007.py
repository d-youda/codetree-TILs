class Secrete():
    def __init__(self, code, place,time):
        self.code = code
        self.place = place
        self.time = time

    def solve_secrete(self):
        print("secret code :",code)
        print("meeting point :",place)
        print("time :",time)

code, place, time = input().split()

first_code = Secrete(code, place, time)
first_code.solve_secrete()