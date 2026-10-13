class Solution:
    def encode(self, strs: List[str]) -> str:
        enc = ""
        for word in strs:
            enc += f"{len(word)}${word}"
        return enc
    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
            delim = s.find("$", i)
            string_len = int(s[i:delim])
            lst.append(s[delim+1:delim+1+string_len])
            i = delim+1+string_len
        return lst