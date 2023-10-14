import itertools

def permutations_lexicographic(s, n):
    # Генерируем все перестановки из n символов в строке s
    perms = itertools.permutations(s, n)

    # Преобразуем перестановки в список и сортируем их лексикографически
    sorted_perms = sorted([''.join(perm) for perm in perms])

    return sorted_perms

# Пример использования функции
s = "abc"
n = 2
result = permutations_lexicographic(s, n)
print(result)