import subprocess
from collections import defaultdict

def part1(input: str):
    lines = input.split('\n')
    result = 0
    i = 0
    fs = defaultdict(lambda: {'file_sizes':0, "sub_dirs":[]})
    cwd_stack = []
    while i < len(lines):
        if lines[i].startswith('$'):
            _, command, value = lines[i].split(' ')
            if command == 'cd':
                if value == '..':
                    cwd_stack.pop()
                else:
                    cwd_stack.append(value)

        else:
            # this is $ ls command
            
            size_or_dir, path = lines[i].split(' ')
            cwd = "/".join(cwd_stack)
            if size_or_dir == 'dir':
                fs[cwd]['sub_dirs'].append(cwd+'/'+path)
                fs[cwd+'/'+path] = {'file_sizes':0, "sub_dirs":[]}
            else:
                fs[cwd]['file_sizes'] += int(size_or_dir)


        i += 1
    dir_sizes = []
    for _,dir in fs.items():
        dir_size = dir['file_sizes']
        dir_size += sub_dir_sizes(dir['sub_dirs'], fs)

        dir_sizes.append(dir_size)


    for ds in dir_sizes:
        if ds > 100000:
            continue
        else: 
            result += ds

    print('Part1: ',result)
    return str(result)

def sub_dir_sizes(sub_dirs, fs):
    result = 0
    for sub_dir in sub_dirs:
        dir = fs.get(sub_dir)

        dir_size = dir.get('file_sizes')
        dir_size += sub_dir_sizes(dir.get('sub_dirs'), fs)

        result += dir_size
    return result

def part2(input: str):
    lines = input.split('\n')
    result = 0
    i = 0
    fs = defaultdict(lambda: {'file_sizes':0, "sub_dirs":[]})
    cwd_stack = []
    while i < len(lines):
        if lines[i].startswith('$'):
            _, command, value = lines[i].split(' ')
            if command == 'cd':
                if value == '..':
                    cwd_stack.pop()
                else:
                    cwd_stack.append(value)

        else:
            # this is $ ls command
            
            size_or_dir, path = lines[i].split(' ')
            cwd = "/".join(cwd_stack)
            if size_or_dir == 'dir':
                fs[cwd]['sub_dirs'].append(cwd+'/'+path)
                fs[cwd+'/'+path] = {'file_sizes':0, "sub_dirs":[]}
            else:
                fs[cwd]['file_sizes'] += int(size_or_dir)


        i += 1
    dir_sizes = []
    for _,dir in fs.items():
        dir_size = dir['file_sizes']
        dir_size += sub_dir_sizes(dir['sub_dirs'], fs)

        dir_sizes.append(dir_size)


    disk_size = 70000000
    needed_space = 30000000
    current_unused_space = disk_size - max(dir_sizes) 
    required_space = needed_space - current_unused_space

    potentials = []
    for ds in dir_sizes:
        if ds > required_space:
            potentials.append(ds)
    result += min(potentials) 

    print('Part2: ',result)
    return result

# 1978318

if __name__ == '__main__':
    input_text = open('input.txt', 'r')
    input: str = input_text.read()

    result = part2(input)
    if not result:
        result = part1(input)


    subprocess.run(['pbcopy'], input=str(result).encode('utf-8'))