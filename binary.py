def search(nums: list, target: int) -> int:
    output_index = len(nums)//2
    index = 0
    while(len(nums) > 0):
        if(len(nums) == 1):
            if nums[0]== target:
                return 0
            else:
                return -1
        else:
            index = len(nums)//2
            if(nums[index] > target):
                nums = nums[:index]
                output_index = output_index // 2
                print(index)
            if(nums[index] < target):
                nums = nums[index:]
                output_index += output_index // 2
                print(index)
            if(nums[index] == target):
                return output_index
            
                

nums = [-1,0,3,5,9,12]
target = 2


print(search(nums, target))
