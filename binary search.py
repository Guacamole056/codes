arr = [10, 20, 30, 40, 50, 60, 70, 80]


def binarysearch(searcharray, searchvalue):
    lower = 0
    upper = len(arr) - 1
    while upper >= lower:
        mid = int((lower + upper) / 2)
        if searchvalue == searcharray[mid]:
            return mid
        elif searchvalue > searcharray[mid]:
            lower = mid + 1
        else:
            upper = mid - 1
    return -1


target = int(input("Enter Value to be found: "))

result = binarysearch(arr, target)

if result != - 1:
    print("Value found at index:", result)
else:
    print(result)