import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

 #Bootstrap

def boostrap(statistic_func, iterations, data):
        samples = np.random.choice(data, replace=True, size=[iterations, len(data)])
        # print samples.shape
        data_mean = data.mean()
        vals = []
        for sample in samples:
            sta = statistic_func(sample)
            # print sta
            vals.append(sta)
        b = np.array(vals)
        # print b
        lower, upper = np.percentile(b, [2.5, 97.5])
        return data_mean, lower, upper


if __name__ == "__main__":
        # print df.columns
        df=pd.read_csv('./vehicles.csv')
        df_nona = df.dropna()
        data = df_nona.values[:, 1]
        boots = []
        for i in range(100, 100000, 1000):
            print(i)
            boot = boostrap(np.std, i, data)
            boots.append([i, boot[0], "std"])
            boots.append([i, boot[1], "lower"])
            boots.append([i, boot[2], "upper"])

        df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Std', "Value"])
        sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

        sns_plot.axes[0, 0].set_ylim(0, )
        sns_plot.axes[0, 0].set_xlim(0, 100000)

        sns_plot.savefig("bootstrapproposed_confidence.png", bbox_inches='tight')
        sns_plot.savefig("bootstrapproposed_confidence.pdf", bbox_inches='tight')
