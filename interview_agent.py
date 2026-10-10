class InterviewPreparationAgent:

    def analyze(
        self,
        resume_skills,
        job_skills,
        missing_skills,
        target_role="AI/ML Engineer"
    ):

        questions = []

        # Questions based on candidate skills
        skill_questions = {
            "python":
                "Explain the difference between a list, tuple and set in Python.",

            "java":
                "Explain the main principles of Object-Oriented Programming in Java.",

            "sql":
                "Explain the difference between INNER JOIN and LEFT JOIN.",

            "machine learning":
                "What is the difference between supervised and unsupervised learning?",

            "artificial intelligence":
                "What is Artificial Intelligence and how is it different from Machine Learning?",

            "nlp":
                "What is NLP and where is it used in real-world applications?",

            "docker":
                "What is Docker and why is it useful for deploying applications?",

            "aws":
                "What are some commonly used AWS services for deploying applications?",

            "rest api":
                "What is a REST API and what are the common HTTP methods?",

            "flask":
                "What is Flask and how can it be used to build a REST API?"
        }

        for skill in resume_skills:

            skill_lower = skill.lower()

            if skill_lower in skill_questions:

                questions.append({
                    "type": "Technical",
                    "skill": skill,
                    "question": skill_questions[skill_lower]
                })

        # Questions based on missing skills
        for skill in missing_skills[:3]:

            questions.append({
                "type": "Skill Gap",
                "skill": skill,
                "question":
                    f"What do you know about {skill} and how would you learn or apply it?"
            })

        # General interview questions
        questions.extend([
            {
                "type": "HR",
                "question":
                    "Tell me about yourself and your technical background."
            },
            {
                "type": "HR",
                "question":
                    "Explain one of your most important projects."
            },
            {
                "type": "HR",
                "question":
                    "What challenges did you face while developing your project?"
            },
            {
                "type": "HR",
                "question":
                    "Why are you interested in this role?"
            }
        ])

        return {
            "agent": "Interview Preparation Agent",
            "target_role": target_role,
            "total_questions": len(questions),
            "questions": questions[:15]
        }