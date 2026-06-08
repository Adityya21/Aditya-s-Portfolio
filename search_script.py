with open('script.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'CGPA' in line or '%' in line:
        print(f'{i}: {line.encode("ascii", "ignore").decode().strip()}')
