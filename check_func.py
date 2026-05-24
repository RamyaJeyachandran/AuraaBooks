import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
lines = open('templates/sales_orders.html', encoding='utf-8').readlines()
for i, line in enumerate(lines):
    if 'function selectViewMode' in line:
        start = max(0, i-2)
        end = min(len(lines), i+30)
        for j in range(start, end):
            print(f'{j+1}: {lines[j].rstrip()}')
        break
