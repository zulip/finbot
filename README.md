Finbot is a python program for doing a company's financial
projections.  It models expenses, and has code to handle things like
taxes, payroll periods, etc. that are common for companies and
important to model correctly.

For a usage example, create a file similar to
[exampleinc.py](https://github.com/zulip/finbot/blob/master/exampleinc.py).
It produces output showing the amount of money the company has left
each month, like the following:

```
$ ./exampleinc.py
2012-01-01 00:00:00 495212.13
2012-02-01 00:00:00 424389.8
2012-03-01 00:00:00 395868.84
2012-04-01 00:00:00 370799.94
2012-05-01 00:00:00 346005.02
2012-06-01 00:00:00 320936.11
2012-07-01 00:00:00 296141.19
2012-08-01 00:00:00 271072.29
2012-09-01 00:00:00 242003.39
2012-10-01 00:00:00 217208.46
2012-11-01 00:00:00 192139.56
2012-12-01 00:00:00 167344.63
2013-01-01 00:00:00 142275.73
2013-02-01 00:00:00 113206.83
2013-03-01 00:00:00 88959.84
2013-04-01 00:00:00 63890.94
2013-05-01 00:00:00 39096.02
2013-06-01 00:00:00 14027.11
2013-07-01 00:00:00 -10767.81
```

There is a very simple test suite you can run via `python money.py`.

Contributions of all forms are welcome!

Finbot is licensed under the Apache license.
