def using_percent(team1_num, team2_num):
    print("В команде Мастера кода участников: %d!" % team1_num)
    print("Итого сегодня в командах участников: %d и %d!" % (team1_num, team2_num))


def using_format(score_2, team1_time):
    print("Команда Волшебники данных решила задач: {}!".format(score_2))
    print("Волшебники данных решили задачи за {:.1f} с!".format(team1_time))


def using_f_string(score_1, score_2, team1_time, team2_time):
    print(f"Команды решили {score_1} и {score_2} задач.")

    tasks_total = score_1 + score_2
    time_avg = (team1_time + team2_time) / tasks_total

    print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!")

    if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
    print(f"Результат битвы: {result}!")


using_percent(team1_num=6, team2_num=6)
using_format(score_2=42, team1_time=1552.512)
using_f_string(score_1=40, score_2=42, team1_time=1552.512, team2_time=2153.31451)
