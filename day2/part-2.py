with open("input.txt", "r") as f:
    ip_text = f.read()


def check_safety_helper(nums):
    delta = 1 if nums[1] > nums[0] else -1
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        
        if delta == 1:
            if (diff < 1) or (diff > 3):
                return 0
        elif delta == -1:
            if (diff > -1) or (diff < -3):
                return 0

    return 1

def check_safety(line) -> int:
    """
    each line should be either increasing or decrasing
    the diff between two adjacent levels - between 1 and 3
    """
    numstrings = line.split()
    nums = [int(i.strip()) for i in numstrings]

    for i in range(len(nums)):
        nums_copy = nums.copy()
        nums_copy.pop(i)
        if check_safety_helper(nums_copy) == 1:
            return 1

    return 0

ip_lines = ip_text.splitlines()

safe_reports = 0

for line in ip_lines:
    safe_reports += check_safety(line)


print(safe_reports)
