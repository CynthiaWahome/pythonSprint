nums = [1,2,3,4,5,6,7,8,9,]
for num in nums:
    # print(nums)
    if num == 1:
        print(num,"st")
    elif num == 2:
        print(num,"nd")
    elif num == 3:
        print(num,"rd")
    elif num < 3 or num < 10:
        print(num,"th")
    else:
        print("That number is not in the list")