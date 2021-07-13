import pylab
from sklearn import datasets
digit_dataset=datasets.load_digits()

pylab.imshow(digit_dataset.data.image[7],cmap=pylab.cm.gray_r)
pylab.show()