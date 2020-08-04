#  Posted from EduTools plugin
# put your python code here
hour1, minute1, second1 = int(input()), int(input()), int(input())
hour2, minute2, second2 = int(input()), int(input()), int(input())

first_point = (hour1 * 3600) + (minute1 * 60) + second1
second_point = (hour2 * 3600) + (minute2 * 60) + second2

delta = second_point - first_point
print(delta)