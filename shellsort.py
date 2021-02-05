import time

def shell_sort(data, drawData, timetick):
    n = len(data)
    interval = n//2
    while interval > 0:
        for i in range(interval, n):
            temp = data[i]
            j = i
            while j >= interval and data[j-interval] > temp:
                drawData(data, ['yellow' if x == j or x == j-interval else 'red' for x in range(n)])
                time.sleep(timetick)
                data[j] = data[j-interval]
                j -= interval

            data[j] = temp
        interval //= 2