Привет!!!

Основные зависимости проекта
requests==2.31.0
pytest==8.4.1

Инструкции по запуску тестов:
1. Установите зависимости:
   pip install -r requirements.txt

2. Запустите тесты:
   pytest -v

Описание тестов:

test_male_with_job — находит самого высокого мужчину с работой.
test_male_without_job — проверяет, что при отсутствии работы герой либо отсутствует, либо соответствует условиям.
test_female_with_job — находит женщину с работой.
test_female_without_job — проверяет результат при отсутствии работы у женщин.
test_unknown_gender — обрабатывает пол "Unknown".
test_case_insensitivity — убеждается, что регистр в параметре gender не влияет на результат.
test_output_structure — проверяет наличие обязательных ключей в ответе.
test_return_none_when_no_match — возвращает None, если не найден ни один подходящий герой.
test_result_is_dict — проверяет, что результат — это словарь.
test_height_is_valid_number — проверяет корректность формата роста в см.
test_hero_has_image — проверяет, что у героя есть изображение.
test_different_filters_return_different_heroes — убеждается, что разные фильтры дают разных героев.
test_gender_with_typo_returns_none — опечатка в поле gender приводит к None.
