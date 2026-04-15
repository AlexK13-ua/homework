        # 13.1. Очистити текст від html-тегів

import codecs

def delete_html_tags(draft, result_file='cleaned.txt'):
    try:
        with codecs.open(draft, 'r', 'utf-8') as file:
            html = file.read()

        cleaned_text = ""
        is_tag = False

        for char in html:
            if char == "<":
                is_tag = True
            elif char == ">":
                is_tag = False
            elif not is_tag:
                cleaned_text += char

        lines = cleaned_text.splitlines()
        final_lines = []
        for line in lines:
            if line.strip():
                final_lines.append(line.strip())

        with codecs.open(result_file, 'w', 'utf-8') as out_file:
            out_file.write("\n".join(final_lines))

        print(f"Файл успішно очищено. Результат у: {result_file}")

    except FileNotFoundError:
        print(f"Помилка: Файл {draft} не знайдено.")

delete_html_tags('draft.html')