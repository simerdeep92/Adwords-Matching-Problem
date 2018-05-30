# Adwords-Matching-Problem
We are given a set of advertisers each of whom have a daily budget Bi . When a user
performs a query, an ad request is placed online and a group of advertisers can then bid for that
advertisement slot. The bid of advertiser i for ad request q is denoted as bi q. We assume that the
bids are small with respect to the daily budgets of the advertisers (i.e, for each i and q, b iq << Bi ) .
Moreover, each advertisement slot can be allocated to at most one advertiser and the advertiser
is charged his bid from his budget. The objective is to maximize the amount of money received
from the advertisers.
For this project, we make the following simplifying assumptions:
1. For the optimal matching (used for calculating the competitive ratio), assume that
everyone’s budget is completely used.
2. The bid values are fixed (unlike in the real world where advertisers normally compete by
incrementing their bid by 1 cent).
3. Each ad request has just one advertisement slot to display.
