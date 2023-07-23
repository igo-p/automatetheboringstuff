import re


def detect_date(date_str):
    date_detection = re.compile(r'''
                            (0[1-9]|1[0-9]|2[0-9]|3[0-1])   # Day
                            /                               # Separator
                            (0[1-9]|1[0-2])                 # Month
                            /                               # Separator
                            (1[0-9]{1,3}|2[0-9]{1,3}        # Year
    )''',re.VERBOSE)

    mo = re.match(date_detection,date_str)

    try:
        date_tuple = mo.groups()
        return isValidDate(date_tuple)
    except:
        return("This is not a valid date")

def isValidDate(date_tuple):
    day_str,month_str,year_str = date_tuple
    day = int(day_str)
    year = int(year_str)

    if (month_str == '04' or month_str == '06' or month_str == '09' or month_str == '11') and day > 30: # Months with 30 days
        return False
    elif (month_str == '02' and year % 4 == 0 and year % 400 == 0 and year % 100 != 0) and day > 29:    # Leap year February
        return False
    elif month_str == '02' and day > 28:                                                                # Normal Februaries
        return False
    else:
        return True

print("Hey to date checker.\n")        
date_to_check = input("Write your alleged date here:\n")
print(detect_date(date_to_check))
