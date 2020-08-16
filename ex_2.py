from collections import Counter

file = open('hits.txt', 'r')
all_str = file.readlines()
ip = []
for i in all_str:
    c = i.split("\t")[1].split("\t")[0]
    ip.append(c)
count_ip = Counter(ip)
print(count_ip.most_common(5))