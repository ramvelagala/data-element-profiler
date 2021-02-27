from data_elements_query import DataQuery

data_query = DataQuery()


def printing():
    print(data_query.total_rows)
    print(data_query.cardinality)
    print(data_query.perc_of_cardinality)
    print(data_query.num_null_values)
    print(data_query.min_value)
    print(data_query.max_value)
    print(data_query.median_value)
    print(data_query.freq_highest_value)
    print(data_query.freq_highest_count)
    print(data_query.freq_highest_perc)
    print(data_query.freq_lowest_value)
    print(data_query.freq_lowest_count)
    print(data_query.freq_lowest_perc)
    print(data_query.lowest_value)
    print(data_query.highest_value)
    print(data_query.median_value)


printing()
