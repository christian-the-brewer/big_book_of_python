# https://inventwithpython.com/bigbookpython/project8.html
"""Calendar Maker by Christian Brewer"""

import datetime

# constants
DAYS = (
    'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'
)
MONTHS = (
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
)

print('---Calendar Maker---')

while True:
    print('Enter year: ')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    print('Please enter a year (2023)')
    continue

while True:
    print('Enter month (1-12): ')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numerical month (1-12):')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 - 12.')
    continue


def get_calendar(year, month):
    cal_text = ''  # string representation of calendar

    # print month and year at top of string
    cal_text += f"{' ' * 34}{MONTHS[month - 1]} {str(year)}\n"
    # add days of week
    for i in range(DAYS):
        cal_text += f"...{DAYS[i]}"
    cal_text += '..\n'

    # horizontal week separators
    week_separator = f"{'+---------' * 7}+\n"

    # blank rows
    blank_row = f"{'|          ' * 7}+\n"

    # get first date in month
    current_date = datetime.date(year, month, 1)

    # rollback currentdate to sunday
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True:
        cal_text += week_separator

        # row with day number labels
        day_number_row = ''
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += f"|{day_number_label}{' ' * 8}"
            current_date += datetime.timedelta(days=1)
        day_number_row += '|\n'

        # add day number row and 3 blank rows to cal text
        cal_text += day_number_row
        for i in range(3):
            cal_text += blank_row

        # check if month is finished
        if current_date.month != month:
            break

    # add horizontal line at bottom of calendar
    cal_text += week_separator
    return cal_text


cal_text = get_calendar(year, month)
print(cal_text)

# save to text file
calender_file_name = f'calendar_{year}_{month}'
with open(calender_file_name, 'w') as fileObj:
    fileObj.write(cal_text)

print(f'Saved to {calender_file_name}')
