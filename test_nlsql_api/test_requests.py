import requests
import pytest
from httmock import all_requests, HTTMock

from nlsql_api import client, models

# create NLSQL client
nlsql = client.NLSQL(token="Token test_token")

# prepare valid data for [POST], [PUT] requests
table = models.Table(spreadsheet_link="spreadsheet_link", spreadsheet_sheet="Sheet1", table_name="Table1")
body = models.Body(name="DataSource-2", db_syntax=8, platform=2, tables=[table])


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


def test_get():
    with HTTMock(response_content):
        r = nlsql.get(data_source_name="DataSource-1")
        assert r.status_code == 200


def test_post():
    with HTTMock(response_content):
        r = nlsql.post(data=body)
        assert r.status_code == 201


def test_put():
    with HTTMock(response_content):
        r = nlsql.put(data=body)
        assert r.status_code == 204
