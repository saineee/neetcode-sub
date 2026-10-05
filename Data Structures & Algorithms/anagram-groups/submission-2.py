class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for word in strs:
            sortWord = "".join(sorted(word))
            words[sortWord].append(word)
        return list(words.values())