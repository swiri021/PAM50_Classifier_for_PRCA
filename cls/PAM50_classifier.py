import pandas as pd
import numpy as np
from scipy import stats

class PAM50_CLS:

	def _calculator(self, *argv):
		sample = argv[0]
		centroid = argv[1]
		label = argv[2]

		corr_result = [stats.spearmanr(sample, sub, nan_policy='omit')[0] for sub in centroid]

		# Is it necessary ?, Adjustment of part for flipping negative value to positive value(NOT abs, because it is rho)
		if self.score_softmax==True:
			corr_result = [x + abs(min(corr_result)) for x in corr_result]

		temp_max = max(corr_result)
		cl = label[corr_result.index(temp_max)]

		return cl, corr_result

	def classifier_1(self, df, centroids):

		### Softmax Function
		def softmax(x):
			return np.exp(x) / np.sum(np.exp(x), axis=0)

		classifier_label = centroids.columns.tolist()
		gene_order = centroids.index.tolist()
		centroids = [centroids[x].values.tolist() for x in centroids.columns.tolist()]

		cl_result = []
		cl_score = []
		df = df.loc[gene_order]

		### Spearman Correlation to get max(correlation), and assign class of maximum rho.
		for x in df.columns.tolist():
			sample = df[x].values.tolist()
			predicted_result, predicted_score = self._calculator(sample, centroids, classifier_label)
			cl_result.append(predicted_result)
			cl_score.append(predicted_score)

		result_df = pd.DataFrame(data=cl_result, index=df.columns.tolist(), columns = ['PAM50'])
		result_score = pd.DataFrame(data=cl_score, index=df.columns.tolist(), columns = classifier_label)

		if self.score_softmax==True:
			result_score = result_score.apply(softmax, axis=1)

		return result_df, result_score

	def __init__(self, df, score_softmax=True):
		df.index = df.index.map(int).map(str)
		self.score_softmax = score_softmax

		### Load Centroid
		_parker_centroid = pd.read_csv('cls/dataset/pam50_centroid.tsv', sep='\t', index_col=0)
		_parker_centroid.index = _parker_centroid.index.map(int)
		_parker_centroid.index = _parker_centroid.index.map(str)

		### Call Classfier
		self.pam50_result, self.pam50_score = self.classifier_1(df, _parker_centroid)