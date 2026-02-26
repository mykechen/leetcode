# Fixed sliding window + Counter: slide window of len(p) over s, compare frequency maps
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        res = []
        p_count = Counter(p)  # target frequency map
        window = Counter(s[:len(p)])  # initial window frequency map

        if window == p_count:
            res.append(0)

        # slide window: add new right char, remove old left char
        for i in range(len(p), len(s)):
            window[s[i]] += 1
            old = s[i-len(p)]
            window[old] -= 1
            if window[old] == 0:
                del window[old]  # clean up for accurate comparison

            if window == p_count:
                res.append(i - len(p) + 1)  # start index of this anagram

        return res