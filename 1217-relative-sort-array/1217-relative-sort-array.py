class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        rank = {value : index for index, value in enumerate(arr2)}
        def sort_key(value):
            return (rank.get(value, len(arr2)), value)



        arr1.sort(key=sort_key)
        return arr1

