class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       freq_nums = Counter(nums) # is a mapping of items in nums and how many there are

       return (sorted(freq_nums, key=freq_nums.get, reverse=True))[:k] # sorts the frequency based on most -> least frequency of a num and then returns the first :k of that list