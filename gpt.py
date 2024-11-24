from bip_utils import Bip32, Bip39SeedGenerator

def check_wallet_seed(seed_phrase):
    # Генерация мастер-ключа из мнемонической фразы
    seed_bytes = Bip39SeedGenerator(seed_phrase).Generate()
    bip32_key = Bip32.FromSeed(seed_bytes)

    # Проверка на успешное создание мастер-ключа
    if bip32_key is not None:
        return "Успешно удалось войти на кошелек!"
    else:
        return "Не удалось войти на кошелек. Пожалуйста, проверьте введенную Seed фразу."

# Seed фраза для тестирования
seed_phrase = "your seed phrase here"

# Проверка валидности Seed фразы
result = check_wallet_seed(seed_phrase)
print(result)
