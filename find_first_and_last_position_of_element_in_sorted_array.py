from sys import stdin

def inp():
    return stdin.readline().rstrip()

def iinp():
    return int(inp())

def mp():
    return map(int, inp().split())

def liinp():
    return list(mp())


def solve(nums, target):
    """
    if len(nums)==1:
        if nums[0]==target:
            return [0, 0]
        else:
            return [-1, -1]
        
    elif len(nums)==0:
        return [-1, -1]

    start = 0
    end   = len(nums)-1
    while nums[start]!=nums[end] and start<=end:
        if nums[start]!=target and nums[end]!=target:
            start += 1
            end   -= 1
        if nums[start]==target and nums[end]!=target:
            end   -= 1
        if nums[start]!=target and nums[end]==target:
            start += 1
            
    return [start, end] if nums[start]==target and nums[end]==target else [-1, -1]
    """
    start, end = 0, len(nums)-1
    first_pos  = -1
    last_pos   = -1
    # Search the first position of target in the left side
    while start<=end:
        mid = (start+end)//2
        if nums[mid]==target:
            first_pos = mid
            end = mid-1
        elif target<nums[mid]:
            end = mid-1
        elif target>nums[mid]:
            start = mid+1
    # Search the last position of target in the right side;
    # initialize variables
    start, end = 0, len(nums)-1
    while start<=end:
        mid = (start+end)//2
        if nums[mid]==target:
            last_pos = mid
            start    = mid+1
        elif target<nums[mid]:
            end = mid-1
        elif target>nums[mid]:
            start = mid+1
    
    return [first_pos, last_pos]

if __name__ == "__main__":

    nums   = liinp()
    target = iinp()
    print(solve(nums, target))
