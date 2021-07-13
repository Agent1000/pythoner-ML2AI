#Gradient Descent
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
mnist_raw=loadmat("C:/Users/000/Desktop/work1/mnist-original.mat")
mnist={
    "data":mnist_raw["data"].T,
    "target":mnist_raw["label"][0],
}
#x data y traget
x,y=mnist["data"],mnist["target"]
##train $ tes set
#class 0-9
x_train,x_test,y_train,y_test =x[:60000],x[60000:],y[:60000],y[60000:]

def displayImage(x):
    plt.imshow(x.resp(28,28),camp=plt.cm.binary,interpolation="nearest")
plt.show()



# y_train =[0,0,.......,9.....,9]
predct_number = 5500
y_train_5=(y_train==5)
y_test_5=(y_test==5)

sgd_clf = SGDClassifier()
sgd_clf.fit(x_train,y_train_5)






#print(x_train.shape)
#print(x_test.shape)
#print(y_train.shape)
#print(y_test.shape)