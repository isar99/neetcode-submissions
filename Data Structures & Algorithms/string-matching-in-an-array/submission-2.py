class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words_len = len(words)
        new_words = []
        for n in range(words_len):
            new_ls = words[:n]+words[n+1:]
            for j in new_ls:
                if words[n] == j or words[n] not in new_words:
                    pass
                if words[n] in j:
                    new_words.append(words[n])
        return list(set(new_words))

        