class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = defaultdict(list)
        for word in strs:
            srtword = "".join(sorted(word))
            sorted_words[srtword].append(word)
        return [word for word in sorted_words.values()]
