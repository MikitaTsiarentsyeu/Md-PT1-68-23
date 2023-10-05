
brands = set()

is_first = True
with open('test.csv') as f:
    for line in f:
        if is_first:
            is_first = False
            continue
        brands.add(line.strip().split(',')[0])

print(brands)

# record = ["puma", "suede", "blue"]
# record = ','.join(record) + '\n'
# with open('test.csv', 'a') as f:
#     f.write(record)


import csv

with open('test.csv') as f:
    reader = csv.reader(f)
    for record in reader:
        print(record)

with open('test.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["puma", "suede", "blue"])

fields = ['brand','model','color']

with open('test.csv') as f:
    reader = csv.DictReader(f, fieldnames=fields)
    for item in reader:
        print(item)