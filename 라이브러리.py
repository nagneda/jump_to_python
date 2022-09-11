import sys
import webbrowser


-라이브러리
유용한 프로그램을 모아놓은 것을 라이브러리 한다.
?라이브러리와 모듈과 패키지와의 관계는 더 공부할 필요가 있다.zip

1.sys : 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 함수.

sys.argv : 명령프롬프트에 들어온 입력값을 리스트로서 결과값을 받음
import sys
print(sys.argv) 를 입력한 프로그램 파일 저장
디렉토리를 해당 파일이 있는 곳으로 설정후 프롬프트 창에서
파일명과 입력값을 입력하면 띄어쓰기를 기준으로 리스트로 받아냄.

sys.path.append : 모듈 경로 추가하기. 

2.pickle : 어떤때에 쓰이는지 잘 모르겠고 필요성이 느껴지지 않아 배제.

3. OS : 환경변수나 디렉터리, 파일 등의 OS자원을 제어할 수 있게 해주는 모듈.

os.environ : 내 시스템의 환경변수값을 불러옴.
이 때 변수명과 디렉터리를 딕셔너리 형태로 저장하고 있기 때문에 내가 궁금한 변수의
경로를 알 수 있음. 이를테면'PYTHONPAH'같은 것들.  os.environ['PYTHONPATH']시 디렉터리 출력

os.getcwd() : 현재 디렉토리 위치 반환하기
os.getcwd() >>> 'C:\doit'
*프롬프트라 가정하고 백슬래쉬로 작성. 소스코드 안일 경우 안됨.
os.chdir('변경할 디렉토리') : 현재 디렉토리 위치 변경하기
>>> os.chdir('C:\doit\mymod')
명령어 : cmd창에서 실행가능한 시스템명령어를 파이썬에서도 실행할 수 있다.
os.('명령어')의 형태로 사용하며 python을 실행하지않은 프롬프트창에서는 
그냥 '명령어'의 형태로만 사용해도 된다.
*시스템명령어의 종류
mkdir(디렉터리) : 디렉터리 생성
rmdir(디렉터리) : 디렉터리 삭제, 단 비어있어야 가능
unlink(파일) : 파일을 지운다.
os.rename(src, dst) : src라는 이름의 파일은 dst라는 이름으로 바꾼다.

위 명령어들을 파이썬에서 사용하기 위해선 import os 후 os.을 앞에 붙이면 된다.
 
4. shutil : 파일을 복사해주는 모듈
shutil.copy(복사할 파일, 피복사 파일(기존파일도 가능))의 형태
복사할 파일의 내용을 피복사파일로 복사해줌. 피복사파일명은 작성할때 정해도 되고
기존에 있는 파일이라면 덮어쓰기 된다.

5. glob : 생략

6. tempfile : 생략

7. time : 시간과 관련된 함수가 많은 모듈
time.time() : 현재시간을 실수형태로 돌려주는 함수(1970년 1월1일 0시 기준)
time.time() >>> 1662871908.0791872
time.localtime(실수) : 실수값을 사용해 연도 월 일 시 분 초 형태로 바꿔줌.
> 현재 시각에 관련된 값을 원하면 괄호안에 time.time기입하면 되고 실수 아무거나 넣어도 됨.
현재 시간과 너무 많이 초과하는 건 안되는 듯.
(tm_year=2022, tm_mon=9, tm_mday=11, tm_hour=15, tm_min=16, tm_sec=48, tm_wday=6, tm_yday=254, tm_isdst=0)
time.asctime() : time.localtime을 이용해 나온 튜플 형태의 값을 인수로 이용해
보기쉬운 형태로 바꿔줌.
time.asctime(time.localtime(time.time())) >>> 'Sun Sep 11 13:54:33 2022'
time.ctime() : time.asctime과 같이 현재시각을 나타내는 간소화된 함수. 다만 
현재시각외의 실수값에 따른 변동된 시간은 출력 불가.
time.strftime() : time.localtime을 통해 튜플로 나온 값을 이용해 원하는 정보만
표현하는 함수. time.strftime('출력할 형식 포맷코드',time.localtime(time.time()))의 형태로 사용
시간 포맷코드는 워낙많아서 일부만 정리.
%a : 요일줄임말 , %b : 달 줄임말 , %c : 날짜와 시간 출력
time.strftime('%a',time.localtime(time.time())) >>> 'SUN'
time.sleep : 주로 루프안에서 사용. 일정 간격을 두고 다음 문장을 실행
time.sleep(3)
print('하이') >>> 3초뒤에 하이가 출력됨

8. calendar : 달력을 보여주는 모듈
calendar.calendar(연도) : 해당연도의 달력출력
calendar.weekday(연도,월,일) : 해당날짜의 요일 정보를 돌려준다.
월요일부터 일요일까지 순차적으로 0~6이다.
calendar.weekday(2022,9,11) >>> 6  // 9월이면 09가 아니고 9로 입력
calendar.monthrange(연도,월) : 입력받은 달의 1일의 요일과 그 달이 며칠까지
있는지 튜플 형태로 반환
calendar.monthrange(2022,9) >>> (3,30)

9. random : 난수(규칙이 없는 임의의 수)를 발생시키는 모듈
random.random() : 0에서 1사이의 난수를 돌려준다.
random.random() >>> 0.1251252346
random.randint(시작숫자,끝숫자) : 범위내의 정수 중 난수를 돌려준다.
random.randint(1,10) >>> 4

여기서 잠깐 pop메소드에 대해 짚고 넘어가자
객체.pop([삭제할 요소의 인덱스번호])의 형태로 사용한다
a=[1,5,2,3]이라는 리스트가 있을때
a.pop() >>> 3을 출력하고
a >>> [1,5,2]가 된다
a.pop(1) >>> 5 #인덱스 번호 1번 요소를 return하며 삭제
a >>> [1,2]

random.choice(반복가능한 요소) : 반복가능한 요소 중 1개를 랜덤으로 반환
a=[2,4,6,1]
random.choice(a) >>> 4
b='안녕하세요'
random.choice(b) >>> '세' #b.pop()은 에러발생 이유는 아래서 서술
***문자열은 반복가능한 요소(iterable)이면서 동시에 변경할 수 없는(immutable)값이다.
즉 인덱싱을 통한 요소반환 같은 건 되지만 수정 삭제 추가는 절대 불가능하다는 것.
pop(제거)은 안되고 choice(인덱싱)는 되는 것도 그 때문.

random.shuffle(리스트) : 리스트 내 요소를 무작위로 섞음

10. webbrowser : 자신의 시스템에서 사용하는 웹 브라우저 자동으로 실행하는 모듈
webbrowser.open(URL) : 해당 URL주소로 이동

11. thread : 생략. 요약하자면 한 프로세스에서 여러가지의 동시작업을
가능하게 해주는 모듈.


