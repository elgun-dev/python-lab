# Problem 5: Grade Calculator
# This program calculates category averages, course average, and course grade.

# These constants store the maximum possible points in each category.
HOMEWORK_MAX = 800.0
QUIZZES_MAX = 400.0
MIDTERM_MAX = 150.0
FINAL_MAX = 200.0

# Read the student status.
print("Enter the student status.")
print("Use UG for undergrad, G for grad, or DL for distance learner.")
status = input("Student status: ")

# Only continue if the student status is valid.
if status != "UG" and status != "G" and status != "DL":
    print("Error: student status must be UG, G or DL")
else:
    # Read the points earned in each category.
    print("Enter homework points, quiz points, midterm exam score, and final exam score.")
    print("Example: 600.0 300.0 120.0 150.0")
    homework_points, quiz_points, midterm_points, final_points = input("Scores: ").split()
    homework_points = float(homework_points)
    quiz_points = float(quiz_points)
    midterm_points = float(midterm_points)
    final_points = float(final_points)

    # Calculate the average for each category.
    homework = (homework_points / HOMEWORK_MAX) * 100
    quizzes = (quiz_points / QUIZZES_MAX) * 100
    midterm = (midterm_points / MIDTERM_MAX) * 100
    final_exam = (final_points / FINAL_MAX) * 100

    # Cap each category at 100%.
    if homework > 100:
        homework = 100.0
    if quizzes > 100:
        quizzes = 100.0
    if midterm > 100:
        midterm = 100.0
    if final_exam > 100:
        final_exam = 100.0

    # Choose the correct weights based on student status.
    if status == "UG":
        course_average = homework * 0.20 + quizzes * 0.20 + midterm * 0.30 + final_exam * 0.30
    elif status == "G":
        course_average = homework * 0.15 + quizzes * 0.05 + midterm * 0.35 + final_exam * 0.45
    else:
        course_average = homework * 0.05 + quizzes * 0.05 + midterm * 0.40 + final_exam * 0.50

    # Choose the final letter grade.
    if course_average >= 90:
        grade = "A"
    elif course_average >= 80:
        grade = "B"
    elif course_average >= 70:
        grade = "C"
    elif course_average >= 60:
        grade = "D"
    else:
        grade = "F"

    # Display all category averages and the final grade.
    print(f"Homework: {homework:.1f}%")
    print(f"Quizzes: {quizzes:.1f}%")
    print(f"Midterm: {midterm:.1f}%")
    print(f"Final Exam: {final_exam:.1f}%")
    print(f"{status} average: {course_average:.1f}%")
    print(f"Course grade: {grade}")
