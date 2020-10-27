# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:00:37 2020

@author: Chetan
"""

import numpy as np
import pandas as pd
import scipy 
import statsmodels.api as ap
ratio = pd.read_csv("C:\\Users\\ADMIN\\Desktop\\chetan\\assignment\\hypothesis\\BuyerRatio.csv")
ratio.insert(0,"index",[0,1])
ratio_1 = ratio.drop(["Observed Values"],axis=1)
Chisquares_results=scipy.stats.chi2_contingency(ratio_1)
Chisquares_results
Chi_square=[['ratio','Test Statistic','p-value'],['Sample Data',Chisquares_results[0],Chisquares_results[1]]]
Chi_square
