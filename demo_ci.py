from reliability.Fitters import Fit_GeneralizedPareto_3P
import matplotlib.pyplot as plt

data = [43, 81, 41, 44, 52, 99, 64, 25, 41, 77, 95, 7]
fit = Fit_GeneralizedPareto_3P(failures=data, show_probability_plot=False, print_results=False)

plt.figure(figsize=(10,4))

plt.subplot(131)
fit.distribution.CDF(CI_type='time',label='time')
fit.distribution.CDF(CI_type='reliability',label='reliability')
plt.title('CDF')
plt.legend()

plt.subplot(132)
fit.distribution.SF(CI_type='time',label='time')
fit.distribution.SF(CI_type='reliability',label='reliability')
plt.title('SF')
plt.legend()

plt.subplot(133)
fit.distribution.CHF(CI_type='time',label='time')
fit.distribution.CHF(CI_type='reliability',label='reliability')
plt.title('CHF')
plt.legend()

plt.tight_layout()
plt.show()