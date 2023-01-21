class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = {}
        for i in range(len(jewels)):
            if jewels[i] not in dict:
                dict[jewels[i]] = 0
        for i in range(len(stones)):
            if stones[i] in dict:
                dict[stones[i]] = dict[stones[i]] + 1
        return sum(dict.values())
