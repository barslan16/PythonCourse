# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 06:45:00 2020

@author: Beyza
"""

import regresdeneme

def test(filename,independent,dependent):
    df = pd.read_csv(filename)
    df.head()
    a= independent
    b= dependent
    s1 = pd.Series(df[a])
    s2 = pd.Series(df[b])
    new_frame = pd.concat(objs=(s1 , s2), axis=1)
    new_frame = new_frame.astype(int)

    train_df = new_frame[0:int((len(new_frame)*70)/100)]
    test_df = new_frame[int((len(new_frame)*70)/100):len(new_frame)]

    X = train_df[a]
    y = train_df[b]
    lr = LineerRegresyon(w_intercept=True)
    lr.fit(X,y)
    print(lr.coef_)
    print(lr.predict([65]))

    X = pd.Series(test_df[a])
    y = lr.predict(test_df[a]).tolist()
    test_df.plot.scatter(x=a,y=b)
    plt.plot(X,y,color="green")

    scores = lr.score(train_df[a],train_df[b])

    e = lr.residual(train_df[a],train_df[b])

    varb = lr.varyansofb(train_df[a])
    print(math.sqrt(varb))

    tstatt = lr.tstat()
    print(tstatt)

    inter = lr.interval()
    print(inter)
