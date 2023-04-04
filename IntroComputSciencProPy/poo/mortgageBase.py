def findPayment(loan, r ,m):
    """Assumes loan and r are floats , m an int 
    Returns the monthly payment for a mortgage of size"""

    return loan*((r*(1+r)**m)/((1+r)**m-1))

class Mortgage(object):
    """Abstract class for building differentes kind of mortages"""
    def __init__(self,loan,annRate,months):
        """loan and annRate are floats, the other ins"""
        self.loan = loan
        self.rate = annRate/12
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment=findPayment(loan,self.rate,months)
        self.legend = None #description of mortgage

    def makePayment(self):
        self.paid.append(self.payment)
        reduction = self.payment -self.outstanding[-1]*self.rate
        self.outstanding.append(self.outstanding[-1]-reduction)
    def getTotalPaid(self):
        return sum(self.paid)
    def __str__(self):
        return self.legend

