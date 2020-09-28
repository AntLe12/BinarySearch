import random

# List of random numbers
numList = [int(random.randint(0, 20) * 2), int(random.randint(0, 20) * 2), int(random.randint(0, 20) * 2),
           int(random.randint(0, 20) * 2), int(random.randint(0, 20) * 2), int(random.randint(0, 20) * 2),
           int(random.randint(0, 20) * 2), int(random.randint(0, 20) * 2), int(random.randint(0, 20) * 2)]

# Sort the list from ascending order
numList.sort()

# Prints the list
print(numList)

# Computer generated number
computerNum = random.randint(0, 20 * 2)

print("Computer number: " + (str(computerNum)))
mid = (len(numList)-1) / 2
print("Halfway number: " + (str(numList[int(mid)])))

# Automatically prints the number and index if it is middle
if computerNum == numList[int(mid)]:
    print("Matching computer number: " + (str(numList[int(mid)])))
    print("Index of matching computer number: " + (str(int(mid))))

# Checks for if the number is greater than the halfway point
elif computerNum > numList[int(mid)]:
    # Upper half of the list is searched
    for i in range(int(mid), len(numList)):
        # Checks if the each element in the half is the computer number
        if computerNum == numList[i]:
            print("Matching computer number: " + (str(numList[i])))
            print("Index of matching computer number: " + (str(i)))
        else:
            continue

# When the number is less than the halfway point
else:
    # Lower half of the list is searched
    for i in range(0, int(mid)+1):
        # Checks if each element in the half is the computer number
        if computerNum == numList[i]:
            print("Matching computer number: " + (str(numList[i])))
            print("Index of matching computer number: " + (str(i)))
        else:
            continue
