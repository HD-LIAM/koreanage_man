korean_age = int(input("한국 나이를 입력하세요: "))    # int를 입력하지 않으면 type error발생
birth = int(input("생일이 지났습니까? 맞으면 0, 아니면 –1을 입력하세요: "))     # hint사용

if birth == 0 :    #if조건문 사용
 print(f"미국 나이는 : {korean_age}입니다. ")   # fstring사용하여 print안에 변수 계산함
else:                
 print(f"미국 나이는 : {korean_age} – {1} = {korean_age-1}입니다. ")   # fstring사용 시 변수나 정수마다 {}해줘야 한다는점 주의!!