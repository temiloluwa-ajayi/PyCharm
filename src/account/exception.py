class AccountException(Exception):
    def __init__(self, message):
        super().__init__(message)


class AccountWithdrawalException(Exception):
    def __init__(self, message):
        super().__init__(message)
