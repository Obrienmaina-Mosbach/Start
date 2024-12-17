from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Data Collection
iris = load_iris()
X, y = iris.data, iris.target

# 2. Preprocessing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Modeling
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 4. Evaluation
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))