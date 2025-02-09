#break
# continue
# pass

n=int(input('enter any no. '))
i=1
while i<=n:
    if i==6:
        i+=1
        continue  # if we use break to loop ruk jayega. #if we use pass so bo pass ho jayega or loop me kuchh nhi hoga
    print(i)
    i=i+1
print('stop')