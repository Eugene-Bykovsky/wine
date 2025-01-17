# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка

- Убедитесь, что у вас установлен Python версии 3.8 или выше. Это можно проверить с помощью команды:

    ```
    python3 --version
    ```
  
- Скачайте репозиторий с кодом и перейдите в него:

    ```
    git clone git@github.com:Eugene-Bykovsky/wine.git
    cd wine
    ```
  
- Создайте и активируйте виртуальное окружение для изоляции зависимостей:

    ```
    python3 -m venv venv
    source venv/bin/activate  # Для Linux и macOS
    venv\Scripts\activate   # Для Windows
    ```
  
- Установите зависимости из файла requirements.txt:

    ```
    pip install -r requirements.txt
    ```

## Запуск

- Запустите сайт командой `python3 main.py`

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
