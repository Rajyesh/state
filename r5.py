lst1 = [2, 3, 8, 6, 7, 5, 8, 9]
n1 = 5  
lst1[:n1] = lst1[:n1][::-1]
print(lst1) 