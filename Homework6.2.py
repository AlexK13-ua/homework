        # 6.2 Конвертер із числа в дату
import string

sec_input = [0, 224930, 466289, 950400, 1209600, 1900800, 8639999, 22493, 7948799]
seconds_in_minute = 60
seconds_in_hour = 3600
seconds_in_day = 86400

for i in sec_input:

    days, remainder = divmod(i, seconds_in_day)
    hours, remainder = divmod(remainder, seconds_in_hour)
    minutes, seconds = divmod(remainder, seconds_in_minute)


    if 5 <= days % 100 <= 20:
            day_word = "дней"
    elif days % 10 == 1:
            day_word = "день"
    elif 2 <= days % 10 <= 4:
            day_word = "дня"
    else:
            day_word = "дней"

    time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    print(days, day_word, time_str)


# ######################################


# while True:
#
#         sec_input = input("Input amount of seconds (0 - 8639999): ")
#         if sec_input.isdigit():
#             sec_input = int(sec_input)
#             if 0 <= sec_input <= 8639999:
#
#                 seconds_in_minute = 60
#                 seconds_in_hour = 3600
#                 seconds_in_day = 86400
#
#                 days, remainder = divmod(sec_input, seconds_in_day)
#                 hours, remainder = divmod(remainder, seconds_in_hour)
#                 minutes, seconds = divmod(remainder, seconds_in_minute)
#
#                 if 11 <= days % 100 <= 14:
#                         day_word = "дней"
#                 elif days % 10 == 1:
#                          day_word = "день"
#                 elif 2 <= days % 10 <= 4:
#                         day_word = "дня"
#                 else:
#                         day_word = "дней"
#
#                 time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
#                 print(days, day_word, time_str)
#             else:
#                 print("Error. Amount is out of range. Please try again")
#         else:
#             print("Error. Positive numbers only. Please try again")