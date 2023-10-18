filtered_df = data_input.groupby('conversation_id').apply(lambda x: x.loc[x['transcript'].apply(len).idxmax()])
