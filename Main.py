import datetime


def get_day(date_text):
    # returns day name like Monday, or None if the date is wrong
    try:
        d = datetime.datetime.strptime(date_text, "%d-%m-%Y")
        return d.strftime("%A")
    except ValueError:
        return None


class Event:
    def __init__(self, date, event_type, name, description):
        self.date = date
        self.day = get_day(date)
        self.event_type = event_type
        self.name = name
        self.description = description

    def set_date(self, new_date):
        # changing the date also changes the day
        self.date = new_date
        self.day = get_day(new_date)

    def date_value(self):
        # used for sorting events by date
        return datetime.datetime.strptime(self.date, "%d-%m-%Y")

    def to_line(self):
        # converts the event into one line for the text file
        return self.date + "|" + self.day + "|" + self.event_type + "|" + self.name + "|" + self.description

    def show(self, number):
        print("Event No    :", number)
        print("Date        :", self.date)
        print("Day         :", self.day)
        print("Event Type  :", self.event_type)
        print("Event Name  :", self.name)
        print("Description :", self.description)
        print("-" * 45)


class AcademicCalendar:
    def __init__(self, file_name):
        self.file_name = file_name
        self.events = []
        self.event_types = ["Class", "Holiday", "Mid-Term Exam", "End-Term Exam",
                            "Assignment", "Result Declaration", "Registration",
                            "College Event"]

    def add_default_events(self):
        # sample records used when the file does not exist
        self.events.append(Event("01-08-2026", "Registration", "Semester Registration", "Last date for course registration"))
        self.events.append(Event("03-08-2026", "Class", "Classes Begin", "First day of classes for the semester"))
        self.events.append(Event("15-08-2026", "Holiday", "Independence Day", "College closed"))
        self.events.append(Event("14-09-2026", "Assignment", "Assignment 1", "Submission of first assignment"))
        self.events.append(Event("21-09-2026", "Mid-Term Exam", "Mid-Term Exams Begin", "Mid-term exams for all courses"))
        self.events.append(Event("02-10-2026", "Holiday", "Gandhi Jayanti", "College closed"))
        self.events.append(Event("12-10-2026", "Result Declaration", "Mid-Term Result", "Mid-term marks will be uploaded"))
        self.events.append(Event("08-11-2026", "Holiday", "Diwali Break", "Festival holiday"))
        self.events.append(Event("20-11-2026", "College Event", "Annual Tech Fest", "Technical events and competitions"))
        self.events.append(Event("01-12-2026", "End-Term Exam", "End-Term Exams Begin", "End-term exams for all courses"))
        self.events.append(Event("25-12-2026", "Holiday", "Christmas", "College closed"))
        self.events.append(Event("05-01-2027", "Result Declaration", "End-Term Result", "Final result declaration"))

    def save_data(self):
        # write all events to the text file, one event per line
        file = open(self.file_name, "w")
        for e in self.events:
            file.write(e.to_line() + "\n")
        file.close()

    def load_data(self):
        try:
            file = open(self.file_name, "r")
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split("|")
                if len(parts) == 5 and get_day(parts[0]) is not None:
                    self.events.append(Event(parts[0], parts[2], parts[3], parts[4]))
            file.close()
            self.events.sort(key=Event.date_value)
            print("Loaded", len(self.events), "events from", self.file_name)
        except FileNotFoundError:
            print("File not found. Creating a new file with sample events.")
            self.add_default_events()
            self.events.sort(key=Event.date_value)
            self.save_data()

    def read_date(self, message):
        # keeps asking until the user enters a valid date
        while True:
            date = input(message).strip()
            if get_day(date) is not None:
                return date
            print("Invalid date! Please use DD-MM-YYYY format (example: 21-09-2026).")

    def clean(self, text):
        # the '|' sign is used in the file, so we remove it from user text
        return text.replace("|", "-").strip()

    def choose_type(self):
        print("\nEvent Types:")
        for i in range(len(self.event_types)):
            print(" ", i + 1, "-", self.event_types[i])
        while True:
            try:
                choice = int(input("Enter event type number: "))
                if 1 <= choice <= len(self.event_types):
                    return self.event_types[choice - 1]
                print("Please enter a number between 1 and", len(self.event_types))
            except ValueError:
                print("Invalid input! Please enter a number.")

    def find_by_date(self, date):
        # returns a list of positions of events that have this date
        found = []
        for i in range(len(self.events)):
            if self.events[i].date == date:
                found.append(i)
        return found

    def select_event(self):
        # asks for a date and returns the position of the chosen event (or -1)
        date = self.read_date("Enter the date of the event (DD-MM-YYYY): ")
        found = self.find_by_date(date)
        if len(found) == 0:
            print("No event found on", date)
            return -1
        if len(found) == 1:
            return found[0]
        print("\nMore than one event found on this date:")
        for i in range(len(found)):
            e = self.events[found[i]]
            print(" ", i + 1, "-", e.name, "(" + e.event_type + ")")
        while True:
            try:
                choice = int(input("Select event number: "))
                if 1 <= choice <= len(found):
                    return found[choice - 1]
                print("Wrong number, try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    def view_calendar(self):
        print("\n----- ACADEMIC CALENDAR -----")
        if len(self.events) == 0:
            print("No events in the calendar.")
            return
        print("Enter month number (1-12) to see one month, or 0 to see all.")
        try:
            month = int(input("Month: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            return
        if month < 0 or month > 12:
            print("Month must be between 0 and 12.")
            return

        print("\n{:<12} {:<11} {:<19} {}".format("Date", "Day", "Type", "Event"))
        print("-" * 65)
        count = 0
        for e in self.events:
            event_month = int(e.date.split("-")[1])
            if month == 0 or event_month == month:
                print("{:<12} {:<11} {:<19} {}".format(e.date, e.day, e.event_type, e.name))
                count = count + 1
        if count == 0:
            print("No events found for this month.")

    def search_event(self):
        print("\n----- SEARCH DATE -----")
        date = self.read_date("Enter date to search (DD-MM-YYYY): ")
        found = self.find_by_date(date)
        if len(found) == 0:
            print("No event found on", date, "(" + get_day(date) + ")")
        else:
            print("\n", len(found), "event(s) found on", date)
            print("-" * 45)
            for i in found:
                self.events[i].show(i + 1)

    def add_event(self):
        print("\n----- ADD EVENT -----")
        date = self.read_date("Enter date (DD-MM-YYYY): ")
        print("Day is", get_day(date))
        event_type = self.choose_type()
        name = self.clean(input("Enter event name: "))
        description = self.clean(input("Enter description: "))
        if name == "":
            print("Event name cannot be empty. Event not added.")
            return
        if description == "":
            description = "No description"

        self.events.append(Event(date, event_type, name, description))
        self.events.sort(key=Event.date_value)
        self.save_data()
        print("Event added and saved successfully!")

    def update_event(self):
        print("\n----- UPDATE EVENT -----")
        pos = self.select_event()
        if pos == -1:
            return
        e = self.events[pos]
        print("\nCurrent details:")
        e.show(pos + 1)
        print("Press Enter to keep the old value.")

        new_date = input("New date (DD-MM-YYYY) [" + e.date + "]: ").strip()
        if new_date != "":
            if get_day(new_date) is None:
                print("Invalid date! Update cancelled.")
                return
            e.set_date(new_date)

        change_type = input("Change event type? (y/n): ").lower()
        if change_type == "y":
            e.event_type = self.choose_type()

        new_name = self.clean(input("New event name [" + e.name + "]: "))
        if new_name != "":
            e.name = new_name

        new_desc = self.clean(input("New description [" + e.description + "]: "))
        if new_desc != "":
            e.description = new_desc

        self.events.sort(key=Event.date_value)
        self.save_data()
        print("Event updated successfully!")

    def delete_event(self):
        print("\n----- DELETE EVENT -----")
        pos = self.select_event()
        if pos == -1:
            return
        print("\nEvent to be deleted:")
        self.events[pos].show(pos + 1)
        confirm = input("Are you sure you want to delete this event? (y/n): ").lower()
        if confirm == "y":
            self.events.pop(pos)
            self.save_data()
            print("Event deleted successfully!")
        else:
            print("Delete cancelled.")

    def display_events(self):
        print("\n----- ALL EVENTS -----")
        if len(self.events) == 0:
            print("No events to display.")
            return
        for i in range(len(self.events)):
            self.events[i].show(i + 1)
        print("Total events:", len(self.events))


def show_menu():
    print("\n==========================================")
    print("   VIT BHOPAL ACADEMIC CALENDAR SYSTEM")
    print("==========================================")
    print("1. View Academic Calendar")
    print("2. Search Date")
    print("3. Add Event")
    print("4. Update Event")
    print("5. Delete Event")
    print("6. Display All Events")
    print("7. Exit")


def main():
    calendar = AcademicCalendar("academic_calendar.txt")
    calendar.load_data()

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            calendar.view_calendar()
        elif choice == "2":
            calendar.search_event()
        elif choice == "3":
            calendar.add_event()
        elif choice == "4":
            calendar.update_event()
        elif choice == "5":
            calendar.delete_event()
        elif choice == "6":
            calendar.display_events()
        elif choice == "7":
            print("Thank you for using the Academic Calendar System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 7.")


main()
