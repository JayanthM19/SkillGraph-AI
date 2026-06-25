import json

with open("datasets/milestones.json", "r") as f:
    milestone_data = json.load(f)


def get_milestones(roadmap):

    milestones = []

    for skill in roadmap:

        milestones.append({
            "skill": skill,
            "milestone": milestone_data.get(
                skill,
                "Complete a practical project related to this skill."
            )
        })

    return milestones