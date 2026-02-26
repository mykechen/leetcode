# BFS shortest path: find min transformations from beginWord to endWord, changing 1 letter at a time
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not beginWord or not endWord:
            return 0

        L = len(beginWord)

        # precompute wildcard patterns -> matching words (e.g. "h*t" -> ["hot","hit"])
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i]+"*"+word[i+1:]].append(word)

        q = deque([(beginWord, 1)])  # (current word, transformation count)
        visited = set()
        visited.add(beginWord)
        while q:
            cur_word, level = q.popleft()

            # try all single-character wildcard patterns for current word
            for i in range(L):
                intermediate_word = cur_word[:i] + "*" + cur_word[i+1:]

                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        q.append([word, level + 1])
                        visited.add(word)

        return 0  # no transformation sequence found