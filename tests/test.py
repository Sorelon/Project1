from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card
from src.widget import get_date


print(get_mask_card_number(str(7000792289606361)))
print(get_mask_account(str(7000792289606361)))
print(mask_account_card("Maestro 1596837868705199"))
print(get_date("2024-03-11Т02:26:18.671407"))
