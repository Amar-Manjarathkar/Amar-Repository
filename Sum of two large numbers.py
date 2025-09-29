class Solution:
    def findSum(self, s1, s2):
        # ensure s1 is the longer string
        if len(s2) > len(s1):
            s1, s2 = s2, s1

        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        res = []  # build digits in reverse order

        while i >= 0 or j >= 0 or carry:
            d1 = ord(s1[i]) - 48 if i >= 0 else 0
            d2 = ord(s2[j]) - 48 if j >= 0 else 0

            s = d1 + d2 + carry
            res.append(chr((s % 10) + 48))
            carry = s // 10

            i -= 1
            j -= 1

        # reverse to normal order
        out = ''.join(res[::-1])

        # strip leading zeros, but return "0" if result is all zeros
        out = out.lstrip('0')
        return out if out != '' else '0'
