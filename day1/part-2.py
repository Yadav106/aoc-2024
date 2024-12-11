with open("input.txt", "r") as f:
    ip_text = f.read()

ip_lines = ip_text.splitlines()

arr_a = []
arr_b = []

for line in ip_lines:
    temp = line.split()
    arr_a.append(int(temp[0].strip()))
    arr_b.append(int(temp[1].strip()))

count_occurence = {}
similarity_score = 0

for num in arr_b:
    count_occurence[num] = count_occurence.get(num, 0) + 1

for num in arr_a:
    similarity_score += num * count_occurence.get(num, 0)

print(similarity_score)
