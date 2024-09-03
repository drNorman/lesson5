# 1 task
immutable_var = ('a', 'b', 3, 12 , True, [5, 6])
print(immutable_var)

# 2 task
try:
    immutable_var[0] = 'c'
    print('Мы сделали невозможное!')
except TypeError:
    print("Нам не удалось изменить элемент коpтежа, так как после того как кортеж создан, в него нельзя добавлять элементы, а также изменять их или удалять.")

# 3 task
mutable_list = ['orange', False, 'e', 'f', 'g', 2024]
mutable_list[0] = 'white'
print(mutable_list)