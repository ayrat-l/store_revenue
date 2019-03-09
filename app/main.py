from app.lib import store_with_best_profit

stores = [
    [500, 700, 400, 540, 610, 1100, 800],
    [300, 490, 500, 320, 600, 900, 1500],
    [600, 140, 250, 400, 1300, 790, 2000]
]

print(store_with_best_profit(stores))


