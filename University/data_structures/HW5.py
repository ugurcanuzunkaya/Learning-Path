def bubble_sort_string(inp_str):
    """
    Write a function that sorts the characters of an input string in alphabetical order by using Bubble Sort Algorithm.
    (Your function should be case insensitive.)
    """
    out_str = inp_str.lower()
    for _ in range(len(out_str)):
        for j in range(len(out_str) - 1):
            if out_str[j] > out_str[j + 1]:
                out_str = out_str[:j] + out_str[j + 1] + out_str[j] + out_str[j + 2:]
    for i in range(len(inp_str)):
        if inp_str[i] not in out_str:
            out_str = out_str.replace(inp_str[i].lower(), inp_str[i], inp_str.count(inp_str[i]))
    return out_str


def selection_sort_string(inp_str):
    """
    Write a function that sorts the characters of an input string in alphabetical order by using Selection Sort Algorithm.
    (Your function should be case insensitive.)
    """
    out_list = list(inp_str.lower())
    for f_s in range(len(out_list) - 1, 0, -1):
        pos_max = 0
        for i in range(1, f_s + 1):
            if out_list[i] > out_list[pos_max]:
                pos_max = i

        temp = out_list[f_s]
        out_list[f_s] = out_list[pos_max]
        out_list[pos_max] = temp

    out_str = ''.join(out_list)

    for i in range(len(inp_str)):
        if inp_str[i] not in out_str:
            out_str = out_str.replace(inp_str[i].lower(), inp_str[i], inp_str.count(inp_str[i]))
    return out_str


def insertion_sort_string(inp_str):
    """
    Write a function that sorts the characters of an input string in alphabetical order by using Insertion Sort Algorithm.
    (Your function should be case insensitive.)
    """
    out_list = list(inp_str.lower())
    for i in range(1, len(out_list)):
        j = i - 1
        n_el = out_list[i]
        while j >= 0 and out_list[j] > n_el:
            out_list[j + 1] = out_list[j]
            j -= 1
        out_list[j + 1] = n_el

    out_str = ''.join(out_list)

    for i in range(len(inp_str)):
        if inp_str[i] not in out_str:
            out_str = out_str.replace(inp_str[i].lower(), inp_str[i], inp_str.count(inp_str[i]))
    return out_str


inp_str = 'Canakkale'

out_str_1 = bubble_sort_string(inp_str)

out_str_2 = selection_sort_string(inp_str)

out_str_3 = insertion_sort_string(inp_str)

print(f"Bubble Sort: {out_str_1}, Selection Sort: {out_str_2}, Insertion Sort: {out_str_3}")




