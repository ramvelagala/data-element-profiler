formatted_dates = np.array([dt.strftime('%Y-%m-%d %H:%M:%S') for dt in datetime_array])

# Print the formatted dates
for date in formatted_dates:
    print(date)
