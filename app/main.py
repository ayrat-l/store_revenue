from app.lib import *

stores = [
    [500, 700, 400, 540, 610, 1100, 800],
    [300, 490, 500, 320, 600, 900, 1500],
    [600, 140, 250, 400, 1300, 790, 2000]
]

print('Самый прибыльный магазин по суммарной выручке за неделю -', store_with_best_profit(stores))

print('ТОП 3 продаж каждого магазина -', top3_sales_of_each_store(stores))

print('Лучший магазин за неделю с ежедневной выручкой -', best_store_of_the_week_with_daily_profit(stores))

print('Худший магазин за неделю с ежедневной выручкой -', bad_store_of_the_week_with_daily_profit(stores))

print('Лучший магазин со средней ежедневной выручкой -', best_average_daily_profit(stores))




