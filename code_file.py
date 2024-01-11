all_files = {'1.txt': {'count': None},
             '2.txt': {'count': None},
             '3.txt': {'count': None}
             }

for file_name in all_files:
    with open(file_name, 'r', encoding='utf-8') as fp:
        all_files[file_name]['count'] = len(fp.readlines())

sorted_files = sorted(all_files.items(), key=lambda x: x[1]['count'] if x[1]['count'] is not None else 0)

with open("final.txt", 'a', encoding='utf-8') as final:
    for file_name, file_data in sorted_files:
        with open(file_name, 'r', encoding='utf-8') as fp:
            file_title = fp.readline().strip()
            final.write(f'{file_name}\n')

            file_lines = file_data['count']
            final.write(f'{file_lines}\n')

            fp.seek(0)  # возвращаемcя в начало файла

            file_content = fp.read()
            final.write(f'{file_content}\n\n')






