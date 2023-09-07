"""
https://leetcode.com/problems/roman-to-integer/solutions/3651672/best-method-c-java-python-beginner-friendly/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


# My solution:
class Solution:

    def romanToInt(self, s: str) -> int:
        numeral_map = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        number = 0
        next = False
        for i in range(len(s)):
            if next:
                next = False
                continue

            c = s[i]
            try:
                if c == "M":
                    number += 1000
                elif c == "D":
                    number += 500
                elif c == "C":
                    if s[i + 1] == "D":
                        number += 400
                        next = True
                        continue
                    elif s[i + 1] == "M":
                        number += 900
                        next = True
                        continue
                    else:
                        number += 100
                elif c == "L":
                    number += 50
                elif c == "X":
                    if s[i + 1] == "L":
                        number += 40
                        next = True
                    elif s[i + 1] == "C":
                        number += 90
                        next = True
                    else:
                        number += 10
                elif c == "V":
                    number += 5
                elif c == "I":
                    if s[i + 1] == "V":
                        number += 4
                        next = True
                    elif s[i + 1] == "X":
                        number += 9
                        next = True
                    else:
                        number += 1
            except IndexError:
                number += numeral_map[c]

        return number


# Better Solution:
class Solution2:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0

        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i + 1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]

        return ans
