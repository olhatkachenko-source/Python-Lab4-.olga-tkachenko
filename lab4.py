def create_tf23_1(filename="TF23_1.txt"):
    """
    Частина а) Створює текстовий файл TF23_1 із символьних рядків різної довжини.
    Виконується тімлідом або на етапі ініціалізації проєкту.
    """
    lines = [
        "Тестовий рядок номер 1 з цифрами 101 та нулями.",
        "Python 3.11: файл містить символи 1 і 0.",
        "Рядок різної довжини для перевірки заміни 1111 та 0000.",
        "Ще один рядок з даними 12345."
    ]
    
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')
        print(f"Файл '{filename}' успішно створено.")
    except IOError as e:
        print(f"Помилка при створенні файлу '{filename}': {e}")


def process_tf23_data(input_filename="TF23_1.txt", output_filename="TF23_2.txt", chunk_size=15):
    """
    Частина б) Читає вміст файлу TF23_1, замінює символ «1» на «0» та навпаки, 
    і записує у файл TF23_2 по 15 символів у рядок.
    Виконується Учасником 1.
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Помилка: файл '{input_filename}' не знайдено.")
        return
    except IOError as e:
        print(f"Помилка читання файлу '{input_filename}': {e}")
        return

    # Заміна «1» на «0» та «0» на «1»
    # Використовуємо словник для коректної взаємної заміни без затирання
    trans_table = str.maketrans({'1': '0', '0': '1'})
    processed_content = content.translate(trans_table)

    # Запис у новий файл порціями по chunk_size (15) символів
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            for i in range(0, len(processed_content), chunk_size):
                chunk = processed_content[i:i + chunk_size]
                file.write(chunk + '\n')
        print(f"Дані успішно оброблено та записано у файл '{output_filename}'.")
    except IOError as e:
        print(f"Помилка запису у файл '{output_filename}': {e}")


def print_tf23_2(filename="TF23_2.txt"):
    """
    Частина в) Читає вміст файлу TF23_2 і друкує його по рядках.
    Виконується Учасником 2.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(f"\n--- Вміст файлу {filename} ---")
            for line in file:
                # Використовуємо end='' щоб уникнути подвійного перенесення рядка, 
                # оскільки у файлі вже є символи кінця рядка
                print(line, end='')
            print("\n---------------------------------")
    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено.")
    except IOError as e:
        print(f"Помилка читання файлу '{filename}': {e}")


if __name__ == "__main__":
    # Головна точка входу для тестування програми всього циклу
    create_tf23_1()
    process_tf23_data()
    print_tf23_2()
