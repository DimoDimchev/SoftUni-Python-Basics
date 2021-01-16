name = input()

grade = float(input())
sum_grades = 0
average_grade = 0

grade_count = 1
fail_count = 0

while 1 == 1:
    sum_grades += grade
    if grade < 4.00:
        fail_count += 1
    if fail_count > 1:
        print(f"{name} has been excluded at {grade_count-1} grade")
        break
    if grade_count == 12:
        average_grade = sum_grades / grade_count
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
    grade_count += 1
    grade = float(input())

