# Этот модуль содержит код из проекта prosemirror-py (https://github.com/fellowapp/prosemirror-py)
# Лицензия: BSD 3-Clause "New" or "Revised" License
# Copyright (c) 2025 fellowapp

import requests
import lxml.html
from requests import Session, Response
from datetime import datetime, timezone
from typing import Any
from prosemirror.model.from_dom import DOMParser
from markdown import markdown

from .rules import RULES
from .schema import schema

API_URL = "https://api.cdnlibs.org/api/chapters"

class RanobelibLoader:

    def __init__(self, access_token: str) -> None:
        self.__token = access_token
        self._dom_parser = DOMParser(schema, RULES) # type: ignore

    
    def __get_session(self) -> Session:
        session = requests.session()
        session.headers = {
            "authorization": self.__token,
            "content-type": "application/json",
            "referer": "https://ranobelib.me/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
        }
        return session
    
    def load_chapter(
            self, 
            branch_id: int,
            text: str,
            manga_id: int,
            name: str,
            number: int,
            volume: int,
            teams: list[int],
            publish_at: str | datetime | None = None,
            pages: Any = [],
            expired_type: int = 0,
            attachments: Any = [],
            ) -> Response:
        """
        Args:
            branch_id (int): id ветки
            text (str): Текст новеллы (обычный/markdowm(md))
            manga_id (int): id новеллы
            name (str): Название главы
            number (int): Номер главы
            volume (int): Том
            teams (list[int]): id команды/команд
            publish_at (str | datetime | None, optional): Строка в формате YYYY-mm-dd HH:MM:SS или datetime или None. Время по UTC!
        """
        if publish_at:
            if isinstance(publish_at, str):
                publish_at = datetime.strptime(publish_at, "%Y-%m-%d %H:%M:%S")
            publish_at = publish_at.astimezone(timezone.utc)
            if datetime.now(tz=timezone.utc) >= publish_at:
                raise ValueError("Указывайте publish_at по UTC!")
        
        html = markdown(text)
        dom = lxml.html.fromstring(html)
        doc = self._dom_parser.parse(dom)
        
        data = {
            "branch_id": branch_id,
            "content": doc.to_json(),
            "expired_type": expired_type,
            "manga_id": manga_id,
            "name": name,
            "number": str(number),
            "volume": str(volume),
            "teams": teams,
            "publish_at": publish_at.strftime("%Y-%m-%d %H:%M:%S") if publish_at else None,
            "pages": pages,
            "attachments": attachments
        }

        
        with self.__get_session() as session:
            response = session.post(API_URL, json=data)
            return response
        

__version__ = "0.1.0"
__all__ = ["RanobelibLoader"]