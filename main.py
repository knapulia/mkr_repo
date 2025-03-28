def load_file(file_path):
   with open (file_path, 'r', encoding='utf-8') as file:
       return file.read().splitlines()

def compare(file1, file2):
    lines1 = load_file(file1)
    lines2 = load_file(file2)

    same_lines = [line for line in lines1 if line in lines2]
    diff_lines = [line for line in lines1 + lines2 if line not in same_lines]

    return same_lines, diff_lines

def save_results(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)
