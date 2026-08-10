# def remove_duplicate(lst):
#     l1 = []
#     for i in lst:
#         if i not in l1:
#             l1.append(i)

#     return l1

# print(remove_duplicate([1,2,3,4,5,7,2,3]))

# def count_ferq(lst):
#     count ={}
#     for i in lst:
#         count.update({i:lst.count(i)})

#     return count

# print(count_ferq([1,2,2,44,1,3]))


# def second_smallest(lst):
#     first = lst[0]
#     second = lst[0]  
#     for i in lst:
#         if i < first:
#             second = first
#             first = i                
#         elif i != first and i < second:
#             second = i

#     return second

# print(second_smallest([1,4,5,31,6,2]))

# def move_zero(lst):
#     l1 = []
#     count = 0
#     for i in lst:
#         if i == 0:
#             count = count +1
#         elif i != 0:
#             l1.append(i)
#     for j in range (0, count):
#         l1.append(0)
        

#     return l1

# print(move_zero([1,2,4,0,4,34,5,0,0]))

# def is_anagram(s1, s2):
#     l1 = list(s1)
#     l2 = list(s2)
#     if len(l1) == len(l2):
#         print("Size is equal")
#     for i in l1:            
#         if i in l2:
#             l2.remove(i)
#         else:
#             return "Not Anagram"     
#     return "Anagram Verifed"

# print(is_anagram("abc","acb"))

# def missing_num(lst):
#     n = lst[-1]
#     for i in range(1,n+1):
#         if i in lst:
#             print(f"{i} is found")
#         elif i not in lst:
#             print(f"{i} is missing")
                           
#     return "Hogaya na ladle"

# print(missing_num([1,2,3,5,6,7,9]))

# def rotate(lst):
#     n1 = lst[-1]
#     lst.remove(n1)
#     l2 = []
#     l2.append(n1)
#     for i in range(0,len(lst)):
#         k = lst[i]
#         l2.append(k)
#     return l2

# print(rotate([1,2,3,4,55,77,34,87]))

# def get_evens(lst):
#     l1 = []
#     for i in lst:
#         if i%2 == 0:
#             l1.append(i)
#     return l1

# # print(get_evens([1,2,3,4,5,6,7,8]))


# def is_sorted(lst):
#     ascending = True
#     descending = True
    
#     for i in range(len(lst) - 1):
#         if lst[i] > lst[i+1]:
#             ascending = False
#         if lst[i] < lst[i+1]:
#             descending = False
    
#     return ascending or descending

# print(is_sorted([1,2,3,4,5,6,7]))
l = [ 1,2,55,4,5]
print(l[-1])

    
