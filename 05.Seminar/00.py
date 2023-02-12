from scipy import stats as stats
x = [1, 2, 3]
y = [4, 5, 6]
statistic, p_value = stats.pearsonr(x, y)
print(type(stats.pearsonr(x, y)))
#print(statistic, p_value)
