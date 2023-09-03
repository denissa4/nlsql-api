import requests
from typing import Type

from nlsql_api.models import *


class NLSQL:

    def __init__(self, token, host="https://api.nlsql.com/v1/"):
        self.host: str = host
        self.token: Optional[str] = token
        self._headers: Header.model_dump = self._create_header()
        self._query_list_separator = ",|"
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

    def _url_data_source(self) -> str:
        return f"{self.host}data-source/"

    def _url_distinct_values(self) -> str:
        return f"{self.host}distinct_values"

    def get_data_source(self, data_source_name: str, params=None, **kwargs) -> requests.Response:
        if not data_source_name:
            raise TypeError(f"The <data_source_name> can't be empty")
        self._check_token()
        return requests.get(f"{self._url_data_source()}{data_source_name}", headers=self._headers,
                            params=params, **kwargs)

    def post_data_source(self, data: Optional[DataSource] = None, **kwargs) -> requests.Response:
        self._check_token()
        data = self._check_data(data)
        return requests.post(self._url_data_source(), headers=self._headers, data=data, **kwargs)

    def put_data_source(self, data: Optional[DataSource] = None, **kwargs) -> requests.Response:
        self._check_token()
        data = self._check_data(data)
        return requests.put(self._url_data_source(), headers=self._headers, data=data, **kwargs)

    def get_distinct_values(self, table_name: str, columns_names: List[str], params=None, **kwargs) \
            -> requests.Response:
        if not table_name or not columns_names:
            raise TypeError(f"The <table_name> and the <columns_names> can't be empty")
        self._check_token()
        columns_names = f"{self._query_list_separator}".join(columns_names)
        return requests.get(f"{self._url_distinct_values()}?table_name={table_name}&columns_names={columns_names}",
                            headers=self._headers, params=params, **kwargs)

    def put_distinct_values(self, data: Optional[DistinctValuesTable] = None, **kwargs) -> requests.Response:
        self._check_token()
        data = self._check_data(data, DistinctValuesTable)
        return requests.put(self._url_distinct_values(), headers=self._headers, data=data, **kwargs)

    def _check_token(self):
        if not self._token:
            raise ValueError("Set token value to make requests")

    @staticmethod
    def _check_data(data, d_type: Type[BaseModel] = DataSource):
        if not isinstance(data, d_type):
            raise ValueError(f"Data must be models.{d_type}, not {type(data)}")
        return data.model_dump_json(exclude_none=True)
