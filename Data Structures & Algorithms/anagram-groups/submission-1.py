class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for str in strs:
            sort = ''.join(sorted(str))

            result[sort].append(str)
        return list(result.values())



                