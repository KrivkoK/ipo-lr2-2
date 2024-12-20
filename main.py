def vse_apples(n, k):
    if n <= 0:
        return "Количество школьников должно быть больше нуля."
    
    apples_per_student = k // n  # Количество яблок, которое получит каждый школьник
    remaining_apples = k % n      # Остаток яблок в корзинке
    return apples_per_student, remaining_apples
# Получаем ввод от пользователя
try:
    n = int(input("Введите количество школьников (n): "))
    k = int(input("Введите количество яблок (k): "))
    
    result = vse_apples(n, k)
    
    if isinstance(result, tuple):
        print(f"Каждому школьнику достанется: {result[0]} яблок(а)")
        print(f"В корзинке останется: {result[1]} яблок(а)")
    else:
        print(result)
except ValueError:
    print("Пожалуйста, введите целые числа.")
