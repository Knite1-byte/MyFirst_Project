def  minimal(l):
    min_number =  l[0]
    for el in l:
        if el < min_number:
            min_number = el

    return min_number
            

nums1 = [5, 6, 7, 4, 8]
min1 = minimal(nums1)

nums2 = [5.4, 7.2, 2.1, 2.4, 9.6, 4.2]
min2 = minimal(nums2)

if min1 < min2:
    print(min1)
else:
    print(min2)