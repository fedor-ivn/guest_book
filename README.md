# guest_book
Тестовое задание "Гостевая книга". Реализовано на стеке: Django, DRF, Vue, Vuetify. 

Выходя за рамки задания, реализована пагинация.

## Техническое задание:
Написать сервис “Гостевая книга”.

Сервис состоит из одной веб страницы.

На ней располагаются кнопка “Оставить отзыв” и карточки отзывов.

При нажатии на кнопку “Оставить отзыв” открывается форма, в которой три поля:
* [ ] Имя (От 3 до 32 символов)
* [ ] Отзыв (От 16 до 512 символов)
* [ ] Картинка (Необязательное).

В карточке отзыва должно быть:
* [ ] Имя
* [ ] Отзыв
* [ ] Картинка (Если имеется)
* [ ] Дата добавления отзыва

Рекомендуемый стек:
* [ ] Django + DRF
* [ ] Vue + Axios + Element-UI + Typescript (Необязательно)

После выполнения выложить на github и прислать ссылку на репозиторий

## Подготовка к запуску
1. Клонируем проект.
```
git clone https://github.com/fedor-ivn/guest_book.git
```
2. Настраиваем virtualenv и пакеты в нём.
```
cd innova_comments_app
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
3. Миграции и загрузка фикстур.
```
python manage.py migrate
python manage.py loaddata ./main/fixtures/initial_data.json
```
4. Скачать архив и распаковать в корне проекта.
[Ссылка на Google Disk](https://drive.google.com/file/d/11r9jtAcDcGX-JlOr-R2CZyprx7BgKEGp/view?usp=sharing)
