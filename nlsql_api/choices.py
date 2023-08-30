from enum import IntEnum


class DbSyntaxEnum(IntEnum):
    google_spreadsheets = 1
    mysql = 2
    mssql = 3
    cql = 4
    postgesql = 5
    redshift = 6
    bigquery = 7
    sqlite = 8
    snowflake = 9


class PlatformEnum(IntEnum):
    messengers = 1
    api = 2


class OperationEnum(IntEnum):
    sum = 1
    avg = 2
    count = 3
    value = 4
    max = 5
    min = 6


class OperationComplexEnum(IntEnum):
    sum = 1
    avg = 2
    count = 3
    max = 4
    min = 5
    value = 6


class DataTypeEnum(IntEnum):
    string = 1
    number = 2
    date = 3
    list_of_strings = 4
    list_of_numbers = 5


class DataTypeEnumComplex(IntEnum):
    string = 1
    number = 2
    date = 3
    date_quarter = 4
    date_month = 5


class OperatorEnum(IntEnum):
    equal = 1
    not_equal = 2
    over_than = 3
    lover_than = 4


class OperatorComplexEnum(IntEnum):
    division = 1
    multiplication = 2
    subtraction = 3
    addition = 4
    datediff_in_days = 5
    datediff_in_hours = 6


class FormatEnum(IntEnum):
    country_names = 1
    usa_states = 2
    iso_3 = 3


class FilterOperationEnum(IntEnum):
    none = 1
    month = 2
    year = 3


class FilterValueQuarterEnum(IntEnum):
    this_quarter = 1
    previous_quarter = 2
    q1 = 3
    q2 = 4
    q3 = 5
    q4 = 6
    none = 7


class FilterValueMonthEnum(IntEnum):
    this_month = 1
    previous_month = 2
    none = 3


class FilterValueYearEnum(IntEnum):
    this_year = 1
    previous_year = 2
    none = 3


class Enum(IntEnum):
    messengers = 1
    api = 2

