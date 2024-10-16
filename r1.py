l1 = [9,8,2,1,7,3,6,4]
new = []
for num in l1:
    if num < 2:
        continue 
    for i in range(2, num):
        if num % i == 0:
            break  
    else:
        new.append(num)  
print(new)