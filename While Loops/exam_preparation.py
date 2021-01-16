limit = int(input())

bad_grades = 0
grade_sum = 0
grade_count = 0
last_problem = ""

success = False

while bad_grades < limit:
    problem_name = input()
    if problem_name == "Enough":
        success = True
        break

    problem_grade = int(input())
    if problem_grade <= 4:
        bad_grades += 1

    last_problem = problem_name
    grade_sum += problem_grade
    grade_count += 1

if not success:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    average_score = grade_sum / grade_count
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {grade_count}")
    print(f"Last problem: {last_problem}")

