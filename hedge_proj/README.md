Hedge Project
==========

## What is it

**Hedging** is an important aspect of portfolio management. Portfolio 
managers are often required to stay within risk limits; for example, 
they cannot let their volatility be to high or value-at-risk so low. 
Also, there are times when market conditions lead them to reduce the 
risk of their portfolio. Hedging is the primary mechanism through which 
they carry out these tasks. This project provie several ideas about how to 
hedging, different ways to hedging(minimun variance, VaR, CVaR, etc.), and 
the performance of hedging. 

## the Basic Hedge Equation
<div align="center">
  <img src="https://github.com/bjd1111/Finance/blob/master/hedge_proj/doc/formula.gif"><br>
</div>



## Main Features
Here are just a few of the things that this project provide:

  - Gathering data from google finance(or fred, if specified)
  - Portfolio returns overview
  - Caculate hedge ratio(weights for hedge securities) using different method(minimun variance, VaR, CVaR) under different lambda(           weights control of whole hedge securities)
  - Perfomance analysis for different method (sharp ratio, cumulative return, variance)
  
## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/bjd1111/Finance/tree/master/hedge_proj


```sh
git clone https://github.com/bjd1111/Finance/tree/master/hedge_proj
```

## Documentation
The official documentation is hosted on PyData.org: https://pandas.pydata.org/pandas-docs/stable

The Sphinx documentation should provide a good starting point for learning how
to use the library. Expect the docs to continue to expand as time goes on.

## Background
Work on ``pandas`` started at AQR (a quantitative hedge fund) in 2008 and
has been under active development since then.

## Getting Help

For usage questions, the best place to go to is [StackOverflow](https://stackoverflow.com/questions/tagged/pandas).
Further, general questions and discussions can also take place on the [pydata mailing list](https://groups.google.com/forum/?fromgroups#!forum/pydata).

## Discussion and Development
Most development discussion is taking place on github in this repo. Further, the [pandas-dev mailing list](https://mail.python.org/mailman/listinfo/pandas-dev) can also be used for specialized discussions or design issues, and a [Gitter channel](https://gitter.im/pydata/pandas) is available for quick development related questions.

## Contributing to pandas
All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.

A detailed overview on how to contribute can be found in the **[contributing guide.](https://pandas.pydata.org/pandas-docs/stable/contributing.html)**

If you are simply looking to start working with the pandas codebase, navigate to the [GitHub “issues” tab](https://github.com/pandas-dev/pandas/issues) and start looking through interesting issues. There are a number of issues listed under [Docs](https://github.com/pandas-dev/pandas/issues?labels=Docs&sort=updated&state=open) and [Difficulty Novice](https://github.com/pandas-dev/pandas/issues?q=is%3Aopen+is%3Aissue+label%3A%22Difficulty+Novice%22) where you could start out.

Or maybe through using pandas you have an idea of your own or are looking for something in the documentation and thinking ‘this can be improved’...you can do something about it!

Feel free to ask questions on the [mailing list](https://groups.google.com/forum/?fromgroups#!forum/pydata) or on [Gitter](https://gitter.im/pydata/pandas).
