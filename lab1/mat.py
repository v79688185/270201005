#If I leave my house at 6:52 am and run 1 mile at an easy pace(8 minute per mile),then 3 miles at tempo(6 minute per mile)and 2 mile at easy pace again, what time do ı get home for breakfast?
begHour,begMinutes = "6:52".split(":")
easy = 8
tempo = 6
total_min = easy + tempo * 3 + easy * 2
lastMin = int(begMinutes) + total_min
lastHour = int(begHour) + lastMin // 60
lastMin = lastMin % 60
print(str(lastHour)+":"+str(lastMin))