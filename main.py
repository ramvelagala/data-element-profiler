first_row_explode[columns_to_extract] = first_row_explode["TRANSCRIPT_TXT"].apply(lambda x: pd.Series({key: x[key] for key in columns_to_extract if x and x != ""  else None}))

