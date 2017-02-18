from quantity import history
from policy import submodules

print('loading...')
his = history.History(dtype='D', path='history')

for k, v in his.market.items():
    print (k)

    for submodule in submodules:
        rt = submodule(v.history)
        rf = rt.process()

        print(rt.name)
        print(rf)