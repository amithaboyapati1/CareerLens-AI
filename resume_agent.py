class ResumeAnalysisAgent:

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

        education = self.extract_education(text_lower)
        projects = self.extract_projects(text)
        experience = self.extract_experience(text)
        certifications = self.extract_certifications(text)

        return {
            "agent": "Resume Analysis Agent",
            "skills": detected_skills,
            "skill_count": len(detected_skills),
            "education": education,
            "projects": projects,
            "experience": experience,
            "certifications": certifications
        }

    def extract_education(self, text):

        education_keywords = [
            "b.tech",
            "btech",
            "b.e",
            "bachelor",
            "m.tech",
            "mtech",
            "master",
            "degree",
            "university",
            "college"
        ]

        found = []

        for keyword in education_keywords:
            if keyword in text:
                found.append(keyword)

        return list(set(found))

    def extract_projects(self, text):

        lines = text.split("\n")

        projects = []

        for line in lines:
            if "project" in line.lower():
                projects.append(line.strip())

        return projects[:10]

    def extract_experience(self, text):

        keywords = [
            "internship",
            "intern",
            "experience",
            "developer",
            "engineer"
        ]

        found = []

        for keyword in keywords:
            if keyword in text.lower():
                found.append(keyword)

        return list(set(found))

    def extract_certifications(self, text):

        lines = text.split("\n")

        certifications = []

        for line in lines:
            if (
                "certificate" in line.lower()
                or "certification" in line.lower()
            ):
                certifications.append(line.strip())

        return certifications[:10]