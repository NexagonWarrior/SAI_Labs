def sort_tuples(data):
    size = len(data)
    for i in range(size):
        for j in range(0, size - i - 1):
            if data[j][1] > data[j + 1][1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
    return data

if __name__ == "__main__":

    my_list = [(10, 5), (3, 1), (8, 9), (2, 4), (5, 2)]

    print(my_list)
    sorted_list = sort_tuples(my_list)
    print(sorted_list)