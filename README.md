# Student Result System

A simple Python console application that allows users to manage student results. The system can store student scores, calculate totals and averages, assign grades automatically, generate reports, and search for student records.

## Features

- Add student results
- Calculate total scores
- Calculate average scores
- Automatically assign grades
- Generate student reports
- Search for a student by name
- View all student records
- Menu-driven interface

## Subjects

The program records scores for four subjects:

- Mathematics
- English
- Science
- Programming

## Grade Scale

| Average Score | Grade |
|--------------|-------|
| 70 and above | A |
| 60–69 | B |
| 50–59 | C |
| 45–49 | D |
| Below 45 | F |

## Project Structure

| Function | Purpose |
|---------|---------|
| `calc_total(scores)` | Calculates the total score. |
| `calc_average(scores)` | Calculates the average score. |
| `calc_grade(avg)` | Determines the student's grade. |
| `generate_report(name, scores)` | Displays a student report. |
| `search_student(records, name)` | Searches for a student record. |
| `main()` | Runs the menu-driven application. |

## How to Run

### Prerequisites

- Python 3.x

### Steps

1. Clone the repository.

```bash
git clone https://github.com/yourusername/student-result-system.git
```

2. Navigate to the project folder.

```bash
cd student-result-system
```

3. Run the program.

```bash
python student_result_system.py
```

## Menu

When the program starts, you'll see the following menu:

```text
----- STUDENT RESULT SYSTEM -----
1. Add student results
2. Search for student
3. View all students
4. Exit
```

## Example Output

```text
STUDENT REPORT
Name: John
Scores: [80.0, 75.0, 68.0, 90.0]
Total score: 313.0
Average score: 78.25
Grade: A
```

## Future Improvements

- Save records to a CSV or JSON file
- Edit existing student records
- Delete student records
- Validate score input (0–100)
- Support additional subjects
- Display class statistics

## Python Concepts Used

- Functions
- Dictionaries
- Lists
- Loops
- Conditional statements
- User input
- Data processing
- Menu-driven programming

## License

This project is created for educational purposes.
