#!/usr/bin/env python

import numpy as np
from scipy.sparse import vstack
from sklearn.ensemble import IsolationForest
from sklearn.datasets import load_svmlight_file
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.random_projection import SparseRandomProjection
import sys

filename = sys.argv[1]
attack = sys.argv[2]
scenario = sys.argv[3]

print >> sys.stderr, "loading data...", filename
data = load_svmlight_file(filename)
X = data[0]
y = data[1]

if scenario == "all":
    X1benign = X[:300,:]
    y1benign = y[:300]
    X2benign = X[400:600,:]
    y2benign = y[400:600]
    Xbenign = vstack((X1benign, X2benign))
    ybenign = np.concatenate((y1benign, y2benign))
else:
    scenario = int(scenario)
    try:
        assert scenario in set([1, 2, 3, 5, 6])
    except:
        print "scenario index must be in {1, 2, 3, 5, 6}"
        sys.exit(-1)
    Xbenign = X[(scenario-1)*100:scenario*100,:]
    ybenign = y[(scenario-1)*100:scenario*100]

if attack == "flash":
    Xattack = X[300:400,:]
    yattack = y[300:400]
elif attack == "java":
    Xattack = X[600:700,:]
    yattack = y[600:700]
else:
    print "attack must be flash or java"
    sys.exit(-1)

X = vstack((Xbenign, Xattack))
y = np.concatenate((ybenign, yattack))

print "Running iForest..."
clf = IsolationForest(100, n_jobs=-1)
clf.fit(X)
yhat = -clf.decision_function(X)
print "AP:", average_precision_score(y, yhat),
print "AUC:", roc_auc_score(y, yhat)
