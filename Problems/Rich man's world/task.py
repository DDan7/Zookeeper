year = 0
deposit = int(input())
while 50000 <= deposit <= 700000:
    deposit = int(deposit * 1.071)
    year += 1
print(year)