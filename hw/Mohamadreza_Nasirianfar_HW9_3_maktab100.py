from datetime import datetime
# import jdatetime

datetime1_user = input('Please enter date and time: ')
datetime2_user = input('Please enter date and time: ')

datetime1 = datetime.strptime(datetime1_user, "%Y-%m-%d %H:%M:%S")
datetime2 = datetime.strptime(datetime2_user, "%Y-%m-%d %H:%M:%S")

time_difference = datetime2 - datetime1
time_difference_seconds = time_difference.total_seconds()
print(time_difference_seconds)

count_kabise = datetime1.year//4
print(count_kabise)

# shamsi_date_1 = jdatetime.date.fromgregorian(date=datetime1)
# print(shamsi_date_1)