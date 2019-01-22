import pandas as pd
from cls.PAM50_classifier import PAM50_CLS

df = pd.read_csv('dataset/example_expr.csv', index_col=0)
pam50 = PAM50_CLS(df, score_softmax=True)

print pam50.pam50_result ### Predict result
print pam50.pam50_score ### Decision score of predict result