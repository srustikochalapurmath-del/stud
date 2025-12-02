import pytest

def student_details(stud_id, name, course, year):
    result = (
        f"studentid: {stud_id}\n"
        f"studentname: {name}\n"
        f"student course: {course}\n"
        f"student academic year: {year}"
    )
    return result


if __name__ == "__main__":
    stud_id = "e1101"
    name = "Alice"
    course = "BCA"
    year = 2024

    print(student_details(stud_id, name, course, year))
