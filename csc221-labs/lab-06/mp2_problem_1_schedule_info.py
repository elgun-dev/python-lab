# Problem 1: Schedule Info
# This program shows room, instructor, and time for a course.

rooms = {
    "CS101": "3004",
    "CS102": "4501",
    "CS103": "6755",
    "NT110": "1244",
    "CM241": "1411",
}

instructors = {
    "CS101": "Haynes",
    "CS102": "Alvarado",
    "CS103": "Rich",
    "NT110": "Burke",
    "CM241": "Lee",
}

times = {
    "CS101": "8:00am",
    "CS102": "9:00am",
    "CS103": "10:00am",
    "NT110": "11:00am",
    "CM241": "1:00pm",
}

course = input("Enter a class name:\n")
course = course.upper()

if course in rooms:
    print(f"Class: {course}")
    print(f"Room: {rooms[course]}")
    print(f"Instructor: {instructors[course]}")
    print(f"Time: {times[course]}")
else:
    print(f"{course} was not found.")
