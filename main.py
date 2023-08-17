def extract_pretty_transcript(x):
    try:
        transcript_data = json.loads(x)
        pretty_transcripts = [item.get('pretty_transcript') for item in transcript_data['transcript'] if item.get('pretty_transcript') is not None]
        return ' '.join(pretty_transcripts)
    except (ValueError, KeyError):
        return None

# Apply the function to the 'TRANSCRIPT_TXT' column
df['Pretty_Transcripts'] = df['TRANSCRIPT_TXT'].apply(extract_pretty_transcript)

print(df)
