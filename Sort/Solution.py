import random

class Solution:
    def __init__(self):
        print("ok")
        return
    
    def swap(self,arr:list[int],i:int,j:int):
        temp = arr[i]
        arr[i]= arr[j]
        arr[j] = temp
        return

    ########交换排序########

    #冒泡排序
    def bubbleSort(self,arr:list[int]) -> None:
        n = len(arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j] > arr[j + 1]:
                    self.swap(arr,j,j+1)
        return

    #快速排序 
    def quickSort(self,arr) -> None:
        n = len(arr)
        self._quickSort(arr,0,n-1)
        return
    
    def _quickSort(self,arr,left,right) -> None:
        if(left >= right):
            return
        pivot = self._quickSortPartition(arr,left,right)
        if pivot > left:
            self._quickSort(arr,left,pivot-1)
        if pivot < right:
            self._quickSort(arr,pivot+1,right)
        return

    def _quickSortPartition(self,arr,left,right) -> int:
        if left >= right:
            return left 
        
        # 随机选择一个基准元素,放到left
        self.swap(arr, left, random.randint(left, right))

        pivot = arr[left]
        hole = left

        while left < right:
            while left < right and arr[right] >= pivot:
                right -= 1
            arr[hole] = arr[right]
            hole = right
            while left < right and arr[left] <= pivot:
                left += 1
            arr[hole] = arr[left]
            hole = left
        arr[hole] = pivot

        return hole
        
    ########插入排序########

    #直接插入排序
    def insertionSort(self,arr:list[int]) -> None:
        n = len(arr)
        for i in range(1,n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return
    
    #折半插入排序
    def binaryInsertionSort(self,arr:list[int]) -> None:
        n = len(arr)
        for i in range(1,n):
            key = arr[i]
            left, right = 0, i - 1
            
            # 二分查找插入位置
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > key:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # 将元素向后移动
            for j in range(i - 1, left - 1, -1):
                arr[j + 1] = arr[j]
            arr[left] = key
        return
    
    #希尔排序
    def shellSort(self,arr:list[int]) -> None:
        n = len(arr)
        gap = n // 2
        
        #gap即每组数相差的间隔，当gap为一时，即为普通插入排序，可额外进行折半优化
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return
    
    ########选择排序########
    #简单选择排序
    def selectionSort(self,arr:list[int]) -> None:
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            if min_index != i:
                self.swap(arr, i, min_index)
        return
    
    #堆排序
    def heapSort(self,arr:list[int]) -> None:
        n = len(arr)
        
        # 构建最大堆
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)
        
        # 逐个取出元素
        for i in range(n - 1, 0, -1):
            self.swap(arr, 0, i)
            self._heapify(arr, i, 0)
        return
    
    def _heapify(self, arr:list[int], n:int, i:int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            self.swap(arr, i, largest)
            self._heapify(arr, n, largest)
        return
    
    ########归并排序########
    #后续遍历，自底向上归并
    def mergeSort(self, arr:list[int]) -> None:
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # 处理剩余元素
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return
    
    #######基数排序########
    #基数排序
    def radixSort(self, arr:list[int]) -> None:
        if len(arr) == 0:
            return
        
        max_num = max(arr)
        exp = 1
        
        while max_num // exp > 0:
            self._countingSort(arr, exp)
            exp *= 10
        return
    
    def _countingSort(self, arr:list[int], exp:int) -> None:
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        # 统计每个数字的出现次数
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
        # 累加计数
        for i in range(1, 10):
            count[i] += count[i - 1]
        # 构建输出数组
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        # 将排序后的结果复制回原数组
        for i in range(n):
            arr[i] = output[i]  
        return

        