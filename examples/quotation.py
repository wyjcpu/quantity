from quantity import quotation


qu = quotation.use('sina')

print(qu.all_market)

# 单只股票
print(qu.stocks('162411')) # 支持直接指定前缀，如 'sh000001'

# 多只股票
print(qu.stocks(['000001', '162411']))

# 更新股票代码
print(quotation.update_stock_codes())

# 选择 leverfun 免费十档行情
qu = quotation.use('lf') # ['leverfun', 'lf']

# 获取十档行情
# 单只股票
print(qu.stocks('162411'))

# 多只股票
print(qu.stocks(['000001', '162411']))