import sys

NumA, Numb = map(int, sys.stdin.readline().split())

NumAList = list(map(int, sys.stdin.readline().split()))
NumBList = list(map(int, sys.stdin.readline().split()))

Result = NumAList + NumBList

ResultDict = list(dict.fromkeys(Result))

print(len(ResultDict) - (len(Result) - len(ResultDict)))