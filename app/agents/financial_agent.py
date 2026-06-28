import re
from datetime import datetime

from app.models.transaction import Transaction
from app.repositories.transaction_repository import TransactionRepository


class FinancialAgent:

    def __init__(self):
        self.repository = TransactionRepository()

    def analyze(self, text):

        amount = self.extract_amount(text)

        transaction_type = self.detect_type(text)

        category = self.detect_category(text)

        transaction = Transaction(
            amount=amount,
            transaction_type=transaction_type,
            category=category,
            description=text,
            created_at=datetime.now()
        )

        self.repository.save(transaction)

        return transaction

    def extract_amount(self, text):

        numbers = re.findall(r"\d+", text)

        if numbers:
            return int(numbers[0])

        return 0

    def detect_type(self, text):

        expense = [
            "پرداخت",
            "خرید",
            "هزینه"
        ]

        income = [
            "فروش",
            "درآمد",
            "دریافت"
        ]

        for word in expense:
            if word in text:
                return "expense"

        for word in income:
            if word in text:
                return "income"

        return "unknown"

    def detect_category(self, text):

        if "بنزین" in text:
            return "حمل و نقل"

        if "چای" in text:
            return "چای"

        if "تبلیغات" in text:
            return "تبلیغات"

        if "اجاره" in text:
            return "اجاره"

        return "عمومی"