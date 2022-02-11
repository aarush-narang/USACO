"""
ID: Aarush Narang [anarang2]
LANG: PYTHON3
TASK: friday
"""

# output will be in the format: "1 2 3 4 5 6 7" where 1 is Saturday and 7 is pos_in_arr (sat, sun, mon, tue, wed, thu, fri)
# time period: January 1, 1900 to December 31, 1900 + N - 1 for a given number of years n.
def getDaysInEachMonth(year):
    if (year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        days_in_each_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return days_in_each_month

def main():
    with open('friday.in', 'r') as f:
        n = int(f.read())

    days = [0, 0, 0, 0, 0, 0, 0] # [sat, sun, mon, tue, wed, thu, fri]

    pos_in_arr = 0 # jan 13 1900 is saturday
    days[pos_in_arr] += 1

    for year in range(1900, 1900 + n):
        days_in_each_month = getDaysInEachMonth(year) # get the number of days in each month for this year
        for month in range(1, 13):
            if year == 1900 and month == 1: continue # skip the first month of the year because it was already calculated

            """
                add the number of days in the previous month (-2 because months start at 1 not 0) 
                to the current position in the array and take the modulo of 7 to get the new position in the array.
                Using that new position, add 1 to the corresponding day in the array and assign that new position to the variable pos_in_arr.
            """
            days[(pos_in_arr + days_in_each_month[month-2]) % 7] += 1 
            pos_in_arr = (pos_in_arr + days_in_each_month[month-2]) % 7

    with open('friday.out', 'w') as f:
        f.write(' '.join(str(day) for day in days) + '\n')


if __name__ == '__main__':
    main()
