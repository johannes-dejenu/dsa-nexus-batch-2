class Solution: 
    def selectionSort(self, arr):
        #code here
        size = len(arr)
        for i in range(size):
            min_idx = i
            for j in range(i + 1, size):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
