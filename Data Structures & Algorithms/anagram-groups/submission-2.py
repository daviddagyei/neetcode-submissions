class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = {}

        for word in strs:
            word_s = "".join(sorted(word))
            if word_s not in seen:
                seen[word_s] = [word]
            else:
                seen[word_s].append(word)

        for lst in seen.values():
            res.append(lst)

        return res

        