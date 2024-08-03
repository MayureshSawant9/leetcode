class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        tar_c = Counter(target)
        arr_c = Counter(arr)

        return not len(tar_c - arr_c)
