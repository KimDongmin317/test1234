import numpy as np
#넘파이 버전 확인하기
#print(np.__version__)

a1 = np.array([1, 2, 3, 4, 5])
print(a1)
#ndarray는 n차원의 매트릭스임을 나타냄
print(type(a1))
#2차원 배열 생성하기
a2 = np.array([ [1,2,3], [4,5,6],[7,8,9]])
print(a2)
# n by n 형식으로 보여줌
print(a2.shape)
print(type(a2))
#a2[x,y]는 x행y열의 숫자를 의미함
print(a2[0,0],a2[0,1],a2[1,2])

#3차원
a3 = np.array([[[1,2,3],[4,5,6],[7,8,9]],
              [[10,11,12],[13,14,15],[16,17,18]],
              [[19,20,21],[22,23,24],[25,26,27]]])
print(a3)
print(a3.shape)

print(a3[2,2,0])
