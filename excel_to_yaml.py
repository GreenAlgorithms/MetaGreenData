import pandas as pd
import yaml

file_path = "Draft metadata fields.xlsx"
df = pd.read_excel(file_path)

df.columns = ['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5', 'Level 6', 'Level 7']

df_ffill = df[1:].copy()  # Skip header row
df_ffill.fillna(method='ffill', axis=0, inplace=True)

# Function to build clean nested dictionary, skipping NaN values
def build_clean_nested_dict(df, levels):
    root = {}
    for _, row in df.iterrows():
        current = root
        keys = [row[level] for level in levels if pd.notna(row[level])]
        for key in keys[:-1]:
            current = current.setdefault(key, {})
        if keys:
            current[keys[-1]] = {}
    return root

levels = ['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5', 'Level 6','Level 7']

nested_dict = build_clean_nested_dict(df_ffill, levels)
yaml_output = yaml.dump(nested_dict, sort_keys=False, allow_unicode=True)

output_file = "metadata_fields.yaml"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(yaml_output)

print(f"YAML file saved as: {output_file}")
