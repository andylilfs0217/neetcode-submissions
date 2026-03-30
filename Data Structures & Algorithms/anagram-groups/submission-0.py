class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for string in strs:
            key = str(sorted(string))
            str_dict[key].append(string)
        result = list()
        for value in str_dict.values():
            result.append(value)
        return result
