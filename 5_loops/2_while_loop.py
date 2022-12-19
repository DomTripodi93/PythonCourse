import datetime

list_to_loop = [1, 4, 5, 2]
index = 0

while index < len(list_to_loop) - 1:
    print(list_to_loop[index])
    index += 1


start_date = datetime.datetime(2023, 7, 1)
end_date = datetime.datetime(2023, 7, 15)

while start_date <= end_date:
    print(start_date)
    start_date += datetime.timedelta(days=1)
