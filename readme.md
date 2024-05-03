## Student Information System (SDU University)

This repository contains a Python program for managing student information within SDU University. The system allows an administrator to perform various tasks related to student records, including adding, updating, and deleting student information, as well as managing student reports.

### Files

- **administrator.py**: Defines the `Administrator` class responsible for managing student records. This includes functionalities to add, update, delete students, add student reports, and generate student reports.
  
- **app.py**: Main entry point of the program. Executes the `main()` function from `main.py` to run the student information system.

- **main.py**: Contains the main logic for interacting with the student information system. It prompts the user for different actions (e.g., adding/updating/deleting students, generating reports) through a console interface.

- **person.py**: Defines the `Person` class, which represents a generic person with attributes like name and email.

- **student.py**: Defines the `Student` and `Course` classes. `Student` inherits from `Person` and includes methods for managing student courses and calculating GPA. `Course` represents a course a student is enrolled in, with attributes such as course ID, name, credits, and grade.

### Usage

To run the program, execute `app.py`:

```bash
python app.py
```

The program will display a menu of options for managing student records. Follow the prompts to perform desired actions like adding, updating, or deleting students, adding course reports, and generating student reports.

### Class Overview

- **Administrator**: Manages student records. Supports functionalities to add, update, delete students, add course reports, and generate reports.
  
- **Student**: Represents a student inheriting from `Person`. Includes methods to manage enrolled courses, calculate GPA, and view courses.

- **Course**: Represents a course that a student is enrolled in. Includes methods to set and get course grades.

### Getting Started

1. Run the program:
   ```bash
   python app.py
   ```

Follow the on-screen prompts to manage student records efficiently.

### Contributor

All contributors of this program are students of SDU University:
- Miqdad Yasser Al-Fafa (220317052)
- Zakky Abdilla (220317051)
- Muhammad Kahfi Aulia (220317050)



Feel free to use, modify, or distribute this code for educational or personal purposes.
