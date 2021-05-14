# 예제1) 리턴문도 없고, 인자도 없는 함수
# def printHello() :
#     print("Hello, User")

# printHello()

# 예제2) 리턴문이 없는 함수 (인자는 있음)
# def printHi(name) :
#     print("Hi", name)

# name = input("당신의 이름은? ")
# printHi(name)

# 예제3) 리턴문이 있는 함수
# def printWelcome(user) :
#     word = "Welcome, " + str(user)
#     return word

# user = int(input("당신의 학번은? "))
# print(printWelcome(user))

# 예제4) 세 개의 값을 동시에 리턴하는 함수
# def func_mul(x) :
#     y1 = x*10
#     y2 = x*20
#     y3 = x*30
#     return y1, y2, y3
# (y1, y2, y3) / [y1, y2, y3]도 가능, 이때는 결과값 하나만 지정해도 됨

# a, b, c = func_mul(10) # return 값이 3개이므로 결과값도 3개를 지정해줘야 함
# print(a, b, c)

# a = func_mul(10)
# print(type(a), a)

# 문자열 안에 우리가 원하는 값을 쉽게 삽입해보자 → formatting
# 파이썬에는 여러 문자열 포매팅 방법이 있습니다!
# 여기서는 format 함수를 사용한 포매팅만 알고 넘어갑시다!
# 더 자세한 포매팅 방법을 알고 싶다면, https://wikidocs.net/13 를 참고해주세요!

# 1. 문자열에 숫자를 바로 대입하기
# print("저는 덕성 멋사 {}기 입니다.".format(9))

# 2. 문자열에 문자열을 입력받아 대입하기
# fruit = input("당신이 좋아하는 과일은? ")
# print("내가 좋아하는 과일은 {}입니다.".format(fruit))

# 3. 두 개 이상의 값을 넣기 (숫자는 인덱스, 문자는 이름으로 삽입)
print("저는 {}학번 {}과입니다.".format(20, "정보통계학"))
print("저는 {}학번 {major}과입니다.".format(20, major = "정보통계학")) #문자 지정도 가능






