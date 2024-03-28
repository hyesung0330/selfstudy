a, b = map(int,input().strip()) # map() - 각요소들에 특정함수를 적용하고싶을때 사용
# strip() - 문자열의 시작과 끝에서 주어진 문자 제거
# a 가 -100000 이상이며 b 가 100000 이하 일때
if a >= -100000 and b <= 100000:
    print("a = "+ str(a)) 
    print("b = "+ str(b)) 
else:
    print("다시 입력하세요")