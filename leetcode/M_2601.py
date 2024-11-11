class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n):
            for f in range(2,int(sqrt(n))+1):
                if n % f == 0:
                    return False
            return True
        
        primes = [0,0]
        for i in range(2,max(nums)):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(primes[i-1])
        
        prev_number = 0
        for num in nums:
            upper_bound = num - prev_number
            largest_prime = primes[upper_bound-1]
            if num - largest_prime <= prev_number:
                return False
            else:
                prev_number = num - largest_prime
        return True