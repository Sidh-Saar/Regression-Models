# -*- coding: utf-8 -*-
"""Copy of decision_tree_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d85nAvMFTjV1LGbNvlteRKQgXbCi_qbh

# Decision Tree Regression

## Importing the libraries

Here, we import NumPy, Scikit-learn, and Matplotlib to make our code shorter and more efficient!
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset

The dataset provides a series of positions, along with the corresponding salaries. The "iloc" method is used to select the rows of data.
"""

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
Y = dataset.iloc[:, -1].values

"""## Training the Decision Tree Regression model on the whole dataset

Here, we train the decision tree regression Model on the whole dataset. First, we import the DecisionTreeRegressor from the Scikit-learn libary. Next, we use the fit method to train the model on the dataset.
"""

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, Y)

"""## Predicting a new result

Here, we predict the salary at position level "6.5."
"""

regressor.predict([[6.5]])

"""## Visualising the Decision Tree Regression results (higher resolution)

Here, the results of the model are visualised for ease of understanding. To create the visual, we use Matplotlib.
"""

X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, Y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

"""## Finding the R-squared Value

Here, we find the R-squared value for the model on the test data, indicating how well the model fits the data.

An R-squared value ranges from 0-1, with a higher value indicating a stronger fit.

This will be completed with various regression models, to see which one works best for our dataset!
"""

from sklearn.metrics import r2_score
Y_pred = regressor.predict(X)
r_squared = r2_score(Y, Y_pred)
print(f"R-squared value: {r_squared}")