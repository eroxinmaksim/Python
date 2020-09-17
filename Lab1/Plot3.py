import matplotlib.pyplot as plt
import Lab1

spam_arr = Lab1.dict_spam
ham_arr = Lab1.dict_ham
spam_tmp = {}
ham_tmp = {}
spam_d = {}
ham_d = {}


def max_s(array):
    max_w = 0
    for item in array:
        if len(item) > max_w:
            max_w = len(item)
    return max_w


def counter_array(tmp_list, out_array):
    for item in tmp_list:
        if not item in out_array:
            out_array[item] = 1
        else:
            out_array[item] += 1
    return tmp_list


def rewrite_data(arr_in, arr_out, max_w):
    for item in range(0, max_w):
        arr_out[item] = 0
    for key, value in arr_in.items():
        for i in range(0, max_w):
            if len(key) == i:
                arr_out[i] += value


def create(arr1, arr2):
    fig, ax = plt.subplots()
    ax.plot(arr1.keys(), arr1.values(), 'y')
    ax.plot(arr2.keys(), arr2.values(), 'b')
    ax.set_xlabel('Кол-во букв', fontsize=15, color='red')
    ax.set_ylabel('Частота', fontsize=15, color='red')
    plt.show()


def avg(array):
    average = 0
    for item in array:
        average = sum(len(item) for item in array) / len(array)
    return average


print('Среднее кол-во букв в категории spam', avg(spam_arr))
print('Среднее кол-во букв в категории ham', avg(ham_arr))
counter_array(spam_arr, spam_tmp)
counter_array(ham_arr, ham_tmp)

rewrite_data(spam_tmp, spam_d, max_s(spam_arr) + 1)
rewrite_data(ham_tmp, ham_d, max_s(ham_arr) + 1)

create(spam_d, ham_d)
