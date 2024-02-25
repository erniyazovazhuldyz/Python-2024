from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("New Date (Subtracting 5 days):", new_date.strftime("%Y-%m-%d"))
#task1

from datetime import datetime, timedelta
current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", current_date.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))
#task2

from datetime import datetime
current_datetime = datetime.now()
datetime_without_microseconds = current_datetime.replace(microsecond=0)
print("Original Datetime:", current_datetime)
print("Datetime without Microseconds:", datetime_without_microseconds)
#task3

from datetime import datetime
date_str1 = "2022-01-01 12:00:00"
date_str2 = "2022-02-01 15:30:45"
date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")
date_difference = date2 - date1
difference_in_seconds = date_difference.total_seconds()
print(f"The difference between the two dates is {difference_in_seconds} seconds.")
#task4


