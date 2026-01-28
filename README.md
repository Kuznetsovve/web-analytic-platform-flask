# Аналитическая платформа заказов

**Тема:** приложение с эмулятором заказов и с аналитическими запросами

**Автор:** Кузнецов Владислав

## Cписок роутов/эндпоинтов

- `/`, `/index`, `/home` - домашняя страница
- `/about` - о проекте
- `/api/hash/<string>` - выводит хэшированную строку
- `/register` - регистрация
- `/login` - вход
- `/logout` - выход
- `/profile` - профиль (требуется логин)
- `/product/<id>` - продукт
- `/order` - заказ
- `/max_revenue_query` - запрос (требуется логин)
- `/avg_revenue_query` - запрос (требуется логин)
- `/total_revenue_query` - запрос (требуется логин)
- `/top_products_query` - запрос (требуется логин)
- `/categories_query` - запрос (требуется логин)
- `/stocks_query` - запрос (требуется логин)

## Описание функциональности приложения

Для гостя:
1. Доступ к форме‑эмулятору оформления заказа без регистрации (выбор товара, его количества, цены)
2. Сохранение введённых данных в базу данных для последующего анализа администратором

Для администратора:
1. Аутентификация через страницу введения логина и пароля и доступ в административную панель после успешного входа
2. Просмотр и фильтрация заказов, построение простых заготовленных аналитических отчётов
3. Работа и с данными, введёнными гостями, и с тестовым набором данных для демонстрации аналитики при отсутствии активности пользователей

## Логическая модель данных

Таблица: `admins`

| Поле          |
|---------------|
| __id__        |
| username      |
| password_hash |
| created_on    |

Таблица: `orders`

| Поле        |
|-------------|
| __id__      |
| created_at  |
| amount      |
| admin_id*   |
| product_id* |
| address     |

Таблица: `products`

| Поле       |
|------------|
| __id__     |
| created_at |
| amount     |
| price      |

Связи: `admins`-<`orders` (1:M)  `products`-<`orders` (1:M)

## Список сторонних библиотек:

```
blinker==1.9.0
click==8.3.1
colorama==0.4.6
Flask==3.1.2
Flask-Login==0.6.3
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.2
greenlet==3.3.0
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
SQLAlchemy==2.0.45
typing_extensions==4.15.0
Werkzeug==3.1.4
WTForms==3.2.1
python-dotenv==1.2.1
psycopg2-binary==2.9.11
```

## Материалы

1. https://habr.com/ru/articles/346306/
2. https://habr.com/ru/articles/346340/
3. https://habr.com/ru/articles/346342/
4. https://habr.com/ru/articles/346344/
5. https://habr.com/ru/articles/346346/
6. https://www.geeksforgeeks.org/python/making-a-flask-app-using-a-postgresql-database/
7. https://pypi.org/project/Flask-WTF/

