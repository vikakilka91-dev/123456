def check_confirm(message: str) -> bool:
    """Запрашивает подтверждение действия у пользователя."""
    while True:
        answer = input(f"{message} (y/n): ").strip().lower()
        if answer in ['y', 'yes', 'н', 'да']:
            return True
        elif answer in ['n', 'no', 'т', 'нет']:
            return False
        else:
            print("Пожалуйста, введите 'y' (да) или 'n' (нет).")
