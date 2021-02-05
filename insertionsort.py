import time

def insertion_sort(data, drawData, timetick):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            drawData(data, ['yellow' if x == j else 'red' for x in range(len(data))])
            time.sleep(timetick)
            data[j+1] = data[j]
            j = j-1
        data[j+1] = key
