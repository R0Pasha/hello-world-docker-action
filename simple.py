import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
numbers = [x,y]
numbers.sort (reverse=True)
while numbers[0]>=numbers[1]:
        if numbers[0]%2!=0:
            print (numbers[0])
        numbers[0]=numbers[0]-1