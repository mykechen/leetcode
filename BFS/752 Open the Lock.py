class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        
        # SOL1: SLOW
        # if '0000' in deadends:
        #     return -1
        
        # q = deque([('0000', 0)])
        # visited = set('0000')

        # while q:
        #     combo, step = q.popleft()

        #     if combo in deadends:
        #         continue
        #     if combo == target:
        #         return step

        #     for i in range(4):
        #         num = int(combo[i])
        #         for dx in [-1, 1]:
        #             num_new = (num + dx) % 10
        #             combo_new = combo[:i] + str(num_new) + combo[i+1:]
        #             if combo_new not in visited:
        #                 q.append((combo_new, step + 1))
        #                 visited.add(combo_new)

        # return -1

        # SOL2

        next_slot = {
            "0": "1",
            "1": "2",
            "2": "3",
            "3": "4",
            "4": "5",
            "5": "6",
            "6": "7",
            "7": "8",
            "8": "9",
            "9": "0",
        }

        prev_slot = {
            "0": "9",
            "1": "0",
            "2": "1",
            "3": "2",
            "4": "3",
            "5": "4",
            "6": "5",
            "7": "6",
            "8": "7",
            "9": "8",
        }

        visited = set(deadends)
        q = deque()
        turns = 0

        if "0000" in visited:
            return -1

        q.append("0000")
        visited.add("0000")

        while q:
            curr_level_nodes_count = len(q)
            for i in range(curr_level_nodes_count):
                curr_combo = q.popleft()

                if curr_combo == target:
                    return turns

                for wheel in range(4):
                    new_combo = list(curr_combo)
                    new_combo[wheel] = next_slot[new_combo[wheel]]
                    new_combo_str = "".join(new_combo)

                    if new_combo_str not in visited:
                        q.append(new_combo_str)
                        visited.add(new_combo_str)

                    new_combo = list(curr_combo)
                    new_combo[wheel] = prev_slot[new_combo[wheel]]
                    new_combo_str = "".join(new_combo)

                    if new_combo_str not in visited:
                        q.append(new_combo_str)
                        visited.add(new_combo_str)

            turns += 1

        return -1