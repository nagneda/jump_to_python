from re import X
from tracemalloc import start


-내장함수
파이썬에 기본적으로 내장돼있는 대표적인 내장함수의 종류에 대해 살펴보자.

1. abs : 절댓값을 돌려주는 함수
abs(3), abs(1.2)

2. all : 반복가능한 요소를 인수로 받아 요소가 모두 참이면 True,
         거짓이 하나라도 있으면 False (and같은 느낌)
all([1,2,3]) >>> True , all([1,2,3,0]) >>> False // 0은 False다.all
비어있는 자료형이 주어질 경우 True를 리턴(자료형에서는 거짓이었던것과는 다름)

3. any : all과 반대의 개념. or개념과 비슷. 하나라도 참이면 True를 돌려줌.
any([1,2,3,0]) >>> True

4. chr : 유니코드값을 문자로 출력 (유니코드값은 숫자형이다)
chr(97) >>> 'a' chr(44032) >>> '가'

5. dir : 객체가 자체보유하고 있는 함수의 종류를 출력
dir([1,2,3]) >>> ['append','index','count',...]

6. divmod : 인수 2개(a,b)를 받고 a를 b로 나눈 몫과 나머지를 튜플 형태로 리턴
divmod(5,2) >>> (2,1)

7. eval : 실행가능한 문자열을 실행하여 결과값 돌려주는 함수
예를 들면 'divmod(4,3)'같은 함수나 '1+5'등 따옴표가 없을시 연산이나 실행이
가능한 문장을 뜻함. 즉 따옴표를 없애고 실행해주는 기능이라 해야하나..?
eval('divmod(4,3') >>> (1,1) eval('3+4') >>> 7

8. filter : 반복가능한 요소를 함수에 넣었을때 나오는 결과값을 묶어서 돌려준다.
filter(함수이름, 반복가능한 자료형)의 형태로 사용
def positive(x):
    return x%2==0
print(list(filter(positive,[1,2,3,4,5,6]))) 돌려줄때는 list함수로 돌려줘야함.
lambda로 간소화 시키면 
list(filter(lambda x: x%2==0, [1,2,3,4,5,6]))
*람다에 대해서는 조금 더 많은 공부가 필요할 것 같다.

9. hex : 정수값을 16진수 문자열로 반환
hex(234) : '0xea'

10. id : 객체의 고유주소값(레퍼런스)를 돌려주는 함수.
a=3, id(3) >>> 135072304 // id(a) >>> 135072304

11. int : 문자열 형태의 숫자나 소수점있는 숫자를 정수형으로 바꿔주는 함수
int(x)의 형태로 사용하고 int(x,radix)의 형태로 사용시 radix진수로 표현된 X를
10진수로 변환
int('3.4') >>> 3 , int('11',2) >>> 3

12. isinstance : 해당 인스턴스가 해당 클래스의 인스턴스인지 판단. 이즈인스턴스.
class Car: pass

a=Car()
b=2
isinstance(a,Car) >>> True
isinstance(b,Car) >>> False

13. map : 입력받은 자료형의 각 요소를 함수f가 수행한 결과를 묶어서 돌려주는 함수.
filter함수와 마찬가지로 반복가능한(iterable) 자료형을 받다보니 결과값 받을때 list화
시켜줘야함.
def two_times(numberlist):
    return numberlist*2
result=list(map(two_times,[1,2,3,4]))
print(result)

*lambda를 통한 간소화
print(list(map(lambda numberlist : numerlist*2, [1,2,3,4])))  

?map과 filter의 차이 
filter는 함수의 리턴값이 조건문을 통해 True를 돌려줬을때만
함수의 인수로 들어갔던 요소를 묶어서 돌려준다는 것 같음.
map은 메소드도 사용되는진 모르겠고 한개한개만 사용할 수 있는
메커니즘을 가지고있는 함수를 이용할때 사용. 예를들면 1차원 list를
오름차순하려면 그냥 sorted를 하면 되지만 2차원 list라고하면 map을
이용해 리스트 안의 리스트요소들을 오름차순 할 수 있음.
a=[[3,1,2],[5,2,3],[7,1,5]]
a=list(map(sorted,a))
print(a)

14. max / min : 반복가능한 자료형에서 최대값 최소값을 뽑아냄
max([1,2,3]) >>> 3
min([1,2,3]) >>> 1

15. oct : 정수형태의 숫자를 8진수 문자열로 반환
oct(34) >>> '0o42'

16. ord : 문자를 유니코드 값으로 반환
ord('a') >>> 97

17. pow : x의 y제곱 결가값을 돌려줌. pow(x,y)로 사용
pow(2,5) >>> 32

18. range : for문과 자주 사용되는 함수. 개별적으로도 사용가능
range([start,]stop[,step])의 형태로 이뤄져있고 []는 관례적으로 
생략가능한 부분을 뜻함. 즉 stop범위만 지정해놓으면 되고 start와 
step을 따로 지정하지 않으면 각각 0, 1로 설정됨. 얘 역시 map이나 filter처럼
print 이용시 값이 순서대로 출력되지 않음. for문에 쓰거나 list로 묶어씀.
저장되는 데이터형태가 어떤식인지 이해가 필요할 듯.
list(range(5)) >>> [0,1,2,3,4]

19. round : 숫자를 반올림해주는 함수. round(number[,ndigits])
형태로 사용하며 ndigits는 반올림된 후 자릿수를 정해줌. 역시 생략가능
round(4.12326) >>> 4.1233
round(4.12326, 3) >>> 4.123

20. zip : 동일한 개수로 이루어진 자료형을 묶어주는 함수
동일한 개수라는 조건부터 반복가능한 자료형을 뜻함.
a='abcd' , b='efgh'
print(list(zip(a,b))) >>> [('a', 'e'), ('b', 'f'), ('c', 'g'), ('d', 'h')]


