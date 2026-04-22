class Solution:

    def encode(self, strs: List[str]) -> str:
        payload = ""
        for s in strs:
            payload += str(len(s)) #give the len of the str
            payload += '-' #delimiter
            payload += s
        return payload

    def decode(self, s: str) -> List[str]:
        result = []
        cur = 0
        while cur < len(s):
            length = ""
            while s[cur] != "-":
                length += s[cur]
                cur+=1
            cur+=1
            string = ""
            for i in range(int(length)):
                string+=s[cur]
                cur+=1
            result.append(string)
        return result



