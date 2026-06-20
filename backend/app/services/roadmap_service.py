def build_unified_roadmap(
    learning_paths
):

    roadmap = []

    seen = set()

    for path in learning_paths.values():

        for skill in path:

            if skill not in seen:

                roadmap.append(skill)
                seen.add(skill)

    return roadmap