import os


def get_info_and_writing_to_list(file_names):
    '''Считывание содержимого файлов и запись информации в список'''
    my_data = []
    for file in file_names:
        with open(file, encoding='utf-8') as f:
            lines = f.read().splitlines()
            my_data.append([file, len(lines)])
            my_data[len(my_data)-1] += lines
    my_data.sort(key=len)
    return my_data


def writing_info_to_file(my_data, my_file):
    '''Запись в файл информации (создание файла при условии отсутствия другого с таким же именем)'''
    with open('res.txt', 'w', encoding='utf-8') as f:
        for file in my_data:
            for elem in file:
                f.write(f'{elem}\n')
    file_path = os.path.join(os.getcwd(), my_file)
    return file_path

data = get_info_and_writing_to_list(['1.txt', '2.txt', '3.txt'])
file_path = writing_info_to_file(data, 'res.txt')

# print(file_path)



