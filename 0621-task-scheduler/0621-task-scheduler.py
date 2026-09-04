class Solution(object):
    def leastInterval(self, tasks, n):

        count = {}

        for task in tasks:
            count[task] = count.get(task, 0) + 1

        max_freq = max(count.values())

        max_count = 0

        for freq in count.values():
            if freq == max_freq:
                max_count += 1

        part = max_freq - 1

        empty_slots = part * (n + 1)

        empty_slots += max_count

        return max(len(tasks), empty_slots)