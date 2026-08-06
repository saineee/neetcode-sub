class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return_list = defaultdict(list)
        for word in strs:
                return_list[tuple((sorted(word)))].append(word)
        return list(return_list.values())
