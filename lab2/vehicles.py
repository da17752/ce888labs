
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
    d_current= df.values[:,0]
    df_nona=df. dropna()
    d_proposed= df_nona.values[:,1]



    #HISTOGRAM
    sns_hist_current=sns.distplot(d_current, bins=20, kde=False, rug=True).get_figure()
    axes = plt.gca()
    axes.set_xlabel('Current Vehicles')
    axes.set_ylabel('Vehicles count')

    sns_hist_current.savefig("hist_current.png", bbox_inches='tight')
    sns_hist_current.savefig("hist_current.pdf", bbox_inches='tight')



    sns_hist_proposed = sns.distplot(d_proposed, bins=20,kde= False, rug=True).get_figure()
    axes = plt.gca()
    axes.set_xlabel('Proposed Vehicles')
    axes.set_ylabel('Vehicles count')

    sns_hist_proposed.savefig("hist_proposed.png", bbox_inches='tight')
    sns_hist_proposed.savefig("hist_proposed.pdf", bbox_inches='tight')

    #SCATER PLOT

    datee = [x + 1 for x in range(249)]
    # print(np.shape(datee))

    sns_plot=sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)
    sns_plot.axes[0,0].set_ylim(0,)
    sns_plot.axes[0,0].set_xlim(0,)

    sns_plot.savefig("scaterplotfleet.png",bbox_inches='tight')
    sns_plot.savefig("scaterplotfleet.pdf",bbox_inches='tight')

    plt.clf()

    # standard deviation

    d_current.std()
    d_proposed.std()




        # print ("Mean: %f")%(np.mean(data))
        # print ("Var: %f")%(np.var(data))





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

