#1. Лучшие продажи у магазина

def store_with_best_profit(stores):
    """
    >>> store_with_best_profit([[10,20,30,40,50], [15,10,25,34,40], [30,5,10,10,15]])
    [0]

    """
    store_profit = [] #Общий доход каждого магазина
    for store in stores:
        store_profit.append(sum(store))

    top_store_index = [] #Находим индекс лучшего магазина по суммарной выручке
    for index, profit in enumerate(store_profit):
        if profit == max(store_profit):
            top_store_index.append(index)
    return top_store_index

#2. Топ 3 лучших продаж каждого магазина

def top3_sales_of_each_store(stores):
    """
    >>> top3_sales_of_each_store([[10, 20, 30, 40, 50], [15, 10, 25, 34, 40], [30, 5, 10, 10, 15]])
    [[50, 40, 30], [40, 34, 25], [30, 15, 10]]
    """
    for store in stores:
        store.sort(reverse=True)

    top3_profit_stores = []
    for store in stores:
        top3_profit_stores.append(store[:3])
    return top3_profit_stores


#3. Лучший магазин за неделю с ежедневной выручкой

def best_store_of_the_week_with_daily_profit(stores):
    """
    >>> best_store_of_the_week_with_daily_profit([[10, 20, 30, 40, 50], [15, 10, 25, 34, 40], [30, 5, 10, 10, 15]])
    [0]
    """
    top1_profit_stores = [] #ТОП1 лучшая продажа магазина
    for store in stores:
        top1_profit_stores.append(max(store))

    top1_index_profit = [] #Определяем индекс магазина с лучшей ежедневной выручкой
    for index, profit in enumerate(top1_profit_stores):
        if profit == max(top1_profit_stores):
            top1_index_profit.append(index)
    return top1_index_profit

#4.Худший магазин за неделю с ежедневной выручкой

def bad_store_of_the_week_with_daily_profit(stores):
    """
    >>> bad_store_of_the_week_with_daily_profit([[10, 20, 30, 40, 50], [15, 10, 25, 34, 40], [30, 5, 10, 10, 15]])
    [2]
    """
    top1_bad_profit = [] #ТОП1 худшая ежедневная выручка за неделю
    for store in stores:
        top1_bad_profit.append(min(store))


    top1_bad_profit_index = [] #Определяем индекс магазина с худшей  ежедневной продажей
    for index, profit in enumerate(top1_bad_profit):
        if profit == min(top1_bad_profit):
            top1_bad_profit_index.append(index)
    return top1_bad_profit_index

#5.Лучший store со средней ежедневной выручкой

def best_average_daily_profit(stores):
    """
    >>> best_average_daily_profit([[10, 20, 30, 40, 50], [15, 10, 25, 34, 40], [30, 5, 10, 10, 15]])
    [0]
    """
    average_daily_profit = []
    for store in stores:
        average_daily_profit.append(round(sum(store)/len(store)))

    average_daily_profit_index = []
    for i, profit in enumerate(average_daily_profit):
        if profit == max(average_daily_profit):
            average_daily_profit_index.append(i)
    return average_daily_profit_index
