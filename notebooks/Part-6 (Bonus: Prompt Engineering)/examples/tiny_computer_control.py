from openai import OpenAI

# Ініціалізація клієнта
client = OpenAI()

def get_code_from_llm(system_instructions: str, user_instructions: str) -> str:
    """
    Надсилаємо інструкції до LLM та повертаємо отриманий Python-код як рядок.
    """
    response = client.responses.create(
        model="gpt-4o",  # або інша доступна модель
        input=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "input_text",
                        "text": system_instructions
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": user_instructions
                    }
                ]
            }
        ],
        text={
            "format": {
                "type": "text"
            }
        },
        reasoning={},
        tools=[],
        temperature=1,
        max_output_tokens=2048,
        top_p=1,
        store=True
    )

    # Отримуємо текст із відповіді
    code_result = response.output[0].content[0].text
    return code_result.replace("```python", "").replace('```', "")

def main():
    MAX_RETRIES = 5

    # Базова інструкція для system
    system_prompt = (
        "Ти — асистент, що перетворює текстові команди у Python-код для виконання.\n"
        "Повертай ЛИШЕ код (Python) без додаткових пояснень чи розгорнутих відповідей.\n"
        "Якщо треба створити файл, використовуй операції з файловою системою.\n"
        "Якщо трапляється помилка, при її виправленні повертай нову версію КОРЕКТНОГО коду."
    )

    while True:
        # Зчитуємо команду користувача з терміналу
        user_input = input("Введіть вашу команду (або 'exit' для виходу): ").strip()
        if user_input.lower() == "exit":
            print("Завершення роботи.")
            break

        retry_count = 0
        current_user_prompt = user_input

        while retry_count < MAX_RETRIES:
            # Надсилаємо поточний user_prompt у LLM для отримання коду
            code_candidate = get_code_from_llm(system_prompt, current_user_prompt)

            try:
                print("\nОтриманий код:")
                print(code_candidate)
                print("\nВиконую код...\n")
                # Використовуємо exec для виконання
                exec_globals = {}
                exec_locals = {}
                exec(code_candidate, exec_globals, exec_locals)

                print("Код виконано успішно.\n")
                # Якщо все ОК, виходимо з циклу спроб
                break

            except Exception as e:
                # Виводимо помилку
                print(f"Помилка під час виконання: {str(e)}\n")
                retry_count += 1
                if retry_count < MAX_RETRIES:
                    # Формуємо новий prompt із описом помилки
                    current_user_prompt = (
                        f"Сталася помилка під час виконання коду:\n{str(e)}\n"
                        f"Виправ цю помилку, будь ласка, і повертай лише коректний Python-код."
                    )
                else:
                    print("Досягнуто ліміту спроб. Перериваю спроби виправити код.\n")

if __name__ == "__main__":
    main()
