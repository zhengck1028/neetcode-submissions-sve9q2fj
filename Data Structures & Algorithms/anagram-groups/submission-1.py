class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = []
        for i, s in enumerate(strs):
            s_char_count = {}
            for c in s: s_char_count[c] = s_char_count.get(c, 0) + 1
            strs_dict.append(s_char_count)
        output = []
        processed = [False] * len(strs)
        for i in range(len(strs)):
            if processed[i]: continue
            group = [strs[i]]
            processed[i] = True
            for j in range(i + 1, len(strs)):
                if not processed[j] and strs_dict[i] == strs_dict[j]:
                    group.append(strs[j])
                    processed[j] = True
            output.append(group)
        return output
