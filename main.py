import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2024, 12, 12)
time_difference = next_birthday - today
if next_birthday == today:
  print(bday_messages.random_message)
else:
  print(f'My next birthday is {time_difference} away.')