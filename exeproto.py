import calendar

def print_month_calendar(year, month):
    # Get the calendar for the specified year and month
    cal = calendar.Calendar()
    month_days = cal.itermonthdays2(year, month)

    # Print the month and year
    month_name = calendar.month_name[month]
    print(f"{month_name} {year}")

    # Print the header
    print("Mon Tue Wed Thu Fri Sat Sun")

    # Iterate over the days in the month
    for day, weekday in month_days:
        if day == 0:
            # Print a blank space for days outside the current month
            print("    ", end="")
        else:
            # Print the day number
            print(f"{day:2d}  ", end="")

        # Start a new line for Sundays
        if weekday == 6:
            print()

    print()

# Get the current year and month
current_year = 2023
current_month = 5

# Print the calendar for the current month
print_month_calendar(current_year, current_month)
