import pandas as pd

projects_df = pd.read_csv(
    "datasets/projects.csv"
)

def recommend_projects(
    missing_skills
):

    recommendations = []

    for _, row in projects_df.iterrows():

        project_skills = [
            s.strip()
            for s in row["skills"].split(",")
        ]

        overlap = len(
            set(project_skills)
            &
            set(missing_skills)
        )

        if overlap > 0:

            recommendations.append({
                "name": row["project_name"],
                "skills": project_skills,
                "score": overlap
            })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations[:5]