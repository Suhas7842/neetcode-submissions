class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 0, mountainArr.length() - 1
        while l < r:
            mid = (l + r) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l

        # Search increasing side
        l, r = 0, peak

        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)

            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1

        # Search decreasing side
        l, r = peak + 1, mountainArr.length() - 1

        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)

            if val == target:
                return mid
            elif val < target:
                r = mid - 1
            else:
                l = mid + 1
        return -1