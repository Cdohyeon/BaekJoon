from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    s = deque(map(int, input().split()))
    s_ = deque(0 for i in range(a))
    s_[b] = 1
    cnt = 0
    while True:
        if s[0] == max(s):
            cnt += 1
            if s_[0] == 1:
                print(cnt)
                break
            else:
                del s[0]
                del s_[0]
        else:
            s.append(s[0])
            del s[0]
            s_.append(s_[0])
            del s_[0]
