def multiplesOf3N5(max):
    count = 0
    for i in range (max):
        if i%3 == 0 or i%5 == 0:
            count = count+i
    return(count)
