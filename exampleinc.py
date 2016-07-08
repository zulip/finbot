#!/usr/bin/python
from money import *

c = Company("Example Inc")
c.add_flow(FixedCost("Initial Cash", -500000))
c.add_flow(FixedCost("Incorporation", 500))
c.add_flow(ConstantCost("Office", 50000))
c.add_flow(PeriodicCost("Subscription", 4000, "2012-01-05", 14))
c.add_flow(DelayedCost("2012-02-01", ConstantCost("Office", 50000)))
c.add_flow(DelayedCost("2012-02-01", FixedCost("Financing", 50000)))
c.add_flow(SemiMonthlyCost("Payroll", 4000, "2012-01-01"))
c.add_flow(SemiMonthlyWages("Payroll", 6000, "2012-01-01"))

print(c)
c.cash_monthly_summary("2012-01-01", "2013-07-01")
