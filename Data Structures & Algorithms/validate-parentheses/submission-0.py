class Solution:
    def isValid(self, s: str) -> bool:
        pairs = ["()", "[]", "{}"]

        while True:
            found = False

            for pair in pairs:
                if pair in s:
                    s = s.replace(pair, "")
                    found = True
                
            if not found:
                break
        
        return s == ""