#!/usr/local/bin/python3
date_entry = input('Enter a date in YYYY-MM-DD format: ')
year, month, day = map(int, date_entry.split('-'))
date1 = (year, month, day)

print(date1);

years = (year - 2018)*365;
months = (month - 6)*30;
days = day - 30;
total = years + months + days;

print("Days between June 30, 2018 and ", date1, ": ", total);