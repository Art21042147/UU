def apply_all_func(int_list, *functions):
    if not all(isinstance(x, (int, float)) for x in int_list):
        raise ValueError(
            "Все элементы списка должны быть числами (int или float).")

    results = {}

    for func in functions:
        results[func.__name__] = func(int_list)

    return results


try:
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
    print(apply_all_func([6, "20", 15, 9], max, min))
    # п.2 примечаний воспринят мною как намёк на то, что неплохо бы было закрепить знания из предыдущего модуля.
except ValueError as e:
    print(e)
