NLSQL Python Client
======================
NLSQL Python Client enables Python programs to set up NLSQL Customization API.

Installation
------------

The recommended way to install nlsql-api is via [pip](https://pip.pypa.io/).


    shell> pip install nlsql-api

Getting Started
---------------


    import nlsql_api

    # Create connection
    nlsql = nlsql_api.client(token="<your_api_token>")

    # GET
    nlsql.get(data_source_name="<DataSource-1>")

    # Create body for [POST, PUT] requests
    table = models.Table(spreadsheet_link="<spreadsheet_link>", spreadsheet_sheet="<Sheet1>", table_name="<Table1>")
    body = models.Body(name="<DataSource-1>", db_syntax=8, platform=2, tables=[table])
    
    # POST
    nlsql.post(data=body)

    # PUT
    nlsql.put(data=body)
    
Please refer to the [NLSQL API Documentation](https://www.nlsql.com/documentation).

