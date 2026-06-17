from backend.app.graphrag.neo4j_connection import driver
from backend.app.services.gemini_service import (
    generate_response
)
from backend.app.services.role_service import (
    get_role_requirements
)


def skill_gap_analysis(known_skills):

    query = """
    MATCH (s:Skill)-[:PREREQUISITE_FOR*]->(target)

    WHERE s.name IN $known_skills

    RETURN DISTINCT target.name AS skill
    """

    with driver.session() as session:

        result = session.run(
            query,
            known_skills=known_skills
        )

        discovered_skills = {
            record["skill"]
            for record in result
        }

    missing_skills = list(
        discovered_skills - set(known_skills)
    )

    return missing_skills

def generate_career_roadmap(
    known_skills,
    target_role,
    missing_skills
):

    prompt = f"""
    User knows:

    {known_skills}

    User wants to become:

    {target_role}

    Missing skills:

    {missing_skills}

    Create:

    1. Skill gap analysis
    2. Recommended learning order
    3. 3-month roadmap
    4. Beginner-friendly explanation
    """

    return generate_response(prompt)


def role_based_gap_analysis(
    resume_skills,
    target_role
):

    required_skills = get_role_requirements(
        target_role
    )

    missing_skills = []

    resume_lower = {
        skill.lower()
        for skill in resume_skills
    }

    for skill in required_skills:

        if skill.lower() not in resume_lower:
            missing_skills.append(skill)

    return missing_skills