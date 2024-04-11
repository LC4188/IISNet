def read_csv(csv_path):
    with open(csv_path, 'r') as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines][1:]
    return lines

def count_class(csv_path):
    lines = read_csv(csv_path)
    label = []
    for l in lines:
        context = l.split(',')
        wnid = context[1]
        if wnid not in label:
            label.append(wnid)
    return len(label)
