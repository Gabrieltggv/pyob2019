import collections
import decimal

from finstory import FinancialHistory, new_decimal

class DeductibleHistory:

    def __init__(self, initial_balance=0.0):
        self._history = FinancialHistory(initial_balance)
        self._deductions = decimal.Decimal(0)

    def __repr__(self):
        name = self.__class__.__name__
        return f'<{name} balance: {self.balance:.2f}>'

    def spend(self, amount, reason, deducting=0.0):
        """Record expense with partial deduction"""
        self._history.spend(amount, reason)
        if deducting:
            self._deductions += new_decimal(deducting)

    def spend_deductible(self, amount, reason):
        """Record expense with full deduction"""
        self._history.spend(amount, reason)
        self.spend(amount, reason, amount)

    @property
    def deductions(self):
        return self._deductions

    def __getattr__(self, name):
        return getattr(self._history, name)
