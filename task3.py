def hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:  
        print(f"Перемістити диск 1 з {from_rod} на {to_rod}")
        return

    hanoi(n-1, from_rod, aux_rod, to_rod)
    
    print(f"Перемістити диск {n} з {from_rod} на {to_rod}")
    
    hanoi(n-1, aux_rod, to_rod, from_rod)

# Функція для візуалізації стану
def show_state(rods):
    print("\nПоточний стан:")
    for rod, disks in rods.items():
        print(f"  {rod}: {disks}")

# Покращена версія з відображенням стану
def hanoi_with_state(n, from_rod='A', to_rod='C', aux_rod='B'):
    rods = {
        from_rod: list(range(n, 0, -1)),
        aux_rod: [],
        to_rod: []
    }
    
    show_state(rods)
    solve_hanoi(n, from_rod, to_rod, aux_rod, rods)
    print(f"\nВсього кроків: {2**n - 1}")

# Допоміжна рекурсивна функція
def solve_hanoi(n, from_rod, to_rod, aux_rod, rods):
    if n == 0:
        return
    
    solve_hanoi(n-1, from_rod, aux_rod, to_rod, rods)
    
    # Переміщуємо диск
    disk = rods[from_rod].pop()
    rods[to_rod].append(disk)
    print(f"\nДиск {disk} з {from_rod} на {to_rod}")
    show_state(rods)
    
    solve_hanoi(n-1, aux_rod, to_rod, from_rod, rods)

if __name__ == "__main__":
    try:
        n = int(input("Скільки дисків? "))
        if n > 0:
            print(f"\nРозв'язуємо Ханойські башти для {n} дисків")
            hanoi_with_state(n)
        else:
            print("Потрібно додатне число")
    except ValueError:
        print("Потрібно ввести число")