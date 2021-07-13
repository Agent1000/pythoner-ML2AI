from sklearn import datasets
iris_dataset = datasets.load_iris()
digit_dataset = datasets.load_digits()

print(iris_dataset.keys())
print(iris_dataset['filename'])
print(digit_dataset.images[0])