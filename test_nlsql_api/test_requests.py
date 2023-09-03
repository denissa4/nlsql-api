import requests
import pytest
from httmock import all_requests, HTTMock

from nlsql_api import client, models

# create NLSQL client
nlsql = client(token="Token test_token")

# prepare valid data for [POST], [PUT] requests
table = models.Table(spreadsheet_link="spreadsheet_link", spreadsheet_sheet="Sheet1", table_name="Table1")
data_source = models.DataSource(name="DataSource-2", db_syntax=8, platform=2, tables=[table])

distinct_values = models.DistinctValues(label_name="ColumnName1", values=["Coca-Cola", "Sprite", "Fanta"])
distinct_values_table = models.DistinctValuesTable(table_name="TableName1", columns_distinct_values=[distinct_values])


@all_requests
def response_content(url, request: requests.models.PreparedRequest):

    def _check_auth():
        token = "Token test_token"
        return token == request.headers.get("Authorization")

    if not _check_auth():
        return {'status_code': 401}

    if request.method == "GET":
        return {'status_code': 200}

    if request.method == "POST":
        if request.body:
            return {'status_code': 201}

    if request.method == "PUT":
        if request.body:
            return {'status_code': 204}

    return {'status_code': 500}


def test_get_data_source():
    with HTTMock(response_content):
        r = nlsql.get_data_source(data_source_name="DataSource-1")
        assert r.status_code == 200


def test_post_data_source():
    with HTTMock(response_content):
        r = nlsql.post_data_source(data=data_source)
        assert r.status_code == 201


def test_put_data_source():
    with HTTMock(response_content):
        r = nlsql.put_data_source(data=data_source)
        assert r.status_code == 204


def test_get_distinct_values():
    with HTTMock(response_content):
        r = nlsql.get_distinct_values(table_name="Table1", columns_names=['column1', 'column2', 'column3'])
        assert r.status_code == 200


def test_put_distinct_values():
    with HTTMock(response_content):
        r = nlsql.put_distinct_values(data=distinct_values_table)
        assert r.status_code == 204
