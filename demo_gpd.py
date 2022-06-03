from reliability.Distributions import GeneralizedPareto_Distribution
from reliability.Fitters import Fit_GeneralizedPareto_3P
from reliability.Probability_plotting import plot_points
import matplotlib.pyplot as plt


dist = GeneralizedPareto_Distribution(Lambda=30, gamma=0.0, xi=0.38)  # creates the distribution object
#plt.subplot(321)
#dist.PDF()

data = dist.random_samples(100, seed=42)  # draws 20 samples from the distribution. Seeded for repeatability
plt.subplot(221)
fit = Fit_GeneralizedPareto_3P(failures=data)  # fits a GeneralizedPareto distribution to the data and generates the probability plot
plt.subplot(222)
fit.distribution.SF(label='fitted distribution')  # uses the distribution object from Fit_GeneralisedPareto_3P and plots the survival function
dist.SF(label='original distribution', linestyle='--') # plots the survival function of the original distribution
plot_points(failures=data, func='SF')  # overlays the original data on the survival function
plt.subplot(223)
fit.distribution.HF(label='fitted distribution')
dist.HF(label='original distribution', linestyle='--') # plots the survival function of the original distribution
plot_points(failures=data, func='HF')  # 
plt.legend()
plt.subplot(224)
fit.distribution.CHF(label='fitted distribution')
dist.CHF(label="original distribution", CI=0.99, plot_CI=True, linestyle='--', CI_type="T")
plot_points(failures=data, func='CHF')
plt.show()

