converter = input("input seconds:  ")
converter = int(converter)
hour = converter // 3600
minute = (converter // 3600) % 60
second = ((converter // 3600) % 60) % 60

print('hour is', hour, 'minute is', minute, 'second is', second)
