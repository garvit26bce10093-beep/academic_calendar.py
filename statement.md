# Project Statement

## Project Title

**VIT Bhopal Academic Calendar System**

## 1. Problem Statement

Academic schedules contain many important dates, including class commencement, holidays, examinations, assignments, registration dates, result declarations, and college events.

Keeping track of these events manually can make it difficult to search for a particular date, update incorrect information, or maintain an organized record.

The proposed **VIT Bhopal Academic Calendar System** provides a simple Python-based solution for managing academic calendar events. The system allows users to view, search, add, update, and delete events while maintaining the information in a text file.

## 2. Project Objective

The main objective of this project is to develop a simple and practical academic calendar management system using Python and Object-Oriented Programming concepts.

The project aims to:

1. Store academic calendar events in a structured manner.
2. Allow users to view events by month or view all events.
3. Allow users to search for events using a date.
4. Allow users to add new academic events.
5. Allow users to update existing events.
6. Allow users to delete events.
7. Automatically determine the day of the week from a date.
8. Preserve event information using file-based storage.
9. Apply input validation and basic error handling.

## 3. Scope of the Project

The current project is a command-line application for managing academic calendar information.

### Included in Scope

- Academic event creation
- Academic event viewing
- Searching events by date
- Updating event information
- Deleting events
- Monthly calendar viewing
- Event categorization
- Automatic day calculation
- Text-file data storage
- Input validation
- Basic error handling

### Outside the Current Scope

The current implementation does not include:

- Web-based access
- Graphical user interface
- Database storage
- Student login or authentication
- Email/SMS notifications
- Automatic reminders
- Cloud-based synchronization
- Mobile application

These features may be added in future versions.

## 4. Target Users

The primary target users are:

- VIT Bhopal students
- Students who want to organize academic dates
- Academic project evaluators and instructors
- Users who need a simple personal academic event management tool

## 5. High-Level Features

### Academic Calendar Viewing

Users can view events for a selected month or display all calendar events.

### Date Search

Users can enter a date to find events scheduled on that date.

### Event Management

Users can:

- Add events
- Update events
- Delete events
- Display complete event details

### Event Categories

The system supports:

- Class
- Holiday
- Mid-Term Exam
- End-Term Exam
- Assignment
- Result Declaration
- Registration
- College Event

### Automatic Day Calculation

The system calculates the day of the week from the entered date using Python's `datetime` functionality.

### Persistent Storage

Events are saved to `academic_calendar.txt`, allowing information to remain available after the program is closed.

## 6. Functional Requirements

### FR1 — View Calendar
The system shall allow users to view academic events for a selected month or all months.

### FR2 — Search Event
The system shall allow users to search for events by entering a date.

### FR3 — Add Event
The system shall allow users to create a new event with a date, type, name, and description.

### FR4 — Update Event
The system shall allow users to modify an existing event.

### FR5 — Delete Event
The system shall allow users to delete an existing event after confirmation.

### FR6 — Display Events
The system shall display detailed information about stored academic events.

### FR7 — Validate Dates
The system shall reject invalid dates and request a valid `DD-MM-YYYY` date.

### FR8 — Store Data
The system shall save events to a text file and load them when the application starts.

## 7. Non-Functional Requirements

### Usability
The application should provide a simple menu-driven interface that can be operated using keyboard input.

### Reliability
The application should validate user input and handle missing data files without crashing.

### Maintainability
The implementation should use classes and separate methods for different operations so that features can be modified more easily.

### Resource Efficiency
The application uses Python's standard library and lightweight text-file storage, making it suitable for a small academic calendar dataset.

### Error Handling
The system handles invalid dates, invalid numeric choices, missing files, and invalid event selections through validation and exception handling.

## 8. Technical Approach

The project is implemented in Python using Object-Oriented Programming.

The main classes are:

- `Event` — represents an individual calendar event.
- `AcademicCalendar` — manages the collection of events and calendar operations.

The application uses:

- Python `datetime` for date processing.
- A Python list for maintaining events during execution.
- A text file for persistent storage.
- Methods for CRUD operations.
- Exception handling for invalid input and missing files.

## 9. Expected Outcome

The expected outcome is a working command-line application through which a user can maintain an organized academic calendar.

The system should allow a user to start the program, view existing academic events, search for a date, create new events, modify events, remove events, and save the resulting calendar data.

## 10. Current Implementation Note

The current implementation is intentionally a lightweight console application using two main classes and file-based storage.

The VITyarthi project guidelines also mention a recommended/minimum structure of **5–10 meaningful modules/classes/files** for coding projects. Therefore, if the course evaluator strictly checks that requirement, the project should be further modularized before final submission.

Possible modules for a future/refined structure include:

- `event.py`
- `calendar_manager.py`
- `storage.py`
- `validators.py`
- `menu.py`
- `main.py`
- `tests/`

This documentation describes the current implementation and does not claim that those additional modules already exist.

## 11. Future Enhancements

Future versions may include:

1. SQLite database support.
2. Graphical user interface.
3. Web-based calendar.
4. User authentication.
5. Notifications and reminders.
6. Calendar export to CSV or other formats.
7. Advanced search and filtering.
8. Automated unit tests.
9. Modular package structure.
10. Integration with official academic calendar data where appropriate.

## 12. Conclusion

The VIT Bhopal Academic Calendar System demonstrates how Python and Object-Oriented Programming can be applied to solve a practical academic information-management problem.

The project provides basic calendar CRUD functionality, date processing, validation, and persistent file storage while maintaining a simple command-line workflow.
