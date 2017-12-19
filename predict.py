import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures
    import pandas as pd
    import numpy as np

ret = pd.read_csv("C:/Users/hp pc/Downloads/final(query)_donald trump.CSV", header=0)
x = np.asarray(list(ret["Polarity"]))
y = np.asarray(list(ret["ixic_ret"]))

x = x.reshape(1260, 1)
y = y.reshape(1260, 1)

pf = PolynomialFeatures(degree=2)
poly_x = pf.fit_transform(x)

genius_regression_model = LinearRegression()
genius_regression_model.fit(poly_x, y)
print("################################################### WELCOME ############################################################")
print("1. Enter range of sentiment for evaluation\n2. Enter single sentiment point for evaluation: ")
c = int(input())


if(c==1):
    lis = []
    while(True):
        print("\n\n-----------------------------------------------------------")
        lis.append(float(input("Enter the next sentiment to evaluate: ")))
        c = input("\nEnter 'exit' to start calculating or any other key to continue: ")
        print("-----------------------------------------------------------")
        if(c.lower()=="exit"):
            break

    print("\n\n")
    for sent in lis:
        print('When tweet sentiment was: ', sent, " expected return was: ",genius_regression_model.predict(pf.fit_transform([sent])))
        print("\n")

elif(c==2):
    sent = float(input("Enter the sentiment to evaluate: "))
    print('When tweet sentiment was: ',sent," expected return was: ", genius_regression_model.predict(pf.fit_transform([sent])))
else:
    print("Incorrect Choice...")
print("###############################################################################################################")