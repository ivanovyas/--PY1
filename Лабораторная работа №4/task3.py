def delete(list_, index=None):
    if index is None:
        list_delete = list_[:-1]  # Слайсируем до последнего элемента, если индекс не задан
    else:
        list_delete = list_[:index] + list_[index+1:]  # Вырезаем элемент с индексом = index
    return list_delete

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
