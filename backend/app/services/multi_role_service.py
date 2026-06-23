from backend.app.graphrag.neo4j_connection import driver
from backend.app.services.career_simulator_service import (
    calculate_role_readiness
)

def get_all_roles():

    with driver.session() as session:

        result = session.run(
            """
            MATCH (r:Role)
            RETURN r.name AS role
            """
        )

        return [
            record["role"]
            for record in result
        ]
        
def get_role_rankings(
    user_skills
):

    roles = get_all_roles()

    scores = {}

    for role in roles:

        scores[role] = calculate_role_readiness(
            user_skills,
            role
        )

    return dict(
        sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )