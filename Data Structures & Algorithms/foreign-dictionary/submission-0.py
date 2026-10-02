from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        visit = {}
        result = []

        def dfs(char):
            if char in visit:
                return visit[char]

            visit[char] = True

            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True

            visit[char] = False
            result.append(char)
            return False

        for char in adj:
            if dfs(char):
                return ""

        result.reverse()
        return "".join(result)