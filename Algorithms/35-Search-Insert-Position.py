def searchInsert(nums, target):
    position = -1
        
    for i in range(len(nums)):
        if (target > nums[i]):
            if ((i + 1) == len(nums) or target <= nums[i + 1]):
                position = i + 1
                break
        elif (target <= nums[i]):
            position = i
            break
                
    return position

def main():
    #Test Cases
    l1 = [1, 3, 5, 6]
    target1 = 5

    print("Input: [1, 3, 5, 6], 5")
    print("Output:", searchInsert(l1, target1)) #Should return 2

    l2 = [1, 3, 5, 6]
    target2 = 2

    print("Input: [1, 3, 5, 6], 2")
    print("Output:", searchInsert(l2, target2)) #Should return 1

    l3 = [1, 3, 5, 6]
    target3 = 7

    print("Input: [1, 3, 5, 6], 7")
    print("Output", searchInsert(l3, target3)) #Should return 4

    l4 = [1, 3, 5, 6]
    target4 = 0

    print("Input: [1, 3, 5, 6], 0")
    print("Output", searchInsert(l4, target4))

if __name__ == "__main__":
    main()
