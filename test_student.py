from student import student_details

def test_student_details():
    expected_output = (
        "studentid: e1101\n"
        "studentname: Alice\n"
        "student course: BCA\n"
        "student academic year: 2024"
    )

    assert student_details("e1101", "Alice", "BCA", 2024) == expected_output
