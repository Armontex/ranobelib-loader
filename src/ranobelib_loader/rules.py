from prosemirror.model.from_dom import TagParseRule

def __get_rule(tag: str, node: str | None , mark: str | None = None) -> TagParseRule:
    return TagParseRule(
        tag=tag,                     # HTML-тег
        node=node,                   # Соответствующий узел в схеме
        priority=0,                  # Приоритет правила (обычно 0)
        consuming=True,              # "Потреблять" ли тег при парсинге
        context=None,                # Контекст (обычно None)
        mark=mark,                   # Метка (если нужно, например для <strong>)
        ignore=False,                # Игнорировать тег (если True)
        close_parent=False,          # Закрывать родительский тег
        skip=False,                  # Пропускать тег
        attrs=None,                  # Фиксированные атрибуты (устаревший способ)
        namespace=None,              # Пространство имён XML (обычно None)
        get_attrs=None,              # Динамические атрибуты
        content_element=None,        # Альтернативный элемент для содержимого
        get_content=None,            # Функция для получения содержимого
        preserve_whitespace=False    # Сохранять пробелы
    )


RULES = [
    # blocks
    __get_rule("h1", "heading"),
    __get_rule("h2", "heading"),
    __get_rule("h3", "heading"),
    __get_rule("h4", "heading"),
    __get_rule("h5", "heading"),
    __get_rule("h6", "heading"),
    __get_rule("ol", "orderedList"),
    __get_rule("ul", "bulletList"),
    __get_rule("li", "listItem"),
    __get_rule("blockquote", "blockquote"),
    __get_rule("hr", "horizontalRule"),

    #marks
    __get_rule("strong", None, "bold"),
    __get_rule("b", None, "bold"),
    __get_rule("bold", None, "bold"),
    __get_rule("em", None, "italic"),
    __get_rule("i", None, "italic"),
    __get_rule("u", None, "underline"),
    __get_rule("s", None, "strike"),
    __get_rule("del", None, "strike"),
]

__all__ = ["RULES"]