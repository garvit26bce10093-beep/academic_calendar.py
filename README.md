# VIT Bhopal Academic Calendar System

## Project Overview

The **VIT Bhopal Academic Calendar System** is a Python-based console application designed to manage and organize academic events in a simple and structured way.

The system allows users to maintain important academic calendar information such as classes, holidays, examinations, assignments, result declarations, registrations, and college events.

The project uses **Object-Oriented Programming (OOP)** concepts and stores calendar information in a text file so that the data can be retained between program executions.

## Problem Statement

Students need to keep track of multiple academic activities such as class commencement dates, examinations, assignments, holidays, result declarations, registration dates, and college events.

Managing these dates manually can make it difficult to search, update, and maintain calendar information.

This project provides a simple command-line solution for storing, viewing, searching, adding, updating, and deleting academic calendar events.

## Objectives

- Provide a simple academic calendar management system.
- Store academic events in an organized format.
- Allow users to search events by date.
- Allow users to add, update, and delete events.
- Automatically determine the day of the week for each date.
- Maintain data using a text file.
- Apply Object-Oriented Programming concepts in Python.
- Provide input validation and basic error handling.

## Features

### 1. View Academic Calendar
Users can view events for a particular month or view all events.

### 2. Search Event by Date
Users can enter a date and find all events scheduled for that date.

### 3. Add Event
Users can add a new academic event by providing:
- Date
- Event type
- Event name
- Description

### 4. Update Event
Existing events can be modified, including their:
- Date
- Event type
- Name
- Description

### 5. Delete Event
Users can select an event and delete it after confirmation.

### 6. Display All Events
The system can display complete details of all stored events.

### 7. Automatic Day Calculation
The day of the week is automatically calculated from the entered date using Python's `datetime` module.

### 8. File-Based Data Storage
Calendar events are stored in `academic_calendar.txt`.

## Event Types

The application currently supports the following event types:

- Class
- Holiday
- Mid-Term Exam
- End-Term Exam
- Assignment
- Result Declaration
- Registration
- College Event

## Technologies Used

- **Programming Language:** Python 3
- **Concepts:** Object-Oriented Programming, Classes and Objects, Methods, Lists, File Handling, Exception Handling
- **Standard Library:** `datetime`
- **Storage:** Plain text file (`academic_calendar.txt`)
- **Version Control:** Git and GitHub

## Project Structure

```text
Academic-Calendar-VIT-Bhopal/
│
├── Main.py
├── README.md
├── statement.md
└── academic_calendar.txt
```

> `academic_calendar.txt` is created automatically when the program is run and the data file does not already exist.

## Classes Used

### Event

The `Event` class represents one academic calendar event.

It stores:

- Date
- Day
- Event type
- Event name
- Description

It also provides methods for changing the date, converting event information into a file line, calculating a sortable date value, and displaying event details.

### AcademicCalendar

The `AcademicCalendar` class manages the complete collection of events and file operations.

It handles:

- Loading data
- Saving data
- Adding events
- Updating events
- Deleting events
- Searching events
- Displaying events
- Validating dates
- Selecting event types

## How to Run

### 1. Install Python

Install **Python 3.x** on your computer.

Check whether Python is installed:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

### 2. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 3. Open the Project Directory

```bash
cd Academic-Calendar-VIT-Bhopal
```

### 4. Run the Program

```bash
python Main.py
```

## How to Use

After starting the program, the main menu is displayed:

```text
==========================================
   VIT BHOPAL ACADEMIC CALENDAR SYSTEM
==========================================
1. View Academic Calendar
2. Search Date
3. Add Event
4. Update Event
5. Delete Event
6. Display All Events
7. Exit
```

Enter the corresponding number to perform an operation.

### Date Format

Dates must be entered in:

```text
DD-MM-YYYY
```

Example:

```text
21-09-2026
```

The program validates the date and automatically calculates its day.

## Data Storage

The program uses a text file named:

```text
academic_calendar.txt
```

Each event is stored in the following format:

```text
date|day|event_type|event_name|description
```

Example:

```text
15-08-2026|Saturday|Holiday|Independence Day|College closed
```

The `|` character is used as a separator. User input containing `|` is automatically replaced with `-` to protect the file structure.

## Input Validation and Error Handling

The application includes basic validation such as:

- Invalid date detection
- Date format validation
- Event type selection validation
- Invalid menu choice handling
- Empty event-name prevention
- Empty description handling
- Handling a missing data file
- Handling non-numeric menu selections

## Testing

The following operations should be tested before submission:

| Test | Expected Result |
|---|---|
| Run program without `academic_calendar.txt` | Sample events are created |
| Enter an invalid date | Program asks for a valid date |
| View month | Events for selected month are displayed |
| Search an existing date | Matching event(s) are displayed |
| Search a date without events | No event message is displayed |
| Add an event | Event is saved to the file |
| Update an event | Updated information is saved |
| Delete an event | Selected event is removed |
| Enter invalid menu choice | Error message is displayed |
| Exit program | Program terminates normally |

## Current Scope

This is a **console-based academic calendar management system**. It focuses on basic event management and persistent file-based storage.

The current version does not include:

- Graphical User Interface (GUI)
- Web interface
- Database management system
- User login/authentication
- Notifications or reminders
- Cloud synchronization

These can be considered for future versions.

## Future Enhancements

Possible improvements include:

- GUI using Tkinter
- Web version using Flask or Django
- SQLite/MySQL database integration
- User authentication
- Calendar visualization
- Event reminders and notifications
- Import/export using CSV
- Advanced search and filtering
- Automated testing
- Separate modules for models, storage, validation, and user interface

## Academic Context

This project was developed as a **VITyarthi Build Your Own Project** for applying programming concepts to a practical problem.

The project demonstrates problem identification, software implementation, Object-Oriented Programming, file handling, validation, documentation, and version-control usage.

## Author

**Student:** Garvit Soni  
**Project:** VIT Bhopal Academic Calendar System

## License

This project is created for academic/educational purposes.
