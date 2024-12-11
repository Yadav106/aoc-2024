with open("input.txt", "r") as f:
    ip_text = f.read()

ip_lines = ip_text.splitlines()

arr_a = []
arr_b = []

for line in ip_lines:
    temp = line.split()
    arr_a.append(int(temp[0].strip()))
    arr_b.append(int(temp[1].strip()))

arr_a = sorted(arr_a)
arr_b = sorted(arr_b)

tot_distance = 0


for i in range(len(arr_a)):
    tot_distance += abs(arr_a[i] - arr_b[i])


print(tot_distance)
