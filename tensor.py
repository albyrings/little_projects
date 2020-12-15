import pandas as pd
import numpy as np
import sklearn 
from sklearn import linear_model
from sklearn.utils import shuffle


data = pd.read_csv("FL_insurance_sample.csv",sep=",")

data=data[["policyID","hu_site_limit","fl_site_limit","fr_site_limit"]]
predict="policyID"

x = np.array(data.drop([predict], 1))
y=np.array(data[predict])

x_train, x_test, y_train, y_test =sklearn.model_selection.train_test_split(x,y,test_size = 0.2)
linear =linear_model.LinearRegression()

linear.fit(x_train,y_train)

acc=linear.score(x_test,y_test)
print(acc)
print(linear)
