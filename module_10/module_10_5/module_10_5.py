from multiprocessing import Pool
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов: 0:00:04.417014
    start = datetime.now()

    for filename in filenames:
        read_info(filename)

    end = datetime.now()

    # Многопроцессорный вызов: 0:00:01.750722
    # start = datetime.now()

    # with Pool(processes=4) as pool:
    #     pool.map(read_info, filenames)

    # end = datetime.now()

    print(end - start)
