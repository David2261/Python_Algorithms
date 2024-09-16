"""
Дан отсортированный по неубыванию список целых чисел a , индекс элемента index  и целое число k .
Необходимо вернуть в любом порядке k  чисел из списка, которые являются ближайшими по значению к элементу a[index]. 

Ограничения:
- Размер списка 1 <= N <= 10^6 ;
- Элементы списка: -10^9 <= a[i] <= 10^9 ;
- Число 0 <= k <= N ;
- Индекс элемента 0 <= index < N .
 

find_k_closest(a=[2, 3, 5, 7, 11], index=3, k=2) -> [5, 7]
find_k_closest(a=[4, 12, 15, 15, 24], index=1, k=3) -> [12, 15, 15]
find_k_closest(a=[2, 3, 5, 7, 11], index=2, k=2) -> [3, 5] или [5, 7]

[-999 2 3 10], index 2, k = 3 -> [2, 3, 10]

[-20 0 2 3 10 11 ], k = 5 -> [3, 2, 0, 10, 11]
         ^
"""

def find_k_closest(a: list[int], index: int, k: int) -> list:
    out = []
    left, right = index, index
    for i in range(k):
        if i == k:
            out.append(i)
        elif a[index] - a[left] <= a[right] - a[index]:
            out.append(a[left])
            left -= 1
        elif a[index] - a[left] > a[right] - a[index]:
            out.append(a[right])
            right += 1
        
        if left < 0:
            break
        elif len(a) >= right:
            break
    if left < 0:
        for n in range(k - i):
            out.append(a[right+n])
    elif len(a) >= right:
        for m in range(k - i):
            out.append(a[left-m])

    return out



    