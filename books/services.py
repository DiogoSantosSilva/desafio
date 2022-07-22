import logging
import requests
from requests.exceptions import HTTPError, ConnectionError
from typing import List


class RequestBookApi:
    def __init__(self):
        self.BASE_URL = "https://gutendex.com"
        self.book_list = []

    def get(self, **kwargs) -> dict:
        """
        Handle the requests to book API
        """
        query_param = self.generate_query_param(kwargs)
        try:
            url = f"{self.BASE_URL}/books{query_param}"
            response = requests.get(url)
            response.raise_for_status()
        except ConnectionError as error:
            logging.error(f"{error}")
            return {}
        except HTTPError as error:
            logging.error(f"{error}")
            return {}
        except Exception as error:
            logging.error(f"{error}")
            return {}

        return {"books": self.sanitize(response.json())}

    def sanitize(self, books: List) -> dict:
        """
        Clean unnecessary attributes
        """
        for book in books["results"]:
            self.book_list.append(
                {
                    "id": book["id"],
                    "title": book["title"],
                    "authors": book["authors"],
                    "languages": book["languages"],
                    "download_count": book["download_count"],
                }
            )

        return self.book_list

    def generate_query_param(self, parameters: dict) -> str:
        """
        Generate a query param structure from a python dict
        """
        query = ""
        for key, value in parameters.items():
            query += "".join(f"?{key}={value}")
        return query
