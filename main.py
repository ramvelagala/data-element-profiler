first_row_explode["TRANSCRIPT_TXT"] = first_row_explode["TRANSCRIPT_TXT"].apply(lambda x: json.loads(x).get('transcript') if x is not "")
