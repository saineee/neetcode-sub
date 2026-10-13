class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedstr = ""
        for word in strs:
            encodedstr += f"{len(word)}%{word}"
        return encodedstr
            
    def decode(self, s: str) -> List[str]:
        list = []
        i = 0
        while i < len(s):
            coordinate = s.find('%', i)
            length = int(s[i:coordinate])
            list.append(s[coordinate+1:coordinate+1+length])
            i = length+1+coordinate
        return list
