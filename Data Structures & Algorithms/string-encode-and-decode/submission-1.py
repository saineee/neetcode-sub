class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"
        return encoded
    def decode(self, s: str) -> List[str]:
        list = []
        i = 0
        while i < len(s):
            coord = s.find("#", i)
            str_length = int(s[i:coord])
            list.append(s[coord+1:str_length+coord+1])
            i = str_length+coord+1
        return list