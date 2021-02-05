import time

def selection_sort(data, drawData, timetick):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if (data[j] < data[min_idx]):
                min_idx = j
            drawData(data, ['yellow' if x==j else 'green' if x<i else 'blue' if x==i else 'pink' if x==min_idx else 'red' for x in range(len(data))])
            time.sleep(timetick)
        data[i], data[min_idx] = data[min_idx], data[i]
