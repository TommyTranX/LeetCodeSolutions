class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        diff = len(a) - len(b)
        if diff > 0:
            b = "0"*diff + b
        if diff < 0:
            a = "0"*-diff + a
        carry = 0
        l = len(a) - 1
        res = ''
        
        while l >= 0:
            s = int(a[l]) + int(b[l]) + carry
            if s == 2:
                carry = 1
                res = '0' + res
            elif s == 3:
                carry = 1
                res = '1' + res
            else:
                res = str(s) + res
                carry = 0
            l -= 1
        if carry:
            res = str(carry) + res
        return res