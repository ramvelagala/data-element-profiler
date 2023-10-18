import pandas as pd
import numpy as np

# Sample DataFrame
data = {'date': ['2023-10-01', '2023-10-01', '2023-10-01', '2023-10-02', '2023-10-02'],
        'classification': ['intime', 'intime', 'oot', 'intime', 'oot']}
df = pd.DataFrame(data)

# Group by date and apply your conditions
def assign_split(group):
    if 'oot' in group['classification'].values:
        group['split'] = 'validation'
    else:
        group_size = len(group)
        train_size = int(0.8 * group_size)
        test_size = group_size - train_size
        group['split'] = np.concatenate([['train'] * train_size, ['test'] * test_size])
    return group

df = df.groupby('date').apply(assign_split)

# Reset the index and drop the groupby index
df = df.reset_index(drop=True)

print(df)

