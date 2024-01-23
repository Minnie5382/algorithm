money = int(input())
price = list(map(int, input().split()))

# BNP
bnp_money = money
timing_money = money

bnp_stock = 0
for p in price:
    if bnp_money >= p: # 주식을 살 수 있으면
        bnp_stock += bnp_money//p # 오늘 매수한 주식 개수
        bnp_money -= p*(bnp_money//p)

# timing
timing_stock = 0
differ = [(price[i+1] - price[i]) for i in range(len(price)-1)]
differ.insert(0, 0)
for i in range(len(price)-2):
    # 3일 연속 하락 -> 전량 매수
    if differ[i] < 0 and differ[i+1] < 0 and differ[i+2] < 0:
        timing_stock += timing_money//price[i+2]
        timing_money -= (timing_money//price[i+2])*price[i+2]

    # 3일 연속 상승 -> 전량 매도
    if differ[i] > 0 and differ[i+1] > 0 and differ[i+2] > 0:
        timing_money += price[i + 2] * timing_stock
        timing_stock = 0 # 전량 매도했으니 0개


bnp_asset = bnp_money + price[-1]*bnp_stock
timing_asset = timing_money + price[-1]*timing_stock

if bnp_asset > timing_asset:
    print("BNP")
elif bnp_asset < timing_asset:
    print("TIMING")
else:
    print("SAMESAME")
