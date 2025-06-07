def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    ite = 0
    if arr[high] < x:
        return -1
    while low <= high:
        ite += 1
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return ite, arr[mid]
    one = arr[mid]
    if one < x:
        return ite, arr[mid + 1]#якщо
    else:
        return ite, one

arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
x = 0.5

result = binary_search(arr, x)
if result != -1:
    print(f"\nQuantity of iterations {result[0]}, Element is {result[1]}")
else:
    print("\nElement is tooooooooooo big")
