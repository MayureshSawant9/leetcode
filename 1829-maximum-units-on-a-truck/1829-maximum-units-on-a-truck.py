class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x : x[1], reverse=True)
        max_units = 0

        for no, unit in boxTypes:
            if truckSize <= no:
                max_units += truckSize * unit
                return max_units

            max_units += no * unit
            truckSize -= no

        return max_units
