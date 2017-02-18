from quantity import utils


print(utils.is_holiday_today())
print(utils.is_holiday('2016-12-12'))
print(utils.is_tradetime_now())
print(utils.get_stock_type('600630'))
print(utils.get_stock_type('000630'))
print(utils.get_all_stock_codes())