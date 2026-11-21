# Блогикум. Часть 2: публикации

Стартовый репозиторий для второй части проекта «Блогикум».
В папке `blogicum/` уже подготовлено приложение по заданию первой части:
главная страница, страницы публикаций и категорий, страницы «О проекте»
и «Наши правила», общие шаблоны и статика.
Данные трёх публикаций пока хранятся в списке `posts` в файле
`blogicum/blog/views.py`.

Во второй части нужно перейти к базе данных. Требования к моделям,
панели администратора и отображению публикаций приведены в уроке.

## Структура

```text
ap-django2/
├── blogicum/
│   ├── blog/              # Приложение публикаций
│   ├── pages/             # Статические страницы
│   ├── blogicum/          # Настройки и маршруты проекта
│   ├── static/            # CSS и изображения
│   ├── templates/         # Работающие шаблоны первой части
│   └── manage.py
├── templates/             # Новые шаблоны для второй части
├── tests/                 # Тесты второй части
├── db.json                # Фикстуры для будущих моделей
├── pytest.ini
└── requirements.txt
```



git clone https://github.com/leramel/Blokigum-2.git

cd Blokigum-2

python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt

python blogicum/manage.py migrate

python blogicum/manage.py loaddata db.json

python blogicum/manage.py createsuperuser

python blogicum/manage.py runserver


