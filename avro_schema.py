"""Data-profiling avro_schema."""

from .data_elements_query import DataQuery
import json

# data_query = DataQuery()


def schema(query_data, gen_format_items):
    """Generate avro-schema."""
    # query_data = DataQuery()
    # gen_format_items = query_data.format_generation()

    data = {
        "name": "Report",
        "properties": {
            "host_name": "query_data.host_name",
            "Data Store Name": "",
            "Database Name": "query_data.db_name",
            "Table Name": "query_data.table_name"
        },

        "type": "record",

        "fields": [
            {
                "name": "Column",
                "type": "string",
                "default": "column_name"
            },
            {
                "name": "inferred_data_class",
                "type": "string",
                "default": "code"
            },
            {
                "name": "count of -1 values",
                "type": "int",
                "default": int(query_data.count_err)
            },
            {
                "name": "perc of -1 values",
                "type": "float",
                "default": float(query_data.count_err_perc)
            },

            {
                "name": "MetaData",
                "type": {
                    "name": "MetaData",
                    "type": "record",
                    "fields": [{
                        "name": "Inferred",
                        "type": {
                            "name": "Inferred",
                            "type": "record",
                            "fields": [{
                                "name": "Data_type",
                                "type": "string",
                                "default": ""
                            },
                                {
                                    "name": "data_length",
                                    "type": "int",
                                    "default": ""
                                },
                                {
                                    "name": "Precision",
                                    "type": "int",
                                    "default": "query_data.num_perc"
                                },
                                {
                                    "name": "scale",
                                    "type": "int",
                                    "default": "query_data.num_scale"
                                },
                                {
                                    "name": "data_scale",
                                    "type": "int",
                                    "default": ""
                                }
                            ]
                        }
                    },
                        {
                            "name": "Defined",
                            "type": {
                                "name": "Defined",
                                "type": "record",
                                "fields": [{
                                    "name": "Data_type",
                                    "type": "string",
                                    "default": ""
                                },
                                    {
                                        "name": "data_length",
                                        "type": "int"
                                    },
                                    {
                                        "name": "Precision",
                                        "type": "int"
                                    },
                                    {
                                        "name": "scale",
                                        "type": "int"
                                    },
                                    {
                                        "name": "data_scale",
                                        "type": "int"
                                    }
                                ]
                            }
                        },
                        {
                            "name": "Defined",
                            "type": {
                                "name": "Defined",
                                "type": "record"
                            }
                        }
                    ]
                }
            },
            {
                "name": "domain_highlights",
                "type": ["", {
                    "name": "domain_highlights",
                    "type": "record",
                    "fields": [{
                        "name": "TotalRows",
                        "type": "int",
                        "default": int(query_data.total_rows)
                    },
                        {
                            "name": "Cardinality",
                            "type": "int",
                            "default": int(query_data.cardinality)
                        },
                        {
                            "name": "per_of_Cardinality",
                            "type": "int",
                            "default": float(query_data.perc_of_cardinality)
                        },
                        {
                            "name": "Nulls",
                            "type": "int",
                            "default": int(query_data.num_null_values)
                        },
                        {
                            "name": "no_of_general_formats",
                            "type": "int",
                            "default": int(len(gen_format_items))
                        },

                    ]
                }],
                "properties": [

                    {
                        "name": "general_formats",
                        "type": "array",
                        "default": list(gen_format_items),

                    },
                    {
                        "name": "Lowest Value",
                        "type": "string",
                        "default": str(query_data.lowest_value)
                    },
                    {
                        "name": "Highest Value",
                        "type": "string",
                        "default": str(query_data.highest_value)
                    },
                    {
                        "name": "Median Value",
                        "type": "string",
                        "default": str(query_data.median_value)
                    },
                    {
                        "name": "Least Frequent Value",
                        "type": "string",
                        "default": str(query_data.freq_lowest_value)
                    },
                    {
                        "name": "Lowest Frequency",
                        "type": "string",
                        "default": str(query_data.freq_lowest_count)
                    },
                    {
                        "name": "Lowest Frequency percentage",
                        "type": "string",
                        "default": query_data.freq_lowest_perc,
                    },
                    {
                        "name": "Highest Frequent Value",
                        "type": "string",
                        "default": str(query_data.freq_highest_value)
                    },
                    {
                        "name": "Highest Frequency",
                        "type": "string",
                        "default": str(query_data.freq_highest_count)
                    },
                    {
                        "name": "highest Frequency percentage",
                        "type": "string",
                        "default": ""
                    }
                ]
            },

            {
                "name": "domain_values",
                "type": "array",
                "fields": [{
                    "name": "top_25",
                    "type": "array",
                    "default": [""]
                },
                    {
                        "name": "bottom_25",
                        "type": "array",
                        "default": [""]
                    }
                ],

            }
        ]
    }
    print(type(data))
    result = json.dumps(data, indent=4)
    return result


print(schema())
