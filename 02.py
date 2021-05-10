daum = 89000
naver = 751000
total = daum*100 + naver *20
loss = (daum*100*0.05) + (naver*20*0.10)

print(total)
print(loss)

#F = 1.8*C+32
F=50
C = (F-32)/1.8
print(C)

a=0
while 1:
    a+=1
    print('pizza')
    if a == 10:
        break

monday_start_price = 1000000
monday_end_price = monday_start_price*0.7

tuesday_start_price = monday_end_price
tuesday_end_price = tuesday_start_price*0.7

wednesday_start_price = tuesday_end_price
wednesday_end_price = wednesday_start_price*0.7
print(wednesday_end_price)

이름 = 's'
생년월일 = '1998년 12월 02일'
주민등록번호 = '202102-0200200'

print(이름, 생년월일, 주민등록번호)

s = 'Daum KaKAo'
s[0:1] = 'KaKao', 'Daum'

a = 'hello world'
a[0] = 'Hi'
print(s)
print(a)

x = 'abodef'
x = 'bdefa'
print(x)