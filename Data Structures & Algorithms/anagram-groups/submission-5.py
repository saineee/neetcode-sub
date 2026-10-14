class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for word in strs:
            sortedword = "".join(sorted(word))
            output[sortedword].append(word)
        return [word for word in output.values()]