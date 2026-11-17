# Student Management System (Python)

A beginner-friendly command-line application for managing student records. It uses object-oriented programming and stores data locally in a JSON file.

## Features

- Add a student with a unique ID
- View all students
- Search by student ID or name
- Update student details
- Add and remove subject grades
- Calculate an individual average and letter grade
- Delete a student after confirmation
- Generate an individual student report
- Generate a class summary
- Automatically save data to `data/students.json`

## Requirements

- Python 3.8 or newer
- No third-party packages are required

## Run the project

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

On some systems, use `python3 main.py`.

## Example workflow

1. Select `1` and add a student:
   - ID: `ST001`
   - Name: `Sara Ahmad`
   - Age: `20`
   - Course: `Python`
2. Select `5` to add a grade:
   - Student ID: `ST001`
   - Subject: `Python Basics`
   - Grade: `92`
3. Select `8` to view the student's report.

The `data` folder and JSON file are created automatically after the first change.

## Project structure

```text
student-management-system/
├── main.py
├── student.py
├── student_manager.py
├── utils.py
├── data/
│   └── students.json   # created automatically
├── tests/
│   └── test_student_manager.py
├── README.md
└── .gitignore
```

## Concepts demonstrated

- Variables, data types, conditions, and loops
- Functions and modular programming
- Classes, objects, methods, and properties
- Lists and dictionaries
- File handling and JSON serialization
- Input validation and exception handling
- CRUD operations (Create, Read, Update, Delete)

## Grade scale

| Average | Letter |
|---:|:---:|
| 90–100 | A |
| 80–89.99 | B |
| 70–79.99 | C |
| 60–69.99 | D |
| 0–59.99 | F |


## Author
Farid Hassani
