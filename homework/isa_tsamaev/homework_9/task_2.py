temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

hot_temperatures = list(filter(lambda temp: temp > 28, temperatures))
max_temp = max(hot_temperatures)
min_temp = min(hot_temperatures)
avg_temp = sum(hot_temperatures) / len(hot_temperatures)

print(f'Max: {max_temp}\nMin: {min_temp}\nAvg: {round(avg_temp)}')
