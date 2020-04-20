for p in range(10, 0, -1):
    if p != 6:
        print("*"*p)


lst = []
for p in range(1, 10):
    second = p * 2
    lst.append(second)
print(lst)

num = 0
result = 0
while num < 1000:
    num += 1
    if (num % 3) != 0:
        continue
    result += num
print(result)
        
    
mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
sum = 0
for score in mutsa_scores:
    sum += score
print(sum/6)




