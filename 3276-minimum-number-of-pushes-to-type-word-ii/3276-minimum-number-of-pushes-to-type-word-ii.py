class Solution:
    def minimumPushes(self, word: str) -> int:
        count = 0
        pushes = 0
        mapping = dict()
        rank = dict()

        for c in word:
            if c in rank:
                rank[c] += 1
            else:
                rank[c] = 1

        for c in sorted(word, key=lambda x: rank[x], reverse=True):

            if c in mapping:
                pushes += mapping[c]

            else:
                mapping[c] = count // 8 + 1
                count += 1
                pushes += mapping[c]

        return pushes
