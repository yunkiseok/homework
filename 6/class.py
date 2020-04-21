class FourCal:
    def __init__(self, name, age, university): 
        self.name = name 
        self.age = age
        self.university = university
        self.add_num = 0
        self.min_num = 0
        self.mul_num = 0
        self.div_num = 0
    def add(self, n1, n2):
        self.add_num += 1
        result = n1 + n2 
        return result    
    def minus(self, n1, n2):
        self.min_num += 1
        result = n1 - n2
        return result
    def multiple(self, n1, n2):
        self.mul_num += 1
        result = n1 * n2 
        return result
    def divide(self, n1, n2):
        self.div_num += 1
        if n2 == 0:
            print("0으로 나눌 수 없습니다!")
            return None
        result = n1 / n2 
        return result
    def ShowCount(self):
        print("덧셈:", self.add_num)
        print("뺄셈:", self.min_num)
        print("곱셈:", self.mul_num)
        print("나눗셈:", self.div_num)

cal = FourCal("윤기석", 26, "고려대")
print(cal.add(4, 2))
print(cal.minus(4, 2))
print(cal.multiple(4, 2))
print(cal.divide(4, 1))
cal.divide(4,2)
cal.minus(3,2)

cal.ShowCount()