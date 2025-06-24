import random
import time

class Test:
    def __init__(self,sortTimes=1000,maxNum=1000,len=100):
        self.arrays = []
        for _ in range(sortTimes):
            arr = [random.randint(0,maxNum) for _ in range(len)]
            random.shuffle(arr)
            self.arrays.append(arr)
        return

    def run(self,func):
        errorTimes = 0
        startTime = time.time()
        testArrays = self.arrays.copy()
        for arr in testArrays:
            testArr = arr.copy()
            func(testArr)
            for i in range(len(testArr) - 1):
                if testArr[i] > testArr[i + 1]:
                    print(f"Error in {func.__name__} at index {i}: {testArr[i]} > {testArr[i + 1]}")
                    errorTimes += 1
                    break
        if errorTimes > 0:
            print(f"Function {func.__name__} failed {errorTimes} times.")
        endTime = time.time()
        print(f"Function {func.__name__} completed {len(self.arrays)} Times in {endTime - startTime:.6f} seconds.")
        return
    
    def RunAll(self,funcs):
        for func in funcs:
            self.run(func)
        return