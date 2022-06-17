'''def print_grade(midterm_score, final_score):
    total_score = midterm_score + final_score
    if total_score >= 90:
        return 'A'
    elif total_score >= 80:
        return 'B'
    elif total_score >= 70:
        return 'C'
    elif total_score >= 60:
        return 'D'
    else:
        return 'F'


for i in range(1, 5, 2):
    print(i)
1, 1, 2, 3, 5, 8, 13, 21

i = 0

while i <15:
    i = i + 1

    if i % 2 == 1:
        continue
    print(i)
'''
numbers = [1,2,3,4,5,5,6,7,8,9,10]
numbers.extend([200, 201, 202])
print(numbers)

del numbers[0]
print(numbers)