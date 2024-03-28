# 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.
# 1 ≤ str의 길이 ≤ 20
# str은 알파벳으로 이루어진 문자열입니다.
# 입력 예 ) aBcDeFg
# 출력 예 ) AbCdEfG
S = input()
for i in S:
    if i.isupper(): # 문자열전체를 T,F 형태로 구분해준다
        i = i.lower() # 대문자는 소문자로 소문자는 대문자로 변경
    else:
        i = i.upper()
    print(i, end='') # 변경사항 출력