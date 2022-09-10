a=[True,20]

if a[0]==a[1]: print('같다')

'''
위 프로그램에서 '같다'라는 출력문이 나올까? 정답은 안나온다. bool자료형은 True와 False 
두가지로 이루어져있고 기본적인 자료형들 조차 bool값을 가지고 있다. 문제는 위와
같은 조건문에서는 a[1]을 True로 인식해서 비교하는 것이 아닌 True가 1의 값으로서
비교대상이 된다. 다음이 그 반증이다.  
'''

if a[0]==1: print('True는 1이다')


#그럼 bool을 이용해 20의 bool값인 True를 이용해 비교해보자

if a[0]==bool(a[1]): print('True와 20의 bool값은 같다')
#정상적으로 출력됨을 확인할 수 있다.

b='ㅇㅇ'
if True==bool(b): print('문자열도같네')

c=[1,2,3,4]
d=[5,6,7,8]
if True:
    c,d=d,c

print(c,d)
c[2]=100
print(c,d)

c=[1,9,6,4,5]
d=[2,4,1,0,3]
print(d[c.index(max(c))])
c[1],d[1]=d[1],c[1]
print(c,d)