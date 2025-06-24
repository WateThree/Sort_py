from Sort.Solution import Solution
from Sort.Test import Test

solution = Solution()
sortFuns = [solution.bubbleSort,
        solution.quickSort,
        solution.insertionSort,
        solution.binaryInsertionSort,
        solution.shellSort,
        solution.selectionSort,
        solution.heapSort,
        solution.mergeSort,
        solution.radixSort]
test = Test(len=100)
print("Testing with array length 100:")
test.RunAll(sortFuns)
test = Test(len = 200)
print("Testing with array length 200:")
test.RunAll(sortFuns)
test = Test(len = 400)
print("Testing with array length 400:")
test.RunAll(sortFuns)
test = Test(len = 800)
print("Testing with array length 800:")
test.RunAll(sortFuns)