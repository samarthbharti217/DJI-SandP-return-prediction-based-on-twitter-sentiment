import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=FutureWarning)
    import pandas as pd
    import numpy as np
    import statsmodels.api as sm


ret = pd.read_csv("C:/Users/hp pc/Downloads/final(query)_donald trump.CSV", header=0)
x = np.asarray(list(ret["Polarity"]))
y = np.asarray(list(ret["ixic_ret"]))

model = sm.OLS(y, x).fit()
predictions = model.predict(x)

print(model.summary())