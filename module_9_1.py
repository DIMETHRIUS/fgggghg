def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        key = function.__name__
        try:
            result = function(int_list)
            results[key] = result
        except TypeError as exc:
            print(f"Ошибка при применении функции {key}: {exc}")
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
