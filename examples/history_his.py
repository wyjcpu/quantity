from quantity import history

his = history.History(dtype='D', path='history')

res = his['000001'].MA(5)