import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate a sample dataset for wireless communication
# The dataset consists of 1000 samples, each with 2 features
data = np.random.randn(1000, 2)

# Assign labels to the samples
labels = np.random.randint(0, 2, size=1000)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)

# Train a decision tree classifier on the training data
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Use the trained classifier to make predictions on the test data
y_pred = clf.predict(X_test)

# Evaluate the performance of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy * 100))