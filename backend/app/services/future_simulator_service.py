from backend.app.services.career_simulator_service import (
    calculate_role_readiness
)


def simulate_future_readiness(
    current_skills,
    missing_skills,
    role
):

    current = calculate_role_readiness(
        current_skills,
        role
    )

    future_skills = (
        current_skills +
        missing_skills
    )

    future = calculate_role_readiness(
        future_skills,
        role
    )

    return {
        "current_readiness": current,
        "future_readiness": future,
        "improvement": round(
            future - current,
            2
        )
    }