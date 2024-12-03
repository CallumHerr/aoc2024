def read_file(fileLoc):
    file = open(fileLoc, "r")

    first_list = []
    second_list = []
    for line in file:
        numbers = line.split()
        first_list.append(numbers[0])
        second_list.append(numbers[1])

    return [first_list, second_list]

[list1, list2] = read_file("data.txt")
list1.sort()
list2.sort()

distance_sum = 0
similarity_score = 0
n = 0
for i in range(len(list1)):
    distance_sum += abs(int(list1[i]) - int(list2[i]))
    #Calculating similarity
    count = 0
    for j in range(n, len(list2)):
        if list2[j] == list1[i]:
            count += 1
            n += 1
        elif count > 0:
            n += 1
            break
    similarity_score += int(list1[i]) * count


print("Distance: " + str(distance_sum))
print("Similarity score: " + str(similarity_score))
