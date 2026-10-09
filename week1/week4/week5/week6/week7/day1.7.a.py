import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = np.array([
    [7.5,7,80],[8.0,8,78],[6.5,6,76],[7.0,9,68],[9.0,8,82],[7.5,7,70],[8.0,8,84],
    [6.0,6,66],[8.5,9,90],[7.0,8,80],[7.5,8,78],[9.0,7,80],[7.0,9,86],[7.5,8,74],
    [7.0,7,70],[8.0,8,82],[6.5,6,62],[7.5,9,81],[8.0,8,80],[7.0,7,70],[8.5,9,90],
    [7.0,8,75],[7.5,8,80],[6.5,6,68],[8.0,9,92],[9.5,7,86],[7.0,8,73],[8.0,9,88]
])
steps = np.array([
    9200,10500,8800,11000,7600,9400,10200,
    8900,10800,9100,11200,7900,10000,9700,
    9500,10300,8600,11500,8200,9800,10600,
    9000,10100,8400,10900,7500,9600,10400
])
y = (steps >= 10000).astype(int)
print("Label distribution (1 = hit goal, 0 = missed):")
print(f"Hit goal:  {y.sum()}/28days")
print(f"Missed:  {(y == 0).sum()}/28days")

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.25,random_state= 42)
clf = RandomForestClassifier(n_estimators = 10, random_state = 42)
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(f"\nClassification accuracy: {accuracy:.0%}")


new_days = np.array([[8.0,8,80],[6.0,5,62],[9.0,9,90]])
preds = clf.predict(new_days)
labels = {1:"Goal hit", 0 :"Below goal"}

print("\nPredictions for new day")
for inputs, pred in zip(new_days,preds):
    print(f"Sleep = {inputs [0]}h, Water = {int(inputs[1])}g, Bench press= {int(inputs[2])}kg => {labels[pred]}")


