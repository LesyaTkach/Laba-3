# TODO Напишите функцию для поиска индекса товара

def find_item_index(items, target):
    """
    Функция для поиска индекса первого вхождения элемента в списке.

    :param items: list - список товаров.
    :param target: str - товар, который нужно найти.
    :return: int | None - индекс первого вхождения товара или None, если товар не найден.
    """
    try:
        return items.index(target)
    except ValueError:
        return None
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
