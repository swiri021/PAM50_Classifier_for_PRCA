# PAM50 Classifier for Prostate Cancer.
This classifier is based on Zhao el al on JAMA for the microarray data, and if you have error or question for this code, let me know.(NOT PAPER)

# Reference
[Associations of Luminal and Basal Subtyping of Prostate Cancer With Prognosis and Response to Androgen Deprivation Therapy](http://jamanetwork.com/journals/jamaoncology/article-abstract/2626510)

# Example
```Python
import pandas as pd
from cls.PAM50_classifier import PAM50_CLS

df = pd.read_csv('cls/dataset/example_expr.csv', index_col=0)
pam50 = PAM50_CLS(df, score_softmax=True)

print pam50.pam50_result ### Predict result
print pam50.pam50_score ### Decision score of predict result

```
