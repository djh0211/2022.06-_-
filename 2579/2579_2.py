import sys
input = sys.stdin.readline

N = int(input())
points = []


'''
dp[n] = dp[n-3]+points[n-1]+points[n], dp[n-2]+points[n]

'''