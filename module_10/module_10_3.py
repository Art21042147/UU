from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        self.print_lock = Lock()

    def deposit(self):
        for _ in range(100):
            coming = randint(50, 500)
            self.balance += coming

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            with self.print_lock:
                print(f"Пополнение: {coming}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for _ in range(100):
            spending = randint(50, 500)
            with self.print_lock:
                print(f"Запрос на {spending}")

            if spending <= self.balance:
                self.balance -= spending
                with self.print_lock:
                    print(f"Снятие: {spending}. Баланс: {self.balance}")
            else:
                with self.print_lock:
                    print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
