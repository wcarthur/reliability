from reliability.Fitters import Fit_Weibull_2P, Fit_Weibull_3P, Fit_Gamma_2P, Fit_Gamma_3P, Fit_Lognormal_2P, Fit_Lognormal_3P, Fit_Loglogistic_2P, Fit_Loglogistic_3P, Fit_Normal_2P, Fit_Exponential_1P, Fit_Exponential_2P, Fit_Beta_2P, Fit_Gumbel_2P, Fit_Weibull_Mixture, Fit_Weibull_CR, Fit_Everything
from reliability.Distributions import Weibull_Distribution, Gamma_Distribution, Lognormal_Distribution, Loglogistic_Distribution, Normal_Distribution, Exponential_Distribution, Beta_Distribution, Gumbel_Distribution, Mixture_Model, Competing_Risks_Model
from reliability.Other_functions import make_right_censored_data
from numpy.testing import assert_allclose
import warnings

# I would like to make these smaller but the slight differences in different python versions (3.6-3.9) mean that tight tolerances result in test failures
atol = 1e-3
atol_big = 0 # 0 means it will not look at the absolute difference
rtol = 1e-3
rtol_big = 0.1 # 10% variation

def test_Fit_Weibull_2P():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    dist = Weibull_Distribution(alpha=50, beta=2)
    rawdata = dist.random_samples(20, seed=5)
    data = make_right_censored_data(data=rawdata, threshold=dist.mean)

    MLE = Fit_Weibull_2P(failures=data.failures, right_censored=data.right_censored, method='MLE', show_probability_plot=False, print_results=False)
    assert_allclose(MLE.alpha, 45.099010886086354, rtol=rtol, atol=atol)
    assert_allclose(MLE.beta, 2.7827531773597984, rtol=rtol, atol=atol)
    assert_allclose(MLE.gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(MLE.AICc, 115.66971887883678, rtol=rtol, atol=atol)
    assert_allclose(MLE.BIC, 116.95530107300358, rtol=rtol, atol=atol)
    assert_allclose(MLE.loglik, -55.4819182629478, rtol=rtol, atol=atol)
    assert_allclose(MLE.AD, 55.60004028891652, rtol=rtol, atol=atol)
    assert_allclose(MLE.Cov_alpha_beta, -0.9178064889295378, rtol=rtol, atol=atol)

    LS = Fit_Weibull_2P(failures=data.failures, right_censored=data.right_censored, method='LS', show_probability_plot=False, print_results=False)
    assert_allclose(LS.alpha, 42.91333312142757, rtol=rtol, atol=atol)
    assert_allclose(LS.beta, 2.9657153686461033, rtol=rtol, atol=atol)
    assert_allclose(LS.gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(LS.AICc, 115.93668384456019, rtol=rtol, atol=atol)
    assert_allclose(LS.BIC, 117.222266038727, rtol=rtol, atol=atol)
    assert_allclose(LS.loglik, -55.61540074580951, rtol=rtol, atol=atol)
    assert_allclose(LS.AD, 55.62807482958476, rtol=rtol, atol=atol)
    assert_allclose(LS.Cov_alpha_beta, -0.1119680481788733, rtol=rtol, atol=atol)


def test_Fit_Weibull_3P():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    dist = Weibull_Distribution(alpha=50, beta=2, gamma=500)
    rawdata = dist.random_samples(20, seed=5)
    data = make_right_censored_data(data=rawdata, threshold=dist.mean)

    MLE = Fit_Weibull_3P(failures=data.failures, right_censored=data.right_censored, method='MLE', show_probability_plot=False, print_results=False)
    assert_allclose(MLE.alpha, 33.0123537701021, rtol=rtol, atol=atol)
    assert_allclose(MLE.beta, 1.327313848890964, rtol=rtol, atol=atol)
    assert_allclose(MLE.gamma, 513.7220829514334, rtol=rtol, atol=atol)
    assert_allclose(MLE.AICc, 116.5327581203968, rtol=rtol, atol=atol)
    assert_allclose(MLE.BIC, 118.01995494105878, rtol=rtol, atol=atol)
    assert_allclose(MLE.loglik, -54.5163790601984, rtol=rtol, atol=atol)
    assert_allclose(MLE.AD, 55.606805028079016, rtol=rtol, atol=atol)
    assert_allclose(MLE.Cov_alpha_beta, -0.7687781958569139, rtol=rtol, atol=atol)

    LS = Fit_Weibull_3P(failures=data.failures, right_censored=data.right_censored, method='LS', show_probability_plot=False, print_results=False)
    assert_allclose(LS.alpha, 32.639290779819824, rtol=rtol, atol=atol)
    assert_allclose(LS.beta, 1.2701961119432184, rtol=rtol, atol=atol)
    assert_allclose(LS.gamma, 514.5065549826453, rtol=rtol, atol=atol)
    assert_allclose(LS.AICc, 119.47369772704523, rtol=rtol, atol=atol)
    assert_allclose(LS.BIC, 120.96089454770721, rtol=rtol, atol=atol)
    assert_allclose(LS.loglik, -55.98684886352262, rtol=rtol, atol=atol)
    assert_allclose(LS.AD, 55.70853682331155, rtol=rtol, atol=atol)
    assert_allclose(LS.Cov_alpha_beta, -0.8435523816679948, rtol=rtol, atol=atol)


def test_Fit_Gamma_2P():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    dist = Gamma_Distribution(alpha=50, beta=2)
    rawdata = dist.random_samples(20, seed=5)
    data = make_right_censored_data(data=rawdata, threshold=dist.mean)

    MLE = Fit_Gamma_2P(failures=data.failures, right_censored=data.right_censored, method='MLE', show_probability_plot=False, print_results=False)
    assert_allclose(MLE.alpha, 30.895317427895733, rtol=rtol, atol=atol)
    assert_allclose(MLE.beta, 2.5300452519936405, rtol=rtol, atol=atol)
    assert_allclose(MLE.gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(MLE.AICc, 154.33194705093553, rtol=rtol, atol=atol)
    assert_allclose(MLE.BIC, 155.61752924510233, rtol=rtol, atol=atol)
    assert_allclose(MLE.loglik, -74.81303234899717, rtol=rtol, atol=atol)
    assert_allclose(MLE.AD, 38.004356262808585, rtol=rtol, atol=atol)
    assert_allclose(MLE.Cov_alpha_beta, -11.610946543514364, rtol=rtol, atol=atol)

    LS = Fit_Gamma_2P(failures=data.failures, right_censored=data.right_censored, method='LS', show_probability_plot=False, print_results=False)
    assert_allclose(LS.alpha, 25.803340662553182, rtol=rtol, atol=atol)
    assert_allclose(LS.beta, 2.8344248030280284, rtol=rtol, atol=atol)
    assert_allclose(LS.gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(LS.AICc, 154.55898223226797, rtol=rtol, atol=atol)
    assert_allclose(LS.BIC, 155.84456442643477, rtol=rtol, atol=atol)
    assert_allclose(LS.loglik, -74.92654993966339, rtol=rtol, atol=atol)
    assert_allclose(LS.AD, 38.01670664187149, rtol=rtol, atol=atol)
    assert_allclose(LS.Cov_alpha_beta, -5.761109354575602, rtol=rtol, atol=atol)


def test_Fit_Gamma_3P():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    dist = Gamma_Distribution(alpha=50, beta=2, gamma=500)
    rawdata = dist.random_samples(20, seed=5)
    data = make_right_censored_data(data=rawdata, threshold=dist.mean)

    MLE = Fit_Gamma_3P(failures=data.failures, right_censored=data.right_censored, method='MLE', show_probability_plot=False, print_results=False)
    assert_allclose(MLE.alpha, 161.8637212853173, rtol=rtol, atol=atol)
    assert_allclose(MLE.beta, 0.5429184966902371, rtol=rtol, atol=atol)
    assert_allclose(MLE.gamma, 515.4451173341464, rtol=rtol, atol=atol)
    assert_allclose(MLE.AICc, 150.0135606540687, rtol=rtol, atol=atol)
    assert_allclose(MLE.BIC, 151.50075747473068, rtol=rtol, atol=atol)
    assert_allclose(MLE.loglik, -71.25678032703435, rtol=rtol, atol=atol)
    assert_allclose(MLE.AD, 38.63647775048046, rtol=rtol, atol=atol)
    assert_allclose(MLE.Cov_alpha_beta, -11.302538880460721, rtol=rtol, atol=atol)

    LS = Fit_Gamma_3P(failures=data.failures, right_censored=data.right_censored, method='LS', show_probability_plot=False, print_results=False)
    assert_allclose(LS.alpha, 15.52387782496473, rtol=rtol, atol=atol)
    assert_allclose(LS.beta, 6.379102526634475, rtol=rtol, atol=atol)
    assert_allclose(LS.gamma, 471.0728464561921, rtol=rtol, atol=atol)
    assert_allclose(LS.AICc, 158.76750225090194, rtol=rtol, atol=atol)
    assert_allclose(LS.BIC, 160.25469907156392, rtol=rtol, atol=atol)
    assert_allclose(LS.loglik, -75.63375112545097, rtol=rtol, atol=atol)
    assert_allclose(LS.AD, 38.025029148894646, rtol=rtol, atol=atol)
    assert_allclose(LS.Cov_alpha_beta, -5.605059720113306, rtol=rtol, atol=atol)


def test_Fit_Lognormal_2P():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    dist = Lognormal_Distribution(mu=1,sigma=0.5)
    rawdata = dist.random_samples(20, seed=5)
    data = make_right_censored_data(data=rawdata, threshold=dist.mean)

    MLE = Fit_Lognormal_2P(failures=data.failures, right_censored=data.right_censored, method='MLE', show_probability_plot=False, print_results=False)
    assert_allclose(MLE.mu, 0.9494190246173423, rtol=rtol, atol=atol)
    assert_allclose(MLE.sigma, 0.4267323457212804, rtol=rtol, atol=atol)
    assert_allclose(MLE.gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(MLE.AICc, 49.69392320890687, rtol=rtol, atol=atol)
    assert_allclose(MLE.BIC, 50.979505403073674, rtol=rtol, atol=atol)
    assert_allclose(MLE.loglik, -22.494020427982846, rtol=rtol, atol=atol)
    assert_allclose(MLE.AD, 46.91678130009629, rtol=rtol, atol=atol)
    assert_allclose(MLE.Cov_mu_sigma, 0.002505454567167978, rtol=rtol, atol=atol)

    LS = Fit_Lognormal_2P(failures=data.failures, right_censored=data.right_censored, method='LS', show_probability_plot=False, print_results=False)
    assert_allclose(LS.mu, 0.9427890879489974, rtol=rtol, atol=atol)
    assert_allclose(LS.sigma, 0.4475312141445822, rtol=rtol, atol=atol)
    assert_allclose(LS.gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(LS.AICc, 49.757609068995194, rtol=rtol, atol=atol)
    assert_allclose(LS.BIC, 51.043191263162, rtol=rtol, atol=atol)
    assert_allclose(LS.loglik, -22.52586335802701, rtol=rtol, atol=atol)
    assert_allclose(LS.AD, 46.93509652892565, rtol=rtol, atol=atol)
    assert_allclose(LS.Cov_mu_sigma, 0.0025640250120794526, rtol=rtol, atol=atol)


def test_Fit_Lognormal_3P():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    dist = Lognormal_Distribution(mu=1,sigma=0.5, gamma=500)
    rawdata = dist.random_samples(20, seed=5)
    data = make_right_censored_data(data=rawdata, threshold=dist.mean)

    MLE = Fit_Lognormal_3P(failures=data.failures, right_censored=data.right_censored, method='MLE', show_probability_plot=False, print_results=False)
    assert_allclose(MLE.mu, 0.5608879850309877, rtol=rtol, atol=atol)
    assert_allclose(MLE.sigma, 0.7396271168422542, rtol=rtol, atol=atol)
    assert_allclose(MLE.gamma, 500.79568888668746, rtol=rtol, atol=atol)
    assert_allclose(MLE.AICc, 52.067948767151364, rtol=rtol, atol=atol)
    assert_allclose(MLE.BIC, 53.555145587813335, rtol=rtol, atol=atol)
    assert_allclose(MLE.loglik, -22.283974383575682, rtol=rtol, atol=atol)
    assert_allclose(MLE.AD, 46.95299490218758, rtol=rtol, atol=atol)
    assert_allclose(MLE.Cov_mu_sigma, 0.007500058692172027, rtol=rtol, atol=atol)

    LS = Fit_Lognormal_3P(failures=data.failures, right_censored=data.right_censored, method='LS', show_probability_plot=False, print_results=False)
    assert_allclose(LS.mu, 0.976088004545536, rtol=rtol, atol=atol)
    assert_allclose(LS.sigma, 0.4340076639560259, rtol=rtol, atol=atol)
    assert_allclose(LS.gamma, 499.9229609896007, rtol=rtol, atol=atol)
    assert_allclose(LS.AICc, 52.60637160294965, rtol=rtol, atol=atol)
    assert_allclose(LS.BIC, 54.09356842361162, rtol=rtol, atol=atol)
    assert_allclose(LS.loglik, -22.553185801474825, rtol=rtol, atol=atol)
    assert_allclose(LS.AD, 46.93164376455629, rtol=rtol, atol=atol)
    assert_allclose(LS.Cov_mu_sigma, 0.0025619981036203664, rtol=rtol, atol=atol)


def test_Fit_Loglogistic_2P():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    dist = Loglogistic_Distribution(alpha=50, beta=8)
    rawdata = dist.random_samples(200, seed=5)
    data = make_right_censored_data(data=rawdata, threshold=dist.mean)

    MLE = Fit_Loglogistic_2P(failures=data.failures, right_censored=data.right_censored, method='MLE', show_probability_plot=False, print_results=False)
    assert_allclose(MLE.alpha, 50.25178370302894, rtol=rtol, atol=atol)
    assert_allclose(MLE.beta, 7.869851191923439, rtol=rtol, atol=atol)
    assert_allclose(MLE.gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(MLE.AICc, 941.9461734708389, rtol=rtol, atol=atol)
    assert_allclose(MLE.BIC, 948.4818944983512, rtol=rtol, atol=atol)
    assert_allclose(MLE.loglik, -468.94262988262756, rtol=rtol, atol=atol)
    assert_allclose(MLE.AD, 582.5464625675626, rtol=rtol, atol=atol)
    assert_allclose(MLE.Cov_alpha_beta, -0.14731273967044273, rtol=rtol, atol=atol)

    LS = Fit_Loglogistic_2P(failures=data.failures, right_censored=data.right_censored, method='LS', show_probability_plot=False, print_results=False)
    assert_allclose(LS.alpha, 50.657493341191135, rtol=rtol, atol=atol)
    assert_allclose(LS.beta, 7.389285094946194, rtol=rtol, atol=atol)
    assert_allclose(LS.gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(LS.AICc, 942.5623765547977, rtol=rtol, atol=atol)
    assert_allclose(LS.BIC, 949.09809758231, rtol=rtol, atol=atol)
    assert_allclose(LS.loglik, -469.25073142460695, rtol=rtol, atol=atol)
    assert_allclose(LS.AD, 582.5637861880587, rtol=rtol, atol=atol)
    assert_allclose(LS.Cov_alpha_beta, -0.1828511494829605, rtol=rtol, atol=atol)


def test_Fit_Loglogistic_3P():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    dist = Loglogistic_Distribution(alpha=50, beta=8, gamma=500)
    rawdata = dist.random_samples(200, seed=5)
    data = make_right_censored_data(data=rawdata, threshold=dist.mean)

    MLE = Fit_Loglogistic_3P(failures=data.failures, right_censored=data.right_censored, method='MLE', show_probability_plot=False, print_results=False)
    assert_allclose(MLE.alpha, 64.53821169314404, rtol=rtol_big, atol=atol_big)
    assert_allclose(MLE.beta, 10.5120425994396, rtol=rtol_big, atol=atol_big)
    assert_allclose(MLE.gamma, 485.67966960645543, rtol=rtol_big, atol=atol_big)
    assert_allclose(MLE.AICc, 943.8101901503343, rtol=rtol, atol=atol)
    assert_allclose(MLE.BIC, 953.5826932703866, rtol=rtol, atol=atol)
    assert_allclose(MLE.loglik, -468.84387058537123, rtol=rtol, atol=atol)
    assert_allclose(MLE.AD, 582.5422181701142, rtol=rtol, atol=atol)
    assert_allclose(MLE.Cov_alpha_beta, -0.18810779930161473, rtol=rtol, atol=atol)

    LS = Fit_Loglogistic_3P(failures=data.failures, right_censored=data.right_censored, method='LS', show_probability_plot=False, print_results=False)
    assert_allclose(LS.alpha, 62.356306952705054, rtol=rtol, atol=atol)
    assert_allclose(LS.beta, 10.033505691693987, rtol=rtol, atol=atol)
    assert_allclose(LS.gamma, 487.9071761434245, rtol=rtol, atol=atol)
    assert_allclose(LS.AICc, 943.8204940620113, rtol=rtol, atol=atol)
    assert_allclose(LS.BIC, 953.5929971820636, rtol=rtol, atol=atol)
    assert_allclose(LS.loglik, -468.84902254120976, rtol=rtol, atol=atol)
    assert_allclose(LS.AD, 582.5422083314535, rtol=rtol, atol=atol)
    assert_allclose(LS.Cov_alpha_beta, -0.1864715435778476, rtol=rtol, atol=atol)


def test_Fit_Normal_2P():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    dist = Normal_Distribution(mu=50,sigma=8)
    rawdata = dist.random_samples(20, seed=5)
    data = make_right_censored_data(data=rawdata, threshold=dist.mean)
    MLE = Fit_Normal_2P(failures=data.failures, right_censored=data.right_censored,method='MLE', show_probability_plot=False, print_results=False)
    assert_allclose(MLE.mu, 49.01641649924297, rtol=rtol, atol=atol)
    assert_allclose(MLE.sigma, 6.653242350482225, rtol=rtol, atol=atol)
    assert_allclose(MLE.AICc, 91.15205546551952, rtol=rtol, atol=atol)
    assert_allclose(MLE.BIC, 92.43763765968633, rtol=rtol, atol=atol)
    assert_allclose(MLE.loglik, -43.223086556289175, rtol=rtol, atol=atol)
    assert_allclose(MLE.AD, 63.64069171746617, rtol=rtol, atol=atol)
    assert_allclose(MLE.Cov_mu_sigma, 1.0395705891908218, rtol=rtol, atol=atol)

    LS = Fit_Normal_2P(failures=data.failures, right_censored=data.right_censored,method='LS', show_probability_plot=False, print_results=False)
    assert_allclose(LS.mu, 48.90984235374872, rtol=rtol, atol=atol)
    assert_allclose(LS.sigma, 6.990098677785364, rtol=rtol, atol=atol)
    assert_allclose(LS.AICc, 91.21601631804141, rtol=rtol, atol=atol)
    assert_allclose(LS.BIC, 92.50159851220822, rtol=rtol, atol=atol)
    assert_allclose(LS.loglik, -43.25506698255012, rtol=rtol, atol=atol)
    assert_allclose(LS.AD, 63.657853523044515, rtol=rtol, atol=atol)
    assert_allclose(LS.Cov_mu_sigma, 1.0973540350799618, rtol=rtol, atol=atol)


def test_Fit_Gumbel_2P():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    dist = Gumbel_Distribution(mu=50,sigma=8)
    rawdata = dist.random_samples(20, seed=5)
    data = make_right_censored_data(data=rawdata, threshold=dist.mean)

    MLE = Fit_Gumbel_2P(failures=data.failures, right_censored=data.right_censored, method='MLE', show_probability_plot=False, print_results=False)
    assert_allclose(MLE.mu, 47.97813932110471, rtol=rtol, atol=atol)
    assert_allclose(MLE.sigma, 5.487155810067562, rtol=rtol, atol=atol)
    assert_allclose(MLE.AICc, 83.17550426530995, rtol=rtol, atol=atol)
    assert_allclose(MLE.BIC, 84.46108645947676, rtol=rtol, atol=atol)
    assert_allclose(MLE.loglik, -39.23481095618439, rtol=rtol, atol=atol)
    assert_allclose(MLE.AD, 76.43706903015115, rtol=rtol, atol=atol)
    assert_allclose(MLE.Cov_mu_sigma, 1.8549915988421086, rtol=rtol, atol=atol)

    LS = Fit_Gumbel_2P(failures=data.failures, right_censored=data.right_censored, method='LS', show_probability_plot=False, print_results=False)
    assert_allclose(LS.mu, 46.43212585298994, rtol=rtol, atol=atol)
    assert_allclose(LS.sigma, 4.827795060868229, rtol=rtol, atol=atol)
    assert_allclose(LS.AICc, 83.88382894786476, rtol=rtol, atol=atol)
    assert_allclose(LS.BIC, 85.16941114203156, rtol=rtol, atol=atol)
    assert_allclose(LS.loglik, -39.58897329746179, rtol=rtol, atol=atol)
    assert_allclose(LS.AD, 76.44737853267988, rtol=rtol, atol=atol)
    assert_allclose(LS.Cov_mu_sigma, 0.32622575178078633, rtol=rtol, atol=atol)


def test_Fit_Exponential_1P():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    dist = Exponential_Distribution(Lambda=5)
    rawdata = dist.random_samples(20, seed=5)
    data = make_right_censored_data(data=rawdata, threshold=dist.mean)

    MLE = Fit_Exponential_1P(failures=data.failures, right_censored=data.right_censored, method='MLE', show_probability_plot=False, print_results=False)
    assert_allclose(MLE.Lambda, 6.101198944227536, rtol=rtol, atol=atol)
    assert_allclose(MLE.AICc, -22.032339191099148, rtol=rtol, atol=atol)
    assert_allclose(MLE.BIC, -21.25882913976738, rtol=rtol, atol=atol)
    assert_allclose(MLE.loglik, 12.127280706660684, rtol=rtol, atol=atol)
    assert_allclose(MLE.AD, 29.59913306667145, rtol=rtol, atol=atol)

    LS = Fit_Exponential_1P(failures=data.failures, right_censored=data.right_censored, method='LS', show_probability_plot=False, print_results=False)
    assert_allclose(LS.Lambda, 5.776959885774546, rtol=rtol, atol=atol)
    assert_allclose(LS.AICc, -21.988412212242917, rtol=rtol, atol=atol)
    assert_allclose(LS.BIC, -21.214902160911148, rtol=rtol, atol=atol)
    assert_allclose(LS.loglik, 12.10531721723257, rtol=rtol, atol=atol)
    assert_allclose(LS.AD, 29.52124203457833, rtol=rtol, atol=atol)


def test_Fit_Exponential_2P():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    dist = Exponential_Distribution(Lambda=5, gamma=500)
    rawdata = dist.random_samples(20, seed=5)
    data = make_right_censored_data(data=rawdata, threshold=dist.mean)

    MLE = Fit_Exponential_2P(failures=data.failures, right_censored=data.right_censored, method='MLE', show_probability_plot=False, print_results=False)
    assert_allclose(MLE.Lambda, 7.062867654421206, rtol=rtol, atol=atol)
    assert_allclose(MLE.gamma, 500.016737532126, rtol=rtol, atol=atol)
    assert_allclose(MLE.AICc, -23.939665128347745, rtol=rtol, atol=atol)
    assert_allclose(MLE.BIC, -22.65408293418094, rtol=rtol, atol=atol)
    assert_allclose(MLE.loglik, 14.322773740644461, rtol=rtol, atol=atol)
    assert_allclose(MLE.AD, 29.413655089419287, rtol=rtol, atol=atol)

    LS = Fit_Exponential_2P(failures=data.failures, right_censored=data.right_censored, method='LS', show_probability_plot=False, print_results=False)
    assert_allclose(LS.Lambda, 6.4445633542175, rtol=rtol, atol=atol)
    assert_allclose(LS.gamma, 500.01368943066706, rtol=rtol, atol=atol)
    assert_allclose(LS.AICc, -23.031777273560103, rtol=rtol, atol=atol)
    assert_allclose(LS.BIC, -21.7461950793933, rtol=rtol, atol=atol)
    assert_allclose(LS.loglik, 13.86882981325064, rtol=rtol, atol=atol)
    assert_allclose(LS.AD, 29.33840933641424, rtol=rtol, atol=atol)


def test_Fit_Beta_2P():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    dist = Beta_Distribution(alpha=5, beta=4)
    rawdata = dist.random_samples(20, seed=5)
    data = make_right_censored_data(data=rawdata, threshold=dist.mean)

    MLE = Fit_Beta_2P(failures=data.failures, right_censored=data.right_censored, method='MLE', show_probability_plot=False, print_results=False)
    assert_allclose(MLE.alpha, 7.429048118107467, rtol=rtol, atol=atol)
    assert_allclose(MLE.beta, 6.519338516778177, rtol=rtol, atol=atol)
    assert_allclose(MLE.AICc, 4.947836247236739, rtol=rtol, atol=atol)
    assert_allclose(MLE.BIC, 6.233418441403544, rtol=rtol, atol=atol)
    assert_allclose(MLE.loglik, -0.12097694714778129, rtol=rtol, atol=atol)
    assert_allclose(MLE.AD, 63.64510718930826, rtol=rtol, atol=atol)
    assert_allclose(MLE.Cov_alpha_beta, 9.993273704064205, rtol=rtol, atol=atol)

    LS = Fit_Beta_2P(failures=data.failures, right_censored=data.right_censored, method='LS', show_probability_plot=False, print_results=False)
    assert_allclose(LS.alpha, 6.699688942917093, rtol=rtol, atol=atol)
    assert_allclose(LS.beta, 5.9477941734033575, rtol=rtol, atol=atol)
    assert_allclose(LS.AICc, 5.02116420233583, rtol=rtol, atol=atol)
    assert_allclose(LS.BIC, 6.306746396502635, rtol=rtol, atol=atol)
    assert_allclose(LS.loglik, -0.1576409246973265, rtol=rtol, atol=atol)
    assert_allclose(LS.AD, 63.661784208694066, rtol=rtol, atol=atol)
    assert_allclose(LS.Cov_alpha_beta, 8.194012965628652, rtol=rtol, atol=atol)


def test_Fit_Weibull_Mixture():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    d1 = Weibull_Distribution(alpha=10, beta=3)
    d2 = Weibull_Distribution(alpha=40, beta=4)
    dist = Mixture_Model(distributions=[d1, d2], proportions=[0.2, 0.8])
    raw_data = dist.random_samples(100, seed=2)
    data = make_right_censored_data(data=raw_data, threshold=dist.mean)

    MLE = Fit_Weibull_Mixture(failures=data.failures, right_censored=data.right_censored, show_probability_plot=False, print_results=False)
    assert_allclose(MLE.alpha_1, 11.06604639424718, rtol=rtol, atol=atol)
    assert_allclose(MLE.beta_1, 2.735078296796997, rtol=rtol, atol=atol)
    assert_allclose(MLE.alpha_2, 34.325433665495346, rtol=rtol, atol=atol)
    assert_allclose(MLE.beta_2, 7.60238532821206, rtol=rtol, atol=atol)
    assert_allclose(MLE.proportion_1, 0.23640116719132157, rtol=rtol, atol=atol)
    assert_allclose(MLE.proportion_2, 0.7635988328086785, rtol=rtol, atol=atol)
    assert_allclose(MLE.AICc, 471.97390405380236, rtol=rtol, atol=atol)
    assert_allclose(MLE.BIC, 484.3614571114024, rtol=rtol, atol=atol)
    assert_allclose(MLE.loglik, -230.66780309073096, rtol=rtol, atol=atol)
    assert_allclose(MLE.AD, 320.1963544647712, rtol=rtol, atol=atol)


def test_Fit_Weibull_CR():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    d1 = Weibull_Distribution(alpha=50, beta=2)
    d2 = Weibull_Distribution(alpha=40, beta=10)
    CR_model = Competing_Risks_Model(distributions=[d1, d2])
    raw_data = CR_model.random_samples(100, seed=2)
    data = make_right_censored_data(data=raw_data, threshold=40)
    MLE = Fit_Weibull_CR(failures=data.failures, right_censored=data.right_censored, show_probability_plot=False, print_results=False)
    assert_allclose(MLE.alpha_1, 53.05674752263902, rtol=rtol, atol=atol)
    assert_allclose(MLE.beta_1, 1.9411091317375062, rtol=rtol, atol=atol)
    assert_allclose(MLE.alpha_2, 38.026383998212154, rtol=rtol, atol=atol)
    assert_allclose(MLE.beta_2, 9.033349805988692, rtol=rtol, atol=atol)
    assert_allclose(MLE.AICc, 665.5311523940719, rtol=rtol, atol=atol)
    assert_allclose(MLE.BIC, 675.5307805064454, rtol=rtol, atol=atol)
    assert_allclose(MLE.loglik, -328.5550498812465, rtol=rtol, atol=atol)
    assert_allclose(MLE.AD, 34.0918038201449, rtol=rtol, atol=atol)


def test_Fit_Everything():
    # ignores the runtime warning from scipy when the nelder-mean or powell optimizers are used and jac is not required
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    dist = Beta_Distribution(alpha=5, beta=4)
    rawdata = dist.random_samples(200, seed=5)
    data = make_right_censored_data(data=rawdata, threshold=dist.mean)
    MLE = Fit_Everything(failures=data.failures, right_censored=data.right_censored, method='MLE', show_probability_plot=False, show_histogram_plot=False, show_PP_plot=False, show_best_distribution_probability_plot=False, print_results=False)
    LS = Fit_Everything(failures=data.failures, right_censored=data.right_censored, method='LS', show_probability_plot=False, show_histogram_plot=False, show_PP_plot=False, show_best_distribution_probability_plot=False, print_results=False)

    #assert_allclose(MLE.best_distribution.alpha, 0.5796887225805948, rtol=rtol, atol=atol) # best fit here is a Beta distribution
    #assert_allclose(MLE.best_distribution.beta, 4.205258710807067, rtol=rtol, atol=atol)
    assert_allclose(MLE.best_distribution.Lambda, 0.594606648, rtol=rtol, atol=atol)
    assert_allclose(MLE.best_distribution.gamma, 1.0480298137989727e-07, rtol=rtol, atol=atol)

    assert_allclose(MLE.Weibull_2P_alpha, 0.5796887225805948, rtol=rtol, atol=atol)
    assert_allclose(MLE.Weibull_2P_beta, 4.205258710807067, rtol=rtol, atol=atol)
    assert_allclose(MLE.Weibull_2P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(MLE.Weibull_2P_AICc, 22.509958498975394, rtol=rtol, atol=atol)
    assert_allclose(MLE.Weibull_2P_BIC, 29.04567952648771, rtol=rtol, atol=atol)
    assert_allclose(MLE.Weibull_2P_loglik, -9.224522396695818, rtol=rtol, atol=atol)
    assert_allclose(MLE.Weibull_2P_AD, 543.31193295208, rtol=rtol, atol=atol)

    assert_allclose(MLE.Weibull_3P_alpha, 0.5796887225805948, rtol=rtol, atol=atol)
    assert_allclose(MLE.Weibull_3P_beta, 4.205258710807067, rtol=rtol, atol=atol)
    assert_allclose(MLE.Weibull_3P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(MLE.Weibull_3P_AICc, 24.571493772983473, rtol=rtol, atol=atol)
    assert_allclose(MLE.Weibull_3P_BIC, 34.343996893035744, rtol=rtol, atol=atol)
    assert_allclose(MLE.Weibull_3P_loglik, -9.224522396695818, rtol=rtol, atol=atol)
    assert_allclose(MLE.Weibull_3P_AD, 543.31193295208, rtol=rtol, atol=atol)

    assert_allclose(MLE.Gamma_2P_alpha, 0.06343366643685251, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gamma_2P_beta, 8.730724670235508, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gamma_2P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gamma_2P_AICc, 29.72088918292124, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gamma_2P_BIC, 36.25661021043356, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gamma_2P_loglik, -12.829987738668741, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gamma_2P_AD, 543.5598195358288, rtol=rtol, atol=atol)

    assert_allclose(MLE.Gamma_3P_alpha, 0.06343366643685251, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gamma_3P_beta, 8.730724670235508, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gamma_3P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gamma_3P_AICc, 31.78242445692932, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gamma_3P_BIC, 41.55492757698159, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gamma_3P_loglik, -12.829987738668741, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gamma_3P_AD, 543.5598195358288, rtol=rtol, atol=atol)

    assert_allclose(MLE.Loglogistic_2P_alpha, 0.5327695781726263, rtol=rtol, atol=atol)
    assert_allclose(MLE.Loglogistic_2P_beta, 4.959959950671738, rtol=rtol, atol=atol)
    assert_allclose(MLE.Loglogistic_2P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(MLE.Loglogistic_2P_AICc, 26.2468431389576, rtol=rtol, atol=atol)
    assert_allclose(MLE.Loglogistic_2P_BIC, 32.78256416646992, rtol=rtol, atol=atol)
    assert_allclose(MLE.Loglogistic_2P_loglik, -11.092964716686922, rtol=rtol, atol=atol)
    assert_allclose(MLE.Loglogistic_2P_AD, 543.3968941075816, rtol=rtol, atol=atol)

    assert_allclose(MLE.Loglogistic_3P_alpha, 0.5327695781726263, rtol=rtol, atol=atol)
    assert_allclose(MLE.Loglogistic_3P_beta, 4.959959950671738, rtol=rtol, atol=atol)
    assert_allclose(MLE.Loglogistic_3P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(MLE.Loglogistic_3P_AICc, 28.30837841296568, rtol=rtol, atol=atol)
    assert_allclose(MLE.Loglogistic_3P_BIC, 38.08088153301795, rtol=rtol, atol=atol)
    assert_allclose(MLE.Loglogistic_3P_loglik, -11.092964716686922, rtol=rtol, atol=atol)
    assert_allclose(MLE.Loglogistic_3P_AD, 543.3968941075816, rtol=rtol, atol=atol)

    assert_allclose(MLE.Lognormal_2P_mu, -0.6258670209896524, rtol=rtol, atol=atol)
    assert_allclose(MLE.Lognormal_2P_sigma, 0.3859306240146529, rtol=rtol, atol=atol)
    assert_allclose(MLE.Lognormal_2P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(MLE.Lognormal_2P_AICc, 36.58934382876143, rtol=rtol, atol=atol)
    assert_allclose(MLE.Lognormal_2P_BIC, 43.125064856273745, rtol=rtol, atol=atol)
    assert_allclose(MLE.Lognormal_2P_loglik, -16.264215061588835, rtol=rtol, atol=atol)
    assert_allclose(MLE.Lognormal_2P_AD, 543.7578077426027, rtol=rtol, atol=atol)

    assert_allclose(MLE.Lognormal_3P_mu, -0.6258670209896524, rtol=rtol, atol=atol)
    assert_allclose(MLE.Lognormal_3P_sigma, 0.3859306240146529, rtol=rtol, atol=atol)
    assert_allclose(MLE.Lognormal_3P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(MLE.Lognormal_3P_AICc, 38.65087910276951, rtol=rtol, atol=atol)
    assert_allclose(MLE.Lognormal_3P_BIC, 48.42338222282178, rtol=rtol, atol=atol)
    assert_allclose(MLE.Lognormal_3P_loglik, -16.264215061588835, rtol=rtol, atol=atol)
    assert_allclose(MLE.Lognormal_3P_AD, 543.7578077426027, rtol=rtol, atol=atol)

    assert_allclose(MLE.Normal_2P_mu, 0.5313204293962966, rtol=rtol, atol=atol)
    assert_allclose(MLE.Normal_2P_sigma, 0.14842166096827056, rtol=rtol, atol=atol)
    assert_allclose(MLE.Normal_2P_AICc, 23.0363966340782, rtol=rtol, atol=atol)
    assert_allclose(MLE.Normal_2P_BIC, 29.572117661590518, rtol=rtol, atol=atol)
    assert_allclose(MLE.Normal_2P_loglik, -9.487741464247222, rtol=rtol, atol=atol)
    assert_allclose(MLE.Normal_2P_AD, 543.3042437249142, rtol=rtol, atol=atol)

    assert_allclose(MLE.Gumbel_2P_mu, 0.5706624792367315, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gumbel_2P_sigma, 0.10182903954122995, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gumbel_2P_AICc, 26.09054970134011, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gumbel_2P_BIC, 32.626270728852425, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gumbel_2P_loglik, -11.014817997878176, rtol=rtol, atol=atol)
    assert_allclose(MLE.Gumbel_2P_AD, 543.3089024789034, rtol=rtol, atol=atol)

    assert_allclose(MLE.Beta_2P_alpha, 5.586642953718748, rtol=rtol, atol=atol)
    assert_allclose(MLE.Beta_2P_beta, 4.950693419749502, rtol=rtol, atol=atol)
    assert_allclose(MLE.Beta_2P_AICc, 24.204124482547897, rtol=rtol, atol=atol)
    assert_allclose(MLE.Beta_2P_BIC, 30.739845510060213, rtol=rtol, atol=atol)
    assert_allclose(MLE.Beta_2P_loglik, -10.07160538848207, rtol=rtol, atol=atol)
    assert_allclose(MLE.Beta_2P_AD, 543.3809275359781, rtol=rtol, atol=atol)

    assert_allclose(MLE.Exponential_2P_lambda, 1.5845505775713558, rtol=rtol, atol=atol)
    assert_allclose(MLE.Exponential_2P_gamma, 0.12428161981215716, rtol=rtol, atol=atol)
    assert_allclose(MLE.Exponential_2P_AICc, 127.11230931613672, rtol=rtol, atol=atol)
    assert_allclose(MLE.Exponential_2P_BIC, 133.64803034364903, rtol=rtol, atol=atol)
    assert_allclose(MLE.Exponential_2P_loglik, -61.52569780527648, rtol=rtol, atol=atol)
    assert_allclose(MLE.Exponential_2P_AD, 548.8966650502098, rtol=rtol, atol=atol)

    assert_allclose(MLE.Exponential_1P_lambda, 1.1776736956890317, rtol=rtol, atol=atol)
    assert_allclose(MLE.Exponential_1P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(MLE.Exponential_1P_AICc, 192.73284561137785, rtol=rtol, atol=atol)
    assert_allclose(MLE.Exponential_1P_BIC, 196.01096095772388, rtol=rtol, atol=atol)
    assert_allclose(MLE.Exponential_1P_loglik, -95.35632179558792, rtol=rtol, atol=atol)
    assert_allclose(MLE.Exponential_1P_AD, 551.326873807673, rtol=rtol, atol=atol)

    assert_allclose(MLE.GeneralizedPareto_3P_lambda, 0.59460664857, rtol=rtol, atol=atol)
    assert_allclose(MLE.GeneralizedPareto_3P_gamma, 1.0480298137989727e-7, rtol=rtol, atol=atol)

    #assert_allclose(LS.best_distribution.mu, 0.5350756091376212, rtol=rtol, atol=atol) # best fit here is a Normal distribution
    #assert_allclose(LS.best_distribution.sigma, 0.15352298167936318, rtol=rtol, atol=atol)

    assert_allclose(LS.best_distribution.Lambda, 1.0, rtol=rtol, atol=atol)
    assert_allclose(LS.best_distribution.gamma, 0.0, rtol=rtol, atol=atol)

    assert_allclose(LS.Weibull_2P_alpha, 0.5948490848650297, rtol=rtol, atol=atol)
    assert_allclose(LS.Weibull_2P_beta, 3.850985192722524, rtol=rtol, atol=atol)
    assert_allclose(LS.Weibull_2P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(LS.Weibull_2P_AICc, 24.002343535956285, rtol=rtol, atol=atol)
    assert_allclose(LS.Weibull_2P_BIC, 30.538064563468602, rtol=rtol, atol=atol)
    assert_allclose(LS.Weibull_2P_loglik, -9.970714915186264, rtol=rtol, atol=atol)
    assert_allclose(LS.Weibull_2P_AD, 543.3536598333712, rtol=rtol, atol=atol)

    assert_allclose(LS.Weibull_3P_alpha, 0.5796887225805948, rtol=rtol, atol=atol)
    assert_allclose(LS.Weibull_3P_beta, 4.205258710807067, rtol=rtol, atol=atol)
    assert_allclose(LS.Weibull_3P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(LS.Weibull_3P_AICc, 24.571493772983473, rtol=rtol, atol=atol)
    assert_allclose(LS.Weibull_3P_BIC, 34.343996893035744, rtol=rtol, atol=atol)
    assert_allclose(LS.Weibull_3P_loglik, -9.224522396695818, rtol=rtol, atol=atol)
    assert_allclose(LS.Weibull_3P_AD, 543.31193295208, rtol=rtol, atol=atol)

    assert_allclose(LS.Gamma_2P_alpha, 0.047474493713487956, rtol=rtol, atol=atol)
    assert_allclose(LS.Gamma_2P_beta, 11.56120649983023, rtol=rtol, atol=atol)
    assert_allclose(LS.Gamma_2P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(LS.Gamma_2P_AICc, 34.77520772749797, rtol=rtol, atol=atol)
    assert_allclose(LS.Gamma_2P_BIC, 41.31092875501029, rtol=rtol, atol=atol)
    assert_allclose(LS.Gamma_2P_loglik, -15.357147010957107, rtol=rtol, atol=atol)
    assert_allclose(LS.Gamma_2P_AD, 543.5555679280225, rtol=rtol, atol=atol)

    assert_allclose(LS.Gamma_3P_alpha, 0.06343366643685251, rtol=rtol, atol=atol)
    assert_allclose(LS.Gamma_3P_beta, 8.730724670235508, rtol=rtol, atol=atol)
    assert_allclose(LS.Gamma_3P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(LS.Gamma_3P_AICc, 31.78242445692932, rtol=rtol, atol=atol)
    assert_allclose(LS.Gamma_3P_BIC, 41.55492757698159, rtol=rtol, atol=atol)
    assert_allclose(LS.Gamma_3P_loglik, -12.829987738668741, rtol=rtol, atol=atol)
    assert_allclose(LS.Gamma_3P_AD, 543.5598195358288, rtol=rtol, atol=atol)

    assert_allclose(LS.Loglogistic_2P_alpha, 0.5489258630949324, rtol=rtol, atol=atol)
    assert_allclose(LS.Loglogistic_2P_beta, 4.282869717868545, rtol=rtol, atol=atol)
    assert_allclose(LS.Loglogistic_2P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(LS.Loglogistic_2P_AICc, 29.55884374185365, rtol=rtol, atol=atol)
    assert_allclose(LS.Loglogistic_2P_BIC, 36.09456476936597, rtol=rtol, atol=atol)
    assert_allclose(LS.Loglogistic_2P_loglik, -12.748965018134946, rtol=rtol, atol=atol)
    assert_allclose(LS.Loglogistic_2P_AD, 543.4725652046802, rtol=rtol, atol=atol)

    assert_allclose(LS.Loglogistic_3P_alpha, 0.5327695781726263, rtol=rtol, atol=atol)
    assert_allclose(LS.Loglogistic_3P_beta, 4.959959950671738, rtol=rtol, atol=atol)
    assert_allclose(LS.Loglogistic_3P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(LS.Loglogistic_3P_AICc, 28.30837841296568, rtol=rtol, atol=atol)
    assert_allclose(LS.Loglogistic_3P_BIC, 38.08088153301795, rtol=rtol, atol=atol)
    assert_allclose(LS.Loglogistic_3P_loglik, -11.092964716686922, rtol=rtol, atol=atol)
    assert_allclose(LS.Loglogistic_3P_AD, 543.3968941075816, rtol=rtol, atol=atol)

    assert_allclose(LS.Lognormal_2P_mu, -0.5829545855241497, rtol=rtol, atol=atol)
    assert_allclose(LS.Lognormal_2P_sigma, 0.42938026719038264, rtol=rtol, atol=atol)
    assert_allclose(LS.Lognormal_2P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(LS.Lognormal_2P_AICc, 39.2494098877054, rtol=rtol, atol=atol)
    assert_allclose(LS.Lognormal_2P_BIC, 45.785130915217714, rtol=rtol, atol=atol)
    assert_allclose(LS.Lognormal_2P_loglik, -17.59424809106082, rtol=rtol, atol=atol)
    assert_allclose(LS.Lognormal_2P_AD, 543.6895545238489, rtol=rtol, atol=atol)

    assert_allclose(LS.Lognormal_3P_mu, -0.6258670209896524, rtol=rtol, atol=atol)
    assert_allclose(LS.Lognormal_3P_sigma, 0.3859306240146529, rtol=rtol, atol=atol)
    assert_allclose(LS.Lognormal_3P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(LS.Lognormal_3P_AICc, 38.65087910276951, rtol=rtol, atol=atol)
    assert_allclose(LS.Lognormal_3P_BIC, 48.42338222282178, rtol=rtol, atol=atol)
    assert_allclose(LS.Lognormal_3P_loglik, -16.264215061588835, rtol=rtol, atol=atol)
    assert_allclose(LS.Lognormal_3P_AD, 543.7578077426027, rtol=rtol, atol=atol)

    assert_allclose(LS.Normal_2P_mu, 0.5350756091376212, rtol=rtol, atol=atol)
    assert_allclose(LS.Normal_2P_sigma, 0.15352298167936318, rtol=rtol, atol=atol)
    assert_allclose(LS.Normal_2P_AICc, 23.270071653194492, rtol=rtol, atol=atol)
    assert_allclose(LS.Normal_2P_BIC, 29.80579268070681, rtol=rtol, atol=atol)
    assert_allclose(LS.Normal_2P_loglik, -9.604578973805367, rtol=rtol, atol=atol)
    assert_allclose(LS.Normal_2P_AD, 543.3018089629097, rtol=rtol, atol=atol)

    assert_allclose(LS.Gumbel_2P_mu, 0.5575543755580943, rtol=rtol, atol=atol)
    assert_allclose(LS.Gumbel_2P_sigma, 0.09267958281580514, rtol=rtol, atol=atol)
    assert_allclose(LS.Gumbel_2P_AICc, 28.66352107358925, rtol=rtol, atol=atol)
    assert_allclose(LS.Gumbel_2P_BIC, 35.19924210110157, rtol=rtol, atol=atol)
    assert_allclose(LS.Gumbel_2P_loglik, -12.301303684002747, rtol=rtol, atol=atol)
    assert_allclose(LS.Gumbel_2P_AD, 543.3456378838292, rtol=rtol, atol=atol)

    assert_allclose(LS.Beta_2P_alpha, 6.54242621734743, rtol=rtol, atol=atol)
    assert_allclose(LS.Beta_2P_beta, 5.795236872686599, rtol=rtol, atol=atol)
    assert_allclose(LS.Beta_2P_AICc, 25.745158997195162, rtol=rtol, atol=atol)
    assert_allclose(LS.Beta_2P_BIC, 32.28088002470748, rtol=rtol, atol=atol)
    assert_allclose(LS.Beta_2P_loglik, -10.842122645805702, rtol=rtol, atol=atol)
    assert_allclose(LS.Beta_2P_AD, 543.3718252593867, rtol=rtol, atol=atol)

    assert_allclose(LS.Exponential_2P_lambda, 1.1858797968873822, rtol=rtol, atol=atol)
    assert_allclose(LS.Exponential_2P_gamma, 0.12338161981215715, rtol=rtol, atol=atol)
    assert_allclose(LS.Exponential_2P_AICc, 136.25275877909922, rtol=rtol, atol=atol)
    assert_allclose(LS.Exponential_2P_BIC, 142.78847980661155, rtol=rtol, atol=atol)
    assert_allclose(LS.Exponential_2P_loglik, -66.09592253675774, rtol=rtol, atol=atol)
    assert_allclose(LS.Exponential_2P_AD, 546.5849877012892, rtol=rtol, atol=atol)

    assert_allclose(LS.Exponential_1P_lambda, 1.0678223705385204, rtol=rtol, atol=atol)
    assert_allclose(LS.Exponential_1P_gamma, 0, rtol=rtol, atol=atol)
    assert_allclose(LS.Exponential_1P_AICc, 193.7910857336068, rtol=rtol, atol=atol)
    assert_allclose(LS.Exponential_1P_BIC, 197.06920107995282, rtol=rtol, atol=atol)
    assert_allclose(LS.Exponential_1P_loglik, -95.88544185670239, rtol=rtol, atol=atol)
    assert_allclose(LS.Exponential_1P_AD, 549.85986679373, rtol=rtol, atol=atol)

    assert_allclose(LS.GeneralizedPareto_3P_lambda, 1.0, rtol=rtol, atol=atol)
    assert_allclose(LS.GeneralizedPareto_3P_gamma, 0.0, rtol=rtol, atol=atol)
    assert_allclose(LS.GeneralizedPareto_3P_xi, 0.1, rtol=rtol, atol=atol)
