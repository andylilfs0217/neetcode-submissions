from collections import defaultdict, Counter

def counter_to_key(counter: dict) -> list:
    return frozenset(counter.items())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_to_list_dict = defaultdict(list)
        for string in strs:
            char_counter = Counter(string)
            key = counter_to_key(char_counter)
            counter_to_list_dict[key].append(string)
        ans = []
        for strings in counter_to_list_dict.values():
            ans.append(strings)
        return ans
