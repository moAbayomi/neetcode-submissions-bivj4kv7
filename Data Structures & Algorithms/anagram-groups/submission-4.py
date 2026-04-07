from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)

        for str in strs:
            # array filled with zeros for a-z
            nin = [0 for i in range(26)]

            for char in str:
                nin[ord(char) - ord("a")] += 1
            
            hash[tuple(nin)].append(str)

        return list(hash.values())

                
            

        
       

