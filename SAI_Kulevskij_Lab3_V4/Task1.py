def rev_req_sort(list):
    if not list:
        return list
    return list[-1:] + rev_req_sort(list[:-1])

if __name__ == '__main__':

    list_size = int(input())
    list = []

    for _ in range(list_size):
        list.append(int(input()))

    print(rev_req_sort(list))