
def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты в формате - 7000792289606361,
    и возвращает ее маску 7000 79** **** 6361."""
    if len(card_number) == 16:
        return card_number[:4] + " " + card_number[4:6] + "**" + " **** " + card_number[12:16]
    elif card_number == "":
        return card_number
    else:
        return card_number


def get_mask_account(bank_account_number: str) -> str:
    """Принимает на вход номер счета в формате- 73654108430135874305 и
    возвращает его маску **4305."""
    if len(bank_account_number) >= 20:
        return "**" + bank_account_number[-4:]
    elif bank_account_number == "":
        return bank_account_number
    else:
        return bank_account_number
