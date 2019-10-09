import collections
def groupAnagrams(strs):
	ans = collections.defaultdict(list)
	for s in strs:
		ans[tuple(sorted(s))].append(s)
	return list(ans.values())

strs = ["are", "bat", "ear", "code", "tab", "era"]
print(groupAnagrams(strs))
