
naver_closing_price = ['날짜', '요일', '종가']
naver_closing_price[0] = [ '09/07', '09/08','09/09','09/10','09/11']
naver_closing_price[1] = [ '월', '화', '수', '목', '금']
naver_closing_price[2] = [ 474500, 461500, 501000, 500500, 488500]

max = max(naver_closing_price[2])
min = min(naver_closing_price[2])
dif = max-min
print('가격차: ', dif)

naver_closing_price[2][3]

naver_closing_price2 = {'09/07':474500, '09/08':461500, '09/09':501000, '09/10': 500500, '09/11':488500}
naver_closing_price2
{'09/09': 501000, '09/11': 488500, '09/08': 461500, '09/10': 500500, '09/07': 474500}

list((naver_closing_price2.values()))[1]