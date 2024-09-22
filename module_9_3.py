first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (
    len(first_item) - len(second_item) for first_item, second_item in zip(first, second) if (
        len(first_item) != len(second_item))
)

second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))
