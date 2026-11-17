# Student Management System

A command-line Student Management System built with Python and Object-Oriented Programming (OOP). This project allows users to manage student records, track grades, and store information using JSON file persistence.

## Features

- **Add Students:** Register new students with their ID, name, age, and course.
- **View Students:** Display all registered students.
- **Search Students:** Find students using their ID or name.
- **Update Information:** Modify existing student details.
- **Manage Grades:** Add grades and calculate student averages.
- **Letter Grades:** Automatically determine letter grades.
- **Delete Students:** Remove student records.
- **Data Persistence:** Save and load student records using JSON files.
- **Input Validation:** Handle invalid and unexpected user input.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- `pathlib`
- `unittest`

## Project Structure

```text
student-management-system/
│
├── main.py
├── student.py
├── student_manager.py
├── utils.py
│
├── data/
│   └── .gitkeep
│
├── tests/
│   └── test_student_manager.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/student-management-system.git
```

### 2. Navigate to the Project Directory

```bash
cd student-management-system
```

### 3. Run the Application

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

## Running Tests

The project includes unit tests to check the functionality of the student management system.

Run the tests with:

```bash
python -m unittest discover -s tests -v
```

## What I Learned

Through this project, I practiced:

- Creating classes and objects in Python.
- Understanding constructors and instance attributes.
- Working with methods, properties, and class methods.
- Organizing code into multiple modules.
- Implementing CRUD operations.
- Reading and writing JSON files.
- Handling exceptions and validating user input.
- Writing unit tests using `unittest`.

## Author

**Farid Hassani**

Aspiring Python Developer | Information Systems Graduate

[GitHub Profile](https://github.com/fred5566)

---

*This project was developed as part of my practical Python programming journey, with a focus on Object-Oriented Programming and real-world application development.*
