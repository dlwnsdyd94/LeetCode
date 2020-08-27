'''4Sum 문제
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

'''Solution
2개를 묶어서 Dict로 저장한 다음, 2sum으로 푼다.
'''

class Solution:
    def fourSum(self, nums, target):
        l = len(nums)
        d = {}
        res = set()
        nums.sort()
        for i in range(l - 1):
            for j in range(i + 1, l):
                key = nums[i] + nums[j]
                if key not in d:
                    d[key] = [(i, j)]
                else:
                    d[key].append((i, j))
        for i in range(2, l - 1):
            for j in range(i + 1, l):
                pre = target - nums[i] - nums[j]
                if pre in d.keys():
                    for v in d[pre]:
                        if v[1] < i:
                            res.add((nums[v[0]], nums[v[1]], nums[i], nums[j]))
        return [list(i) for i in res]

''' 내 풀이 방식
combinations로 모든 조합을 구한다음,
조합 중 합이 target과 같은 걸 구한다.
중복된 조합을 set를 이용하여 제거,
리스트 내의 숫자 순서는 다르지만 같은 조합도 sort를 시킨다음 set를 이용하여 제거

from itertools import permutations
from collections import defaultdict
import time

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        temp = []
        for num4 in list(combinations(nums,4)):
            if sum(num4) == target:
                temp.append(num4)
        temp = set(temp)
        answer = []
        for a in temp:
            answer.append(tuple(sorted(a)))
        answer = set(answer)
        return answer
'''
