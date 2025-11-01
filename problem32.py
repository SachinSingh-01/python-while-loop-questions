# Print numbers from 1 to 10 but skip 5 (don’t print 5).
i=1
while i<=10:
    if(i==5):
        i+=1  
        continue
    print(i)
    i+=1