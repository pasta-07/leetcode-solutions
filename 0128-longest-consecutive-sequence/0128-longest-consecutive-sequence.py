class Solution(object):
    def longestConsecutive(self, nums):
        # Convert to a set for O(1) lookups
        num_set = set(nums)
        longest = 0

        for n in num_set:
            # Only start building a sequence if 'n' is the absolute start of it
            if (n - 1) not in num_set:
                up = n
                down = 1
                
                # Keep checking for the next consecutive numbers moving 'up'
                while (up + 1) in num_set:
                    up += 1
                    down += 1 # 'down' acts as our length streak counter
                
                longest = max(longest, down)
                
        return longest

# --- Code execution outside the class block ---
A = [100, 4, 200, 1, 3, 2]

# 1. Create an instance of the Solution class
sol = Solution()

# 2. Call the method using the object instance and pass the array 'A'
print("length:", sol.longestConsecutive(A))
