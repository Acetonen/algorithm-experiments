Feature: Находим длину списка
  Для того чтобы найти длину списка
  Мы создали метод len()

  Scenario Outline: Найти длину списка
    Given У нас есть лист <list_of_numbers>
    When мы вызываем метод .len
    Then получаем количество элементов как переменную <length>

    Examples:
      | list_of_numbers | length |
      | 1 2 3           | 3      |
      |                 | 0      |