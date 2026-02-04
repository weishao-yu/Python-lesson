results = []
def flatten(lst):
    for item in lst:
        if type(item) == type([]):
            flatten(item)
        else:
            results.append(item)
    return results
print(flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]))
# returns [1, 2, 0, 1, 3, 1, 3, 3, 4, 1, 2]