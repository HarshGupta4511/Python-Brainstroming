def find_max(lst):
        largest = lst[0]
        for i in lst:
            if i > largest:
                largest = i
        return largest        
            

print(find_max([3, 7, 2, 9, 5]))