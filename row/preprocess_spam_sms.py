#!/usr/bin/env python

import numpy as np
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.datasets import dump_svmlight_file

messages = []
labels = []

with open("SMSSpamCollection", "r") as f:
    for line in f:
        fields = line.strip().split("\t")
        ham_or_spam = fields[0]
        message = fields[1]

        if ham_or_spam == "ham":
            label = 0
        else:
            label = 1

        messages.append(message)
        labels.append(label)

count_vectorizer = CountVectorizer(strip_accents='unicode', stop_words='english')
counts = count_vectorizer.fit_transform(messages)
labels = np.array(labels)
print "Data shape:", counts.shape

dump_svmlight_file(counts, labels, "spam-sms")
