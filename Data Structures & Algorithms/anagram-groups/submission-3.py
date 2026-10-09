class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for word in strs:
            sorted_key = "".join(sorted(word))
            words[sorted_key].append(word)
        return [word for word in words.values()]