"""
Utility functions for RealPython API interactions.
"""
import requests

class RealPythonUtil:
    """
    Utility class for RealPython API interactions.
    """

    @staticmethod
    def get_realpython(response):
        """
        Extract userId, title, completed from list of dicts.
        """
        payload = {
            "userId": [],
            "title": [],
            "completed": []
        }

        for item in response:
            payload["userId"].append(item.get("userId"))
            payload["title"].append(item.get("title"))
            payload["completed"].append(item.get("completed"))

        return payload

    





