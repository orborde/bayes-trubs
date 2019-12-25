# bayes-trubs
https://a-point-in-tumblspace.tumblr.com/post/189588000957/bayes-trubs-part-1

> There are circumstances (which might only occur with infinitesimal probability, which would be a relief) under which a perfect Bayesian reasoner with an accurate model and reasonable priors – that is to say, somebody doing everything right – will become more and more convinced of a very wrong conclusion, approaching certainty as they gather more data.

That's pretty scary! This repo is a Monte Carlo simulation which attempts to implement a Bayesian reasoner coming to arbitrarily wrong conclusions (whatever that means) about the value of theta.

# Running it

```./bayes-trubs.py```

and then press any key in the plot window.

You're looking at a plot of the posterior distribution. Each time you press a key, you'll sample another datapoint from the real distribution (parameter θ=1/4) and graph the updated posterior.
