# 다시까먹을 미래의 나를 위한 주석
import sys
t = int(sys.stdin.readline())
i = [int(sys.stdin.readline()) for i in range(t)]

dp = []
# 직접 3번째 최대값까지 작성(이유 dp의 4번째 최대값을 구하기 위해 dp[1]을 찾을 때 없어서 오류가 날 수 있어서)
dp.append(i[0])  # 첫계단의 최대값
if t >= 2:
    dp.append(i[1]+i[0])  # 두번째 계단 최대값
if t >= 3:
    dp.append(max(i[2]+i[0], i[2]+i[1]))  # 세번째 계단 최대값
for a in range(3, t):  # 위에 3번째계단까지는 계산했으니 3부터 시작(4번째 계단부터 계산 시작)
    dp.append(max(dp[a-2] + i[a], dp[a-3]+i[a-1]+i[a]))
    # print(dp[a-2] + i[a])
    # print(dp[a-3]+i[a-1]+i[a])
    # dp[a-2](a-2까지 계단의 최대값) + i[a](현재 계단의 점수) = 두 칸으로 간경우,
    # dp[a-3](a-3까지 계단의 최대값)+i[a-1](a-1계단의 점수)+i[a](현재 계단의 점수)= 한 칸으로 간경우
    # 추가 설명 dp[a-3]의 최대값을 더한이유 현재 계단 수는 i[a]이기 때문에 전계단인 i[a-1]의 점수를 더하는데 한 칸씩 연속으로 갈 수 는 없기에 dp[a-1]이 아닌 dp[a-3]의 최대값을 들고온다
print(dp[len(dp)-1])
