import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

df = pd.read_csv("glass.csv")
y = df["Type"]
df1 = df.drop("Type",axis=1).copy()
X_train, X_test, Y_train, Y_test = train_test_split(df1, y,test_size=0.3)
svc = SVC(kernel='rbf', C=1, random_state=0)
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
acc_svc1 = round(svc.score(X_test, Y_test) * 100, 2)
print("svm accuracy with test is:", acc_svc1)