# Hash map with sorted string as key: anagrams share the same sorted form
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        hashmap = {}  # sorted string -> list of original strings

        for s in strs:
            sorted_s = "".join(sorted(s))  # use sorted form as the grouping key

            if sorted_s in hashmap:
                hashmap[sorted_s].append(s)
            else:
                hashmap[sorted_s] = [s]

        return hashmap.values()