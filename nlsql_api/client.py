import requests

from nlsql_api.models import *


class NLSQL:

    def __init__(self, token, host="https://api.nlsql.com/v1/data-source/"):
        self.host: str = host
        self.token: Optional[str] = token
        self._headers: Header.model_dump = self._create_header()

    # a getter function of token
    @property
    def token(self) -> Optional[str]:
        return self._token

    # a setter function of token
    @token.setter
    def token(self, value: str):
        if not isinstance(value, str):
            raise TypeError(f"The <token> must be str, not {type(value)}")
        self._token: Optional[str] = value

    def _create_header(self):
        return Header(Authorization=self._token).model_dump(by_alias=True)

    def get(self, data_source_name: str, params=None, **kwargs) -> requests.Response:
        if not data_source_name:
            raise TypeError(f"The <data_source_name> can't be empty")
        self._check_token()
        return requests.get(f"{self.host}{data_source_name}", headers=self._headers, params=params, **kwargs)

    def post(self, data: Optional[Body] = None, **kwargs) -> requests.Response:
        self._check_token()
        data = self._check_data(data)
        return requests.post(self.host, headers=self._headers, data=data, **kwargs)

    def put(self, data: Optional[Body] = None, **kwargs) -> requests.Response:
        self._check_token()
        data = self._check_data(data)
        return requests.put(self.host, headers=self._headers, data=data, **kwargs)

    def _check_token(self):
        if not self._token:
            raise ValueError("Set token value to make requests")

    @staticmethod
    def _check_data(data):
        if not isinstance(data, Body):
            raise ValueError(f"Data must be models.Body, not {type(data)}")
        return data.model_dump_json(exclude_none=True)
