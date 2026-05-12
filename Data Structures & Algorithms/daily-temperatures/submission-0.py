class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            for t in range(i + 1, len(temperatures)):
                if temperatures[t] > temp:
                    res[i] = (t - i)
                    break
        return res