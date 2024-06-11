# User function Template for python3
class Solution:
    def hasArrayTwoCandidates(self, arr, n, x):
        # Create an empty set to store the elements we have seen so far
        seen = set()
        # Traverse the array
        for num in arr:
            # Calculate the complement of the current number
            complement = x - num
            # If the complement is in the set, we found a pair
            if complement in seen:
                return True
            # Add the current number to the set
            seen.add(num)
        # If no pair is found, return False
        return False

# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends
