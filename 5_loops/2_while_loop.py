import datetime

start_date = datetime.datetime(2023, 7, 1)

end_date = datetime.datetime(2023, 9, 1)

date_list = []

while start_date < end_date:
    print(start_date)
    date_list.append(start_date)
    start_date += datetime.timedelta(days=1)


print("\nwhile loop complete")
print(date_list)
