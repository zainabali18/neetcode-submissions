class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        result = []
        i=0
        while i < len(s):
            # Read digits until we hit #
            j=i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])

            # Read length chars
            result.append(s[j+1: j+1+length])

            # jump to start of next chunk
            i = j+1+length
        return result

