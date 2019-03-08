#Лучшие продажи у магазина

stores = [
    [500, 700, 400, 540, 610, 1100, 800],
    [300, 490, 500, 320, 600, 900, 1500],
    [600, 140, 250, 400, 1300, 790, 2000]
]

store_profit = [] #Общий доход каждого магазина
for store in stores:
    store_profit.append(sum(store))

top_store_index = [] #Находим индекс лучшего магазина по суммарной выручке
for index, profit in enumerate(store_profit):
    if profit == max(store_profit):
        top_store_index.append(index)

#Топ 3 лучших продаж каждого магазина

for store in stores:
    store.sort(reverse=True)

top3_profit_stores = []
for store in stores:
    top3_profit_stores.append(store[:3])
print(top3_profit_stores)

#Лучший магазин за неделю с ежедневной вырочкой

for store in stores:
    store.sort(reverse=True)

top1_profit_stores = []
for store in stores:
    top1_profit_stores.append(store[:1])

top1_index_profit = []
for index, profit in enumerate(top1_profit_stores):
    if profit == max(top1_profit_stores):
        top1_index_profit.append(index)
