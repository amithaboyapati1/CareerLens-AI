class CareerStrategyAgent:

    def analyze(self, missing_skills, target_role="AI/ML Engineer"):

        priority_order = [
            "python",
            "machine learning",
            "deep learning",
            "artificial intelligence",
            "sql",
            "nlp",
            "llm",
            "docker",
            "aws",
            "fastapi",
            "rest api",
            "langchain",
            "langgraph",
            "react",
            "java",
            "spring boot"
        ]

        prioritized_skills = []

        # Arrange missing skills according to priority
        for skill in priority_order:

            if skill.lower() in [
                s.lower() for s in missing_skills
            ]:
                prioritized_skills.append(skill)

        # Add any remaining missing skills
        for skill in missing_skills:

            if skill.lower() not in [
                s.lower() for s in prioritized_skills
            ]:
                prioritized_skills.append(skill)

        # Generate recommendations
        recommendations = []

        for skill in prioritized_skills[:5]:

            recommendations.append(
                f"Improve your knowledge of {skill}"
            )

        return {
            "agent": "Career Strategy Agent",
            "target_role": target_role,
            "priority_skills": prioritized_skills,
            "recommendations": recommendations,
            "next_action": (
                "Start learning the highest-priority "
                "missing skill and build a practical project."
            )
        }