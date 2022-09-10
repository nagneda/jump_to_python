-패키지
패키지는 파이썬 모듈을 디렉토리 구조로 저장해놓은 것을 뜻한다.
쉽게 말하자면 모듈들의 집합체라고 할 수 있으며 여러개의 디렉토리들로
이루어져있고 그 디렉토리내에 모듈이 있는 형식이다.
폴더들안에 모듈이 있고 그 폴더안에 또 폴더가 있고..이런식이다.
사용방법은 모듈을 사용하는 것과 비슷하다.

우선 PYTHONPATH 혹은 sys.path.append를 통해 패키지를 불러올 디렉토리를
설정해준다. 이후에 a폴더안의 b폴더안의 c라는 모듈을 불러오고 싶다면
import a.b.c의 형태로 사용하거나 from a.b import c로 사용할 수도 있다.
이때 주의할점은 import끝에 오는 a.b.c의 항목에서 c는 무조건 모듈이어야한다.
(점프투파이썬에서는 패키지 혹은 모듈이어야 한다고 명시돼있는데 내 생각에는
모듈이어야만 한다.)
다만 from import의 형태로 작성할 시에는 import에
모듈의 함수명까지 작성가능(일반적인 모듈 import방법과 동일 
ex)from random import randint같은 형태 // randint는 random의 함수이다.
또한 사용하려는 모듈까지는 선언을 해주어야한다. import a만 하고 a.b.c.함수
이런식으로는 사용이 불가능하다.

다른 내용이 많이 있으나 우선은 간단하게 이까지 정리. 어떻게 동작하고
사용해야하는지만 알고 있자. 추가내용있을시 추가서술할 계획.