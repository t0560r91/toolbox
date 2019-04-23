import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold

def get_cv_scores(X, y, estimator, verbos=False, **params):
    """
    "Takes in X, y, estimator, and optional parameters 
    and returns cross validated train, test MSE and R2 scores.
    If verbos=True, returns coef_ and intercept_."

    INPUT:
        X: Pandas DataFrame
        y: Pandas Series
        estimator: ML algorithm class in Sklearn interface
        **params: optioanal parameters for the estimator
        verbos: True or False

    OUTPUT:
        Train CV MSE
        Train CV R2
        Test CV MSE
        Test CV R2
        Beta Coefficients
        Intercept
    """
    
    kf = KFold(5, shuffle=True)
    test_mses = []
    test_r2s = []
    train_mses = []
    train_r2s = []
    for train, test in kf.split(X):
        model = estimator(params)
        model.fit(X.loc[train], y.loc[train])
        ytest_ = model.predict(X.loc[test])
        ytrain_ = model.predict(X.loc[train])

        test_mses.append(mean_squared_error(y.loc[test], ytest_))
        test_r2s.append(r2_score(y.loc[test], ytest_))
        train_mses.append(mean_squared_error(y.loc[train], ytrain_))
        train_r2s.append(r2_score(y.loc[train], ytrain_))
        output = np.mean(train_mses), np.mean(train_r2s), np.mean(test_mses), np.mean(test_r2s)

    if verbos==True:
        try:
            coef = model.coef_
        except:
            coef = None
        try:
            intercept = model.intercept_
        except:
            intercept = None
        output = output + tuple([coef, intercept])
        
    return output