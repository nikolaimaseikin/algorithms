items = {
    'guitar': {'weight': 1, 'price': 1500},
    'recorder': {'weight': 4, 'price': 3000},
    'laptop': {'weight': 3, 'price': 2000},
    'iphone':{'weight': 1, 'price': 2000}
}
BAGPACK_CAPACITY = 4
solution_table = [[{'items_group':[], 'summary_price': 0} for i in range(BAGPACK_CAPACITY)] for i in range(len(items))]
row_index = 0
current_bag_capacity = 0
for key, value in items.items( ):
    for j in range(BAGPACK_CAPACITY): 
        current_bag_capacity = j + 1
        if value['weight'] < current_bag_capacity:
            if solution_table[row_index - 1][j]['summary_price'] > value["price"] + solution_table[row_index - 1][j - value["weight"]]['summary_price']:
                solution_table[row_index][j]['summary_price'] = solution_table[row_index - 1][j]['summary_price']
                solution_table[row_index][j]['items_group'] = solution_table[row_index - 1][j]['items_group']
            else:
                solution_table[row_index][j]['summary_price'] = value["price"] + solution_table[row_index - 1][j - value["weight"]]['summary_price']
                solution_table[row_index][j]['items_group'] = [key] + [solution_table[row_index - 1][j - value["weight"]]['items_group']][0]
        elif value['weight'] == current_bag_capacity:
            if solution_table[row_index - 1][j]['summary_price'] > value["price"]:
                solution_table[row_index][j]['summary_price'] = solution_table[row_index - 1][j]['summary_price']
                solution_table[row_index][j]['items_group'] = solution_table[row_index - 1][j]['items_group']
            else:
                solution_table[row_index][j]['summary_price'] = value["price"]
                solution_table[row_index][j]['items_group'] = [key]
        else:
            solution_table[row_index][j]['summary_price'] = solution_table[row_index - 1][j]['summary_price']
            solution_table[row_index][j]['items_group'] = solution_table[row_index - 1][j]['items_group']
    row_index += 1
for i in solution_table:
            for j in i:
                print(str(j['items_group']) + '= ' + str(j['summary_price']), end=" ")
            print()