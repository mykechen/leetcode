class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        # # SOL 1: Slow w/ sorting + fixed sliding window
        # s1_sorted = sorted(s1)
        # s1_len = len(s1)

        # for right in range(len(s2) - len(s1) + 1):
        #     substr = s2[right:right+s1_len]
        #     substr_sorted = sorted(substr)

        #     if substr_sorted == s1_sorted:
        #         return True

        # return False
        
        # SOL 2: Optimized
        if len(s1) > len(s2):
            return False

        s1_count = defaultdict(int)
        s2_count = defaultdict(int)

        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1

        if s1_count == s2_count:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            s2_count[s2[right]] += 1
            s2_count[s2[left]] -= 1

            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]

            left += 1

            if s1_count == s2_count:
                return True

        return False