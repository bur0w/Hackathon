# Final Program
import os
import pandas as pd
columns_to_keep = ['player_name', 'times_faced', 'events']
os.listdir('drive/My Drive')
df = pd.read_csv('drive/My Drive/savant_pitch_level.csv')

# Filter only relevant columns
mlb_data = df[columns_to_keep]

# Get rid of all the empty events
mlb_data = mlb_data.dropna(subset=['events'])

# Seperate the hits from the outs
hits = ['double', 'single',
       'home_run', 'triple']
outs = ['strikeout', 'field_out','force_out', 'grounded_into_double_play', 'fielders_choice','other_out','strikeout_double_play', 'fielders_choice_out',
'double_play', 'sac_fly_double_play', 'triple_play','sac_bunt_double_play',
  ]
# Isolate hit events into hits and out events into outs
mlb_data['is_hit'] = mlb_data['events'].isin(hits)
mlb_data['is_out'] = mlb_data['events'].isin(outs)

mlb_data['cumulative_hits'] = mlb_data.groupby(['player_name', 'times_faced'])['is_hit'].cumsum()
mlb_data['cumulative_pa'] = mlb_data.groupby(['player_name', 'times_faced']).cumcount() + 1
mlb_data['batting_average'] = mlb_data['cumulative_hits'] / mlb_data['cumulative_pa']

# Pivot the table to have separate columns for times_faced
result = mlb_data.pivot_table(index='player_name', columns='times_faced', values='batting_average', aggfunc='last')

# This differeinetates between first time through order, second time, and third time
result.columns = [f'batting_average_times_{col}' for col in result.columns]
result.reset_index(inplace=True)

# Subracts the two differences between the batting averages so it allows us to see which hitters struggle with consitisency
result['first_second_difference'] = result['batting_average_times_1'] - result['batting_average_times_2']
result['first_third_difference'] = result['batting_average_times_1'] - result['batting_average_times_3']

# Saves it to a file
result.to_csv('drive/My Drive/AVGPerTF.csv', index=False)


# Saves it to a file
result.to_csv('drive/My Drive/AVGPerTF.csv', index=False)



