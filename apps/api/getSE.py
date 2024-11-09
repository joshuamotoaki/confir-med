import pandas as pd
import ast
polypharm_side_effects_df = pd.read_csv('apps/api/drug-data/polypharm_side_effects.csv')

drug_1="Aluminum hydroxide" # Kremil S
drug_2="Ibuprofen" # Alaxan

side_effects = polypharm_side_effects_df[
    ((polypharm_side_effects_df['Drug 1'] == drug_1) & (polypharm_side_effects_df['Drug 2'] == drug_2)) |
    ((polypharm_side_effects_df['Drug 1'] == drug_2) & (polypharm_side_effects_df['Drug 2'] == drug_1))
]

if not side_effects.empty:
    # Get the side effects list
    side_effects_list = side_effects.iloc[0]['Side Effects']
    if isinstance(side_effects_list, str):
        side_effects_list = ast.literal_eval(side_effects_list)
    format_se = [side_effect.title() for side_effect in side_effects_list]
    print(f"Side effects for {drug_1} and {drug_2}: {format_se}")
else:
    print(f"No side effects found for the drug pair {drug_1} and {drug_2}.")