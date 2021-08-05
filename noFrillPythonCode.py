import numpy as np
import scipy.optimize as opt

# Compound interest formula with fees
def simulateYear(principal,claimingEvents,apy,fee):
    firstTerm = principal-fee/apy*claimingEvents
    secondTerm = (1+apy/claimingEvents)**claimingEvents
    thirdTerm = fee/apy*claimingEvents
    result = firstTerm*secondTerm+thirdTerm
    return result

# Parameters for your specific coin
principal = 5.6
apy = 0.1
fee = 0.004
minimumDeltaT=fee/(principal*apy/365)
maximumClaimingEvents = 365/minimumDeltaT

# Solve for the maximum
neg_simulateYear = lambda claimingEvents: -1*simulateYear(principal,claimingEvents,apy,fee)
bounded_o = opt.minimize_scalar(neg_simulateYear,bounds=[0.1,maximumClaimingEvents],method="bounded")

# Print Answer
print("The ideal number of reinvesting events per year is:", bounded_o.x)
