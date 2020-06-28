empty = frozenset()
frozen_set_int = frozenset({1, 2, 3})
fs_in_set = {frozenset(), frozenset({1,2})}
print(empty)
print(fs_in_set)
print(type(frozen_set_int))