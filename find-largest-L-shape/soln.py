# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    def spread(i,j): # spread the False left, up, and left-up
        if 0 <= i - 1 < N and 0 <= j < M:
            A[i - 1][j] &= A[i][j]
        if 0 <= i < N and 0 <= j - 1 < M:
            A[i][j - 1] &= A[i][j]
        if 0 <= i - 1 < N and 0 <= j - 1 < M:
            A[i - 1][j - 1] &= A[i][j]

    def findL(R, C, k):
        for i in range(R):
            for j in range(C):
                if i + k < R and j + k < C and \
                A[i][j] and A[i + k][j] and A[i + k][j + k]:
                    return True
        return False

    M, N = len(A[0]), len(A)
    R, C = N, M
    K = 1
    ans = 0
    while R > 0 and C > 0:
        if findL(R, C, K):
            ans = K
        for i in range(R):
            for j in range(C):
                spread(i,j)
        K += 1
        R -= 1
        C -= 1
    return ans
