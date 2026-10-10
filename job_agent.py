class JobIntelligenceAgent:

    def __init__(self):

        self.skills = [
            "python",
            "java",
            "c",
            "c++",
            "javascript",
            "typescript",
            "html",
            "css",
            "react",
            "spring boot",
            "sql",
            "mysql",
            "mongodb",
            "postgresql",
            "git",
            "github",
            "docker",
            "aws",
            "azure",
            "machine learning",
            "deep learning",
            "artificial intelligence",
            "data science",
            "pandas",
            "numpy",
            "scikit-learn",
            "tensorflow",
            "pytorch",
            "flask",
            "fastapi",
            "rest api",
            "nlp",
            "natural language processing",
            "llm",
            "langchain",
            "langgraph"
        ]

    def analyze(self, text):

        text_lower = text.lower()

        detected_skills = []

        for skill in self.skills:
            if skill.lower() in text_lower:
                detected_skills.append(skill)

        experience = self.extract_experience(text_lower)
        responsibilities = self.extract_responsibilities(text)

        return {
            "agent": "Job Intelligence Agent",
            "required_skills": detected_skills,
            "skill_count": len(detected_skills),
            "experience": experience,
            "responsibilities": responsibilities
        }

    def extract_experience(self, text):

        experience_keywords = [
            "experience",
            "years",
            "year",
            "fresher",
            "internship",
            "developer",
            "engineer"
        ]

        found = []

        for keyword in experience_keywords:
            if keyword in text:
                found.append(keyword)

        return list(set(found))

    def extract_responsibilities(self, text):

        lines = text.split("\n")

        responsibilities = []

        keywords = [
            "responsible",
            "develop",
            "design",
            "build",
            "implement",
            "maintain",
            "analyze",
            "collaborate"
        ]

        for line in lines:

            line_lower = line.lower()

            for keyword in keywords:

                if keyword in line_lower:
                    responsibilities.append(line.strip())
                    break

        return responsibilities[:10]