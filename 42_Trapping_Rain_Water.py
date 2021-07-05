def trap(height):
    n = len(height)
    tallest = tallest_index = 0
    for i in range(n):
        if height[i] > tallest:
            tallest = height[i]
            tallest_index = i
    volume = n * tallest
    second_tallest = 0
    for i in range(tallest_index):
        if height[i] > second_tallest:
            second_tallest = height[i]
        print("i is "+str(i)+" and "+str(tallest-second_tallest))
        volume -= (tallest - second_tallest + height[i])
    second_tallest = 0
    for i in range(n-1,tallest_index,-1):
        if height[i] > second_tallest:
            second_tallest = height[i]
        print("i is "+str(i)+" and "+str(tallest-second_tallest))
        volume -= (tallest - second_tallest + height[i])
    return volume - tallest
        
# sample inputs:

#Expect 6
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

#Expect 9
print(trap([4,2,0,3,2,5]))


"""highs = []
    volume = 0
    tallest = 0
    tallest_index = 0 
    for i in range(len(height)):
        print("i is "+str(i))
        print(highs)
        print(volume)
        if not highs and height[i] == 0:
            continue
        elif not highs and height[i] != 0:
            highs.append([i,height[i]])
            tallest, tallest_index = height[i], i
        elif height[i] < highs[-1][1]:
            volume += highs[-1][1] - height[i]
        elif height[i] == highs[-1][1]:
            highs.append([i,height[i]])
        elif height[i] > tallest:
            tallest, tallest_index = height[i], i
            highs.append([i,height[i]])
        else:
            if i == tallest_index + 1:
                highs.append([i,height[i]])       
                continue 
            j = len(highs)
            while highs[j][1] < height[i] and j> tallest_index:
                j -= 1
            highs = highs[:j+1]
            highs.append([i,height[i]])
            volume += height[i] * (i-j)
    return volume"""