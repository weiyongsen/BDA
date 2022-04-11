import numpy as np
A = np.array([[1,2],[1,2],[0,0]])
print('打印A：\n{}'.format(A))
u,sigma,vt=np.linalg.svd(A)
print(u,sigma,vt)
# print(u*sigma*vt.T)