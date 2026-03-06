"""
realpython.py 
Author(s): Saikumar Pandi <pandisaikumar.tech@gmail.com>
"""
import os 
import requests
import logging

log = logging.getLogger(os.path.basename(__file__))
log.setLevel(logging.INFO)

DEFAULT_TIMEOUT = 10

class RealPython:
    def __init__(self):
        self.headers = {}
        self.verify = True
        self.CAPTURE_RESPONSE_TIME = True
        self.RESPONSE_TIMES = {}

    def get(self, url, params=None, headers=None, timeout=DEFAULT_TIMEOUT):
        """
        This handles GET method

        :param url: URL to get
        :type url: str
        :param params: parameters for get
        :type params: dict
        :param headers: headers for get
        :type headers: dict
        :param timeout: timeout value for the request
        :type timeout: int
        :returns: Response object
        :rtype: requests.models.Response
        :raises Timeout: If the request exceeds the timeout value
        """
        if headers is None:
            headers = self.headers
        try:
            response = requests.get(url, params=params, timeout=timeout,
                                    headers=headers, verify=self.verify)
        except requests.exceptions.Timeout:
            log.error(
                "RESPONSE TIMEOUT EXCEPTION. Response exceeds {} sec".format(timeout))
            return None
        return response

    def put(self, url, payload=None, headers=None, **kwargs):
        """
        This handles PUT method

        :param url: URL to put
        :type url: str
        :param payload: payload for put
        :type payload: dict
        :param headers: headers for put
        :type headers: dict
        :param kwargs: Additional parameters for the request
        :returns: Response object
        :rtype: requests.models.Response
        :raises Timeout: If the request exceeds the timeout value
        """
        timeout = kwargs.get("timeout") if kwargs.get("timeout") else DEFAULT_TIMEOUT
        if headers is None:
            headers = self.headers

        try:
            content_type = headers.get('Content-Type', '').lower()

            if content_type in ['application/json']:
                response = requests.put(url, json=payload, headers=headers,
                                        timeout=timeout, verify=self.verify)
            elif content_type in ['application/x-www-form-urlencoded']:
                response = requests.put(url, data=payload, headers=headers,
                                        timeout=timeout, verify=self.verify)
            elif content_type in ['application/xml', 'text/xml', 'text/plain']:
                response = requests.put(url, data=payload, headers=headers,
                                        timeout=timeout, verify=self.verify)
            else:
                response = requests.put(url, data=payload, headers=headers,
                                        timeout=timeout, verify=self.verify)

        except requests.exceptions.Timeout:
            log.error(
                "RESPONSE TIMEOUT EXCEPTION. Response exceeds {} sec".format(timeout))
            return None

        return response

    def post(self, url, payload=None, headers=None, **kwargs):
        """
        This handles POST method

        :param url: URL to post
        :type url: str
        :param payload: payload for post
        :type payload: dict
        :param headers: headers for post
        :type headers: dict
        :param kwargs: Additional parameters for the request
        :returns: Response object
        :rtype: requests.models.Response
        :raises Timeout: If the request exceeds the timeout value
        """
        timeout = kwargs.get("timeout") if kwargs.get("timeout") else DEFAULT_TIMEOUT
        if headers is None:
            headers = self.headers

        try:
            content_type = headers.get('Content-Type', '').lower()

            if content_type in ['application/json']:
                response = requests.post(url, json=payload, headers=headers,
                                         timeout=timeout, verify=self.verify)
            elif content_type in ['application/x-www-form-urlencoded']:
                response = requests.post(url, data=payload, headers=headers,
                                         timeout=timeout, verify=self.verify)
            elif content_type in ['application/xml', 'text/xml', 'text/plain']:
                response = requests.post(url, data=payload, headers=headers,
                                         timeout=timeout, verify=self.verify)
            else:
                response = requests.post(url, data=payload, headers=headers,
                                         timeout=timeout, verify=self.verify)

        except requests.exceptions.Timeout:
            log.error(
                "RESPONSE TIMEOUT EXCEPTION. Response exceeds {} sec".format(timeout))
            return None

        return response

    def delete(self, url, headers=None, **kwargs):
        """
        This handles DELETE method

        :param url: URL to delete
        :type url: str
        :param headers: headers for delete
        :type headers: dict
        :param kwargs: Additional parameters for the request
        :returns: Response object
        :rtype: requests.models.Response
        :raises Timeout: If the request exceeds the timeout value
        """
        timeout = kwargs.get("timeout") if kwargs.get("timeout") else DEFAULT_TIMEOUT
        if headers is None:
            headers = self.headers

        try:
            content_type = headers.get('Content-Type', '').lower()
            if content_type in ['application/json', 'application/x-www-form-urlencoded']:
                # Usually, DELETE doesn't traditionally use body content,
                # but some APIs might accept a payload or params.
                response = requests.delete(url, headers=headers, timeout=timeout, verify=self.verify)
            else:
                response = requests.delete(url, headers=headers, timeout=timeout, verify=self.verify)

        except requests.exceptions.Timeout:
            log.error(
                "RESPONSE TIMEOUT EXCEPTION. Response exceeds {} sec".format(timeout))
            return None
        return response

