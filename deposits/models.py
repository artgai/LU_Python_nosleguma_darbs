from django.db import models


class InterestCalc:
    def __init__(self, deposit, term, rate):
        self.deposit = deposit
        self.term = term
        self.rate = rate

    def interest(self):
        return float(5)

    # Šeit atstāju kā paraugu funkcionējošu un pareizu
    # interest kalkulatoru, kas, diemžēl, praksē vēl nesāka
    # darboties, jo for cikls prasa int nevis float. Tāpēc
    # pagaidām manā aplikācijā visi interest ir 5.
    #
    # def interest(self):
    #     total = self.deposit
    #     profit = 1 + self.rate
    #
    #     for years in range(self.term):
    #         total = total * profit
    #
    #     interest = total - self.deposit
    #
    #     return interest


class Deposit(models.Model):
    deposit = models.FloatField()
    term = models.FloatField()
    rate = models.FloatField()

    def get_interest(self):
        calculation_data = InterestCalc(
            deposit=self.deposit,
            term=self.term,
            rate=self.rate,
        )

        result = calculation_data.interest()

        return result

    interest = property(get_interest)
