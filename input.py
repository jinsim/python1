# 파이썬에서 입력을 받는 함수가 있습니다~~ 구글링해서 찾아보세요!

print('문제 1. 전화번호 받기')

print('조건 1. 저장할 때는 공백 문자 없이')
print('조건 2. -, ., , 등이 들어올 때 전부 제외 하고 숫자만 저장!')

print('문제 2. 영어 이름 받기')
print('choi juwon 을 입력 받으면,')
print('first name : Choi, last name: Juwon 이 출력되게 만들기')

# 문제1 
number = input("전화번호를 입력해주세요:")
number = number.replace("-","").replace(".","").replace(",","")
print(number)

# 문제2 
eng = input()
eng = eng.title().split()
print("first name : ",eng[0],", last name: ",eng[1])