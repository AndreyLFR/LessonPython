func = '''def rename_files(desired_name, num_digits, source_ext, target_ext, range_old_name=[]):
    import os
    current_path = os.getcwd()
    if not os.path.isdir('test_folder'):
        os.mkdir('test_folder')
    files = os.listdir(f'{current_path}/test_folder')
    i = 1
    for f in files:
        if f.split('.')[-1] == source_ext:
            remainder = [f[i] for i in range(range_old_name[0] - 1, range_old_name[1])] if range_old_name else ''
            serial_num = [str(0) for _ in range(num_digits - len(str(i)))]
            new_name = f'{"".join(remainder)}{desired_name}{"".join(serial_num)}{str(i)}.{target_ext}'
            i += 1
            os.rename(f'test_folder/{f}', f'test_folder/{new_name}')
'''
import os
current_path = os.getcwd()
with open(f'{current_path}/__init__.py', 'w', encoding='utf-8') as f:
    f.write(func)
