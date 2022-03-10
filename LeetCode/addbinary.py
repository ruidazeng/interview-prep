# managing the carried bit throughout the solution
# also uses ord to simplify if-statements
# totaling the sums at each bit to avoid more scenarios given unequal string sizes

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i, j, carry = len(a)-1, len(b)-1, 0
        while i >= 0 or j >= 0:
            total = carry;
            if i >= 0:
                total += ord(a[i]) - ord('0')
            if j >= 0 :
                total += ord(b[j]) - ord('0')
            i, j = i-1, j-1
            
            # reset carry
            if total > 1:
                carry = 1
            else:
                carry = 0
            
            res = str(total % 2) + res

        # final bit
        if carry != 0:
            res = str(carry) + res
            
        return res