'''
과제 1. 별찍기 (4월 20일까지)
- 아래와 같이 * 을 출력 하는 프로그램을 만들어보세요
**********
*********
********
*******
*****
****
***
**
*


과제 2. 구구단 (4월 20일까지)
- 구구단 2단을 출력해보세요!

과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요. (4월 20일까지)

과제 4. for 문을 활용하여 멋사 학생들의 평균 점수를 구해보세요. (4월 20일까지)
- mutsa_scores = [90, 77, 40, 55, 90, 100, 88]

과제 5. input.py 문제 2개 풀기 (4월 20일까지)

과제 6. HTML / CSS 페이스북 모바일 클론코딩 (4월 27일까지)
- 이미지 자율
- 까먹기전에 해주세요~

'''
# 과제1
i=0
while i <10:
    i += 1
    if i == 5:
        continue
    print("*" * (11-i))

# 과제2
for i in range(1,10):
    j=2
    print(j,"*",i,"=",j*i)

# 과제3
j=0
while i<1001:
    if i % 3 == 0:
        j += i
    i += 1
print(j)

# 과제4
mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
total = 0
average = 0
for score in mutsa_scores:
    total += score
average = total / len(mutsa_scores)
print(average)