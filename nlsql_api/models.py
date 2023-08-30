from typing import List, Optional, TypedDict

from pydantic import BaseModel, Field, ValidationError, model_validator

from .choices import *


# Header = TypedDict('Header',
#                    {'Authorization': str,
#                     'Content-Type': str
#                     })


class Header(BaseModel):
    Authorization: str
    Content_Type: str = Field(alias="Content-Type", default="application/json")


class DataSource(BaseModel):
    name: str
    db_syntax: DbSyntaxEnum
    platform: PlatformEnum = PlatformEnum.api
    suggestion_mode: bool = False
    additional_regular_exp_symbols: str = ""


class Arguments(BaseModel):
    argument: str
    operation: OperationEnum


class Dates(BaseModel):
    date_argument: Optional[str] = None
    is_default: bool


class TopArguments(BaseModel):
    top_argument: str


class Filters(BaseModel):
    argument: Optional[str] = None
    data_type: DataTypeEnum
    operator: OperatorEnum
    value: str


class MapsColumn(BaseModel):
    format: FormatEnum


class ColumnOtherParams(BaseModel):
    arguments: Optional[List[Arguments]] = None
    dates: Optional[List[Dates]] = None
    top_arguments: Optional[List[TopArguments]] = None
    filters: Optional[List[Filters]] = None
    maps_column: Optional[List[MapsColumn]] = None


class Columns(BaseModel):
    label_name: str
    default_label_name: str
    column_other_params: Optional[List[ColumnOtherParams]] = None


class ComplexArguments(BaseModel):
    argument: str
    column_1: str
    column_2: str
    operation_1: OperationComplexEnum
    operation_2: OperationComplexEnum
    operator: OperatorComplexEnum
    filter_column_1: Optional[str] = None
    filter_column_2: Optional[str] = None
    data_type_1: Optional[DataTypeEnumComplex] = None
    data_type_2: Optional[DataTypeEnumComplex] = None
    filter_operation_1: Optional[FilterOperationEnum] = None
    filter_operation_2: Optional[FilterOperationEnum] = None
    filter_value_1: Optional[str] = None
    filter_value_1_end: Optional[str] = None
    filter_value_2: Optional[str] = None
    filter_value_2_end: Optional[str] = None
    filter_value_quarter_1: Optional[FilterValueQuarterEnum] = None
    filter_value_quarter_2: Optional[FilterValueQuarterEnum] = None
    filter_value_month_1: Optional[FilterValueMonthEnum] = None
    filter_value_month_2: Optional[FilterValueMonthEnum] = None
    filter_value_year_1: Optional[FilterValueYearEnum] = None
    filter_value_year_2: Optional[FilterValueYearEnum] = None

    @model_validator(mode='after')
    def check_filter_operation(self) -> "ComplexArguments":
        if self.filter_operation_1 in [2, 3] and self.data_type_1 != 3:
            raise ValidationError('filter_operation_1 is only available for data_type_1 is 3 (Date)')
        if self.filter_operation_2 in [2, 3] and self.data_type_2 != 3:
            raise ValidationError('filter_operation_2 is only available for data_type_2 is 3 (Date)')
        return self

    @model_validator(mode='after')
    def check_filter_value(self) -> "ComplexArguments":
        if (self.filter_value_1 or self.filter_value_1_end) and self.filter_operation_1 not in [2, 3]:
            raise ValidationError('filter_value_1/filter_value_1_end is only available for '
                             'filter_operation_1 is 2 (Month) or 3 (Year).')
        if (self.filter_value_2 or self.filter_value_2_end) and self.filter_operation_2 not in [2, 3]:
            raise ValidationError('filter_value_2/filter_value_2_end is only available for '
                             'filter_operation_2 is 2 (Month) or 3 (Year).')
        if self.filter_value_1_end and not self.filter_value_1:
            raise ValidationError('filter_value_1_end is only available if filter_value_1 is used')
        if self.filter_value_2_end and not self.filter_value_2:
            raise ValidationError('filter_value_2_end is only available if filter_value_2 is used')
        return self

    @model_validator(mode='after')
    def check_filter_value_quarter(self) -> "ComplexArguments":
        if self.filter_value_quarter_1 and self.data_type_1 != 4:
            raise ValidationError('filter_value_quarter_1 is only available for '
                             'data_type_1 is 4 (Date Quarter).')
        if self.filter_value_quarter_2 and self.data_type_2 != 4:
            raise ValidationError('filter_value_quarter_2 is only available for '
                             'data_type_2 is 4 (Date Quarter).')
        return self

    @model_validator(mode='after')
    def check_filter_value_month(self) -> "ComplexArguments":
        if self.filter_value_month_1 and self.data_type_1 != 5:
            raise ValidationError('filter_value_month_1 is only available for '
                             'data_type_1 is 5 (Date Month).')
        if self.filter_value_month_2 and self.data_type_2 != 5:
            raise ValidationError('filter_value_month_2 is only available for '
                             'data_type_2 is 5 (Date Month).')
        return self

    @model_validator(mode='after')
    def check_filter_value_year(self) -> "ComplexArguments":
        if self.filter_value_year_1 and self.data_type_1 not in [4, 5]:
            raise ValidationError('filter_value_year_1 is only available for '
                             'data_type_1 is 4 (Date Quarter) or 5 (Date Month).')
        if self.filter_value_year_1 and self.data_type_2 not in [4, 5]:
            raise ValidationError('filter_value_year_2 is only available for '
                             'data_type_2 is 4 (Date Quarter) or 5 (Date Month).')
        return self


class ColumnArg(BaseModel):
    argument: str
    column: str
    column_value: str
    operation: OperationEnum


class Table(BaseModel):
    spreadsheet_link: str
    spreadsheet_sheet: str
    table_name: str
    is_first_line: bool = False
    db_schema: str = ""
    columns: Optional[List[Columns]] = None
    complex_arguments: Optional[List[ComplexArguments]] = None
    column_arg: Optional[List[ColumnArg]] = None


class Joins(BaseModel):
    # Option: Class method validation with context of table name and column names.
    master_table: str
    master_column: str
    join_table: str
    join_column: str


class Body(DataSource):
    tables: Optional[List[Table]] = []
    joins: Optional[List[Joins]] = None
