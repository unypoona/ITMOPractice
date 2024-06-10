def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        columns = file.readline().strip().split(',')
        for line in file:
            values = line.strip().split(',')
            row = {}
            for col, val in zip(columns, values):
                if col in ['Quantity', 'Price', 'Freight']:  # Явное указание столбцов с числами
                    row[col] = float(val)
                else:
                    row[col] = val
            data.append(row)
    return data, columns

def write_csv(data, columns, file_path):

    with open(file_path, 'w') as file:
        file.write(','.join(columns) + '\n')
        for row in data:
            file.write(','.join(str(row[col]) for col in columns) + '\n')

def add_total_column(data):

    for row in data:
        row['Total'] = round(row['Quantity'] * row['Price'] + row['Freight'], 2)
    return data

data, columns = read_csv('orderdata_sample.csv')

data = add_total_column(data)
columns.append('Total')

write_csv(data, columns, 'orderdata_modified.csv')