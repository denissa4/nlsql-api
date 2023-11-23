NLSQL Python Client
======================
NLSQL Python Client enables Python programs to set up NLSQL Customization API. 
Please use POST to create and PUT for update or append you database structure.

Installation
------------

The recommended way to install nlsql-api is via [pip](https://pip.pypa.io/).


    shell> pip install nlsql-api

Getting Started
---------------
#### DataSource operations

    import nlsql_api

    # Create connection using <your_api_token>
    nlsql = nlsql_api.client(token="Token 1a2b3c4d")

    # GET
    response = nlsql.get_data_source(data_source_name="DataSource-1")
    print(response.json())

    # Create body for [POST, PUT] requests
    column1 = nlsql_api.models.Columns(label_name="ColumnName1")
    table1 = nlsql_api.models.Table(table_name="Table1", columns=[column1])
    data_source = nlsql_api.models.DataSource(name="DataSource-1", db_syntax=8, platform=2, tables=[table1])
    
    # POST
    nlsql.post_data_source(data=data_source)

    # PUT
    nlsql.put_data_source(data=data_source)


#### DistinctValues operations
    ...
    # GET
    response = nlsql.get_distinct_values(table_name="Table1", columns_names=['column1', 'column2', 'column3'])
    print(response.json())

    # PUT
    distinct_values = nlsql_api.models.DistinctValues(label_name="ColumnName1", values=["Coca-Cola", "Sprite", "Fanta"])
    distinct_values_table = nlsql_api.models.DistinctValuesTable(table_name="TableName1", columns_distinct_values=[distinct_values])

    nlsql.put_distinct_values(data=distinct_values_table)


Please refer to the [NLSQL API Documentation](https://www.nlsql.com/documentation).

