# 1. Скачайте любой датасет с сайта https://www.kaggle.com/datasets
# Загрузите набор данных из CSV-файла в DataFrame.
# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# Выведите информацию о данных (.info()) и статистическое описание (.describe()).

# 2. Определите среднюю зарплату (Salary) по городу (City) - используйте файл
# приложенный к дз - staff_list.csv (переименовал)


import pandas as pnds
from pandas import Series, DataFrame


def task01():
    dframe: DataFrame = pnds.read_csv('data_store/country_hits.csv')

    print('Первые 5 строк:')
    print(dframe.head())
    print('\nПоследние 5 строк:')
    print(dframe.tail())

    # При выводе виде f-строки или через запятую,
    # надпись "Информация о данных:" низменно появлялась в конце, перед None.
    # В остальных строках не срабатывал \n после надписи, перед head(), tail() и describe().

    print('\nИнформация о данных:')
    print(dframe.info())
    print('\nСтатистическое описание:')
    print(dframe.describe())


def task02():
    dframe: DataFrame = pnds.read_csv('data_store/staff_list.csv')

    dframe['City']: Series = dframe['City'].fillna('Регионы')
    dframe['Salary']: Series = dframe['Salary'].fillna(0)

    # Зерокот помог сделать переименование столбцов, сокращение зарплаты до копеек и добавление ₽

    average_salary: DataFrame = dframe.groupby('City')['Salary'].mean().reset_index()
    average_salary['Salary']: Series = average_salary['Salary'].apply(lambda x: f'{x:.2f} ₽')

    average_salary: DataFrame = average_salary.rename(columns={'City': 'Город', 'Salary': 'Средняя зарплата'})

    print('\nИсправленная таблица:')
    print(dframe)
    print('\nСредняя зарплата по городам:')
    print(average_salary)


if __name__ == "__main__":
    task01()
    task02()