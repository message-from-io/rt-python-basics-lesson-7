
'''
7.1. Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.

Примечание: Списки фруктов создайте вручную в начале файла.
'''

list_1 = ['apple', 'pear', 'banana', 'plum', 'peach']
list_2 = ['pineapple', 'mango', 'apple', 'kiwi', 'banana']
result_list = []

result_list = [item_2 for item_2 in list_2 if item_2 in list_1]
print(result_list)

# Результат:
#
# ['apple', 'banana']
