import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 




# def permutation(statistic, error):


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	d_old= df.values[:,0]
	df_nona=df.dropna()
	d_new= df_nona.values[:,1]

	sns_hist_old=sns.distplot(d_old, bins=20, kde=False, rug=True).get_figur()
	axes = plt.gca()
	axes.set_xlabel('Old Vehicles')
	axes.set_ylabel('vehicles count')

	sns_hist_new = sns.distplot(d_new, bins=20,kde=False, rug=True).get_figur()
	axes = plt.gca()
	axes.set_xlabel('New Vehicles')
	axes.set_ylabel('vehicles count')

	sns_hist_old.savefig("hist_new.png", bbox_inches='tight')
	sns_hist_old.savefig("hist_new.pdf", bbox_inches='tight')


	# sns_plot.axes[0,0].set_ylim(0,)
	# sns_plot.axes[0,0].set_xlim(0,)
    #
	# sns_plot.savefig("scaterplot.png",bbox_inches='tight')
	# sns_plot.savefig("scaterplot.pdf",bbox_inches='tight')
    #
	# data = df.values.T[1]
	#
	# print((("Mean: %f")%(np.mean(data))))
	# print((("Median: %f")%(np.median(data))))
	# print((("Var: %f")%(np.var(data))))
	# print((("std: %f")%(np.std(data))))
	# print((("MAD: %f")%(mad(data))))
    #
	# plt.clf()
	# sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()
    #
	# axes = plt.gca()
	# axes.set_xlabel('Millons of pounds in sales')
	# axes.set_ylabel('Sales count')
    #
	# sns_plot2.savefig("histogram.png",bbox_inches='tight')
	# sns_plot2.savefig("histogram.pdf",bbox_inches='tight')
    #

	