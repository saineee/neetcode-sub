class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)

        for word in wordList + [beginWord]:
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i + 1:]
                adj[pat].append(word)

        seen = {beginWord}
        q = deque([beginWord])
        steps = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return steps

                for i in range(len(word)):
                    pat = word[:i] + "*" + word[i + 1:]

                    for nxt in adj[pat]:
                        if nxt not in seen:
                            seen.add(nxt)
                            q.append(nxt)

            steps += 1

        return 0