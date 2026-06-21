import pandas as pd

df = pd.read_csv("datasets/resources.csv")

resource_db = {}

for _, row in df.iterrows():
    resource_db[row["skill"]] = {
        "docs": row["docs"],
        "course": row["course"],
        "project": row["project"]
    }

def get_resources(skill):
    return resource_db.get(
        skill,
        {
            "docs": "Not Available",
            "course": "Not Available",
            "project": "Not Available"
        }
    )