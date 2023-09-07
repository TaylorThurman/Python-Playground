"""
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


# My Solution
def longest_common_prefix(strs: list[str]) -> str:
    base = strs[0]
    prefix = 200

    for s in strs[1:]:
        curr = 0
        for i in range(len(s)):
            c = s[i]
            if i < len(base) and c == base[i]:
                curr += 1
            else:
                break
        if curr < prefix:
            prefix = curr

    return base[0:prefix]


# Better Solution
def longest_common_prefix_2(v: list[str]) -> str:
    ans = ""
    v = sorted(v)
    first = v[0]
    last = v[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans


print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
print(longest_common_prefix(["cir", "car"]))
print(longest_common_prefix(["a"]))

print(longest_common_prefix_2(["flower", "flow", "flight"]))
print(longest_common_prefix_2(["dog", "racecar", "car"]))
print(longest_common_prefix_2(["cir", "car"]))
print(longest_common_prefix_2(["a"]))
