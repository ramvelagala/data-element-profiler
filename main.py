value['TRANSCRIPT_TXT'].apply(lambda x: ' '.join(
        item.get('pretty_transcript') for item in json.loads(x)['transcript'] if item.get('pretty_transcript') is not None))

