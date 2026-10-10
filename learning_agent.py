class LearningPlanAgent:

    def analyze(self, priority_skills, target_role="AI/ML Engineer"):

        skill_resources = {
            "python": "Practice Python programming and problem solving",
            "machine learning": "Study supervised and unsupervised learning and build ML models",
            "deep learning": "Learn neural networks, CNNs and model training",
            "nlp": "Learn text processing, embeddings and NLP applications",
            "llm": "Learn LLM concepts, prompting and RAG",
            "docker": "Learn Docker containers and containerize an AI application",
            "aws": "Learn AWS fundamentals and basic cloud deployment",
            "fastapi": "Build REST APIs using FastAPI",
            "rest api": "Learn REST API design and integration",
            "langchain": "Build an application using LangChain",
            "langgraph": "Learn agent workflows using LangGraph",
            "sql": "Practice SQL queries and database design"
        }

        weekly_plan = []

        for index, skill in enumerate(priority_skills[:4]):

            skill_lower = skill.lower()

            action = skill_resources.get(
                skill_lower,
                f"Learn {skill} and build a small practical project"
            )

            weekly_plan.append({
                "week": index + 1,
                "skill": skill,
                "action": action
            })

        projects = []

        if priority_skills:

            projects.append(
                f"Build a practical {priority_skills[0]} project"
            )

        if len(priority_skills) >= 2:

            projects.append(
                f"Build a project combining "
                f"{priority_skills[0]} and {priority_skills[1]}"
            )

        return {
            "agent": "Learning Plan Agent",
            "target_role": target_role,
            "weekly_plan": weekly_plan,
            "recommended_projects": projects,
            "duration": f"{len(weekly_plan)} weeks"
        }