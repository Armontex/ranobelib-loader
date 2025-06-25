```markdown
# Ranobelib Loader

Неофициальное API для загрузки контента на сайт Ranobelib.me.

## Установка

```bash
pip install ranobelib-loader
```

## Требования

- Python >= 3.10

## Использование

```python
from ranobelib_loader import RanobelibLoader

# Инициализация загрузчика с access token
loader = RanobelibLoader(access_token="your_access_token")

# Загрузка главы
response = loader.load_chapter(
    branch_id=123,
    text="Текст главы в формате Markdown",
    manga_id=456,
    name="Название главы",
    number=1,
    volume=1,
    teams=[789],
    publish_at="2025-01-01 12:00:00"  # По UTC
)

print(response.status_code)
print(response.json())
```

## Параметры метода load_chapter

- `branch_id` (int): ID ветки
- `text` (str): Текст новеллы (обычный текст или Markdown)
- `manga_id` (int): ID новеллы
- `name` (str): Название главы
- `number` (int): Номер главы
- `volume` (int): Том
- `teams` (list[int]): ID команды/команд
- `publish_at` (str | datetime | None): Время публикации в формате "YYYY-mm-dd HH:MM:SS" (по UTC)
- `pages` (Any): Страницы (по умолчанию [])
- `expired_type` (int): Тип истечения (по умолчанию 0)
- `attachments` (Any): Вложения (по умолчанию [])

## Зависимости

- lxml==5.4.0
- Markdown==3.8.2
- prosemirror==0.5.2
- Requests==2.32.4

## Лицензия

BSD 3-Clause License

Этот модуль содержит код из проекта [prosemirror-py](https://github.com/fellowapp/prosemirror-py) (лицензия BSD 3-Clause "New" or "Revised" License)
```