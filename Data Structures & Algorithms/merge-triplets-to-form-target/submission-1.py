class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        combination = [0, 0, 0]
        x, y, z = target
        for triplet in triplets:
            if triplet[0] > x or triplet[1] > y or triplet[2] > z:
                continue
            combination[0] = max(combination[0], triplet[0])
            combination[1] = max(combination[1], triplet[1])
            combination[2] = max(combination[2], triplet[2])
            if combination == target:
                return True
        return False