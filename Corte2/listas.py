my_long_list = [0] * 100 # a long list of zeros
print(my_long_list)

day = [""] * 24
print(day)

timetable = day * 7
print(timetable)

timetable = [[""] * 24 for day in range(7)]
print(timetable)
     
