'''Pancake Sorting 문제

Given an array of integers A, We need to sort the array performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 0 <= k < A.length.
Reverse the sub-array A[0...k].
For example, if A = [3,2,1,4] and we performed a pancake flip choosing k = 2, we reverse the sub-array [3,2,1], so A = [1,2,3,4] after the pancake flip at k = 2.

Return an array of the k-values of the pancake flips that should be performed in order to sort A. Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

'''

'''My Solution
풀이
이 문제는 Sorting하는 문제로서
하노이탑 푸는 것을 밴치마킹해서 풀었다.

맨 뒤에 올 가장 큰 숫자를 찾아 맨 앞으로 보낸 다음, 다시 리스크의 전체를 한번 더 뒤짚는 방식으로 정렬을 하였다.

Key Point : 이미 정렬된 상태는 굳이 정렬하지 않도록 구분하는게 이 문제에 있어서 Point였다.
'''
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:

        lengthA = len(A)
        answer = []

        if A[0] != None :
            max_val = A[0]
            count = 1
        else:
            return []
        num = 1
        while lengthA > 0:
            # 최대값 구하기
            for i in range(lengthA):
                if max_val < A[i]:
                    max_val = A[i]
                    count = i+1 # max의 index

            # 가장 큰 숫자 맨 앞으로 보내기
            if max_val != A[lengthA - 1]: # 이미 Sorting 되어있는 상태이면 굳이 뒤짚기를 하지 않는다.
                answer.append(count)
                for i in range(count // 2):
                    temp = A[i]
                    A[i] = A[count -1 - i]
                    A[count -1 - i] = temp

            # 가장 큰 숫자 맨 뒤로 보내기
            if max_val != A[lengthA - 1]: # # 이미 Sorting 되어있는 상태이면 굳이 뒤짚기를 하지 않는다.
                answer.append(lengthA)
                for i in range(lengthA // 2):
                    temp = A[i]
                    A[i] = A[lengthA -1 - i]
                    A[lengthA -1 - i] = temp

            # 초기화
            lengthA -= 1
            max_val = A[lengthA-1]
            count = lengthA
        return answer

''' LeetCode's Solution

내 풀이방식과 비슷하다.

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        """ sort like bubble-sort
            sink the largest number to the bottom at each round
        """
        def flip(sublist, k):
            i = 0
            while i < k / 2:
                sublist[i], sublist[k-i-1] = sublist[k-i-1], sublist[i]
                i += 1

        ans = []
        value_to_sort = len(A)
        while value_to_sort > 0:
            # locate the position for the value to sort in this round
            index = A.index(value_to_sort)

            # sink the value_to_sort to the bottom,
            #   with at most two steps of pancake flipping.
            if index != value_to_sort - 1:
                # flip the value to the head if necessary
                if index != 0:
                    ans.append(index+1)
                    flip(A, index+1)
                # now that the value is at the head, flip it to the bottom
                ans.append(value_to_sort)
                flip(A, value_to_sort)

            # move on to the next round
            value_to_sort -= 1

        return ans
'''
