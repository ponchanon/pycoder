class Solution:
    """
    Given a string `s` and an integer `k`, this function returns the minimum number of characters 
    that need to be taken from the string such that each character 'a', 'b', and 'c' appears at least `k` times.
    If it is not possible to achieve this, the function returns -1.

    Args:
        s (str): The input string consisting of characters 'a', 'b', and 'c'.
        k (int): The minimum number of times each character 'a', 'b', and 'c' must appear.

    Returns:
        int: The minimum number of characters to be taken from the string to satisfy the condition, 
             or -1 if it is not possible.
    """
    def takeCharacters(self, s: str, k: int) -> int:
        count = [0, 0, 0]
        for c in s:
            count [ord (c) - ord("a")] += 1
        if min (count) < k:
            return -1
            # Sliding Window
        res = float("inf")
        l = 0
        for r in range(len(s)):
            count [ord (s[r]) - ord("a")] -= 1
            while min(count) < k:
                count [ord(s [l]) - ord("a")] += 1
                l += 1
            res = min(res, len(s) - (r - l + 1))
        return res