# 문자열 str이 주어질 때, str을 출력하는 코드를 작성해 보세요.
# 1 ≤ str의 길이 ≤ 1,000,000
# str에는 공백이 없으며, 첫째 줄에 한 줄로만 주어집니다.
# 입력 예) HelloWorld!
# 출력 예) HelloWorld!

str = input() # 문자열 str에 input() 사용하여 문자입력
# str의 길이가 1이상 1000000 이하이며 공백이 없을때  str = input()의 입력을 출력
if len(str)>= 1 and len(str) <= 1000000 and str!= ' ': 
    print(str)
else:
    print("다시 입력하세요.") # 위 조건성립이 안되면 출력