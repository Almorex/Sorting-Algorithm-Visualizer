import time

def heapify(data, n, i, drawData, timetick):
    drawData(data, ['yellow' if x==i else 'red' for x in range(n)])
    time.sleep(timetick)
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and data[i] < data[left]:
        largest = left
    if right < n and data[largest] < data[right]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest, drawData, timetick)


def heap_sort(data, drawData, timetick):
    n = len(data)
    for i in range(n//2, -1, -1):
        heapify(data, n, i, drawData, timetick)

    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0, drawData, timetick)
        drawData(data, ['green' if x > i else 'yellow' if x==i else 'red' for x in range(n)])
        time.sleep(timetick)