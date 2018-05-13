from sklearn import tree

#[Height, Weight, Shoe size]
x = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [155, 56, 23], [154, 89, 43]]

y = ['male', 'male', 'female', 'female', 'male']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

result = clf.predict([[180, 70, 42]])

print(result)
