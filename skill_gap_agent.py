class SkillGapAgent:

    def analyze(self, resume_skills, job_skills):

        resume_set = set(
            skill.lower() for skill in resume_skills
        )

        job_set = set(
            skill.lower() for skill in job_skills
        )

        matched_skills = sorted(
            resume_set.intersection(job_set)
        )

        missing_skills = sorted(
            job_set.difference(resume_set)
        )

        total_required = len(job_set)

        if total_required > 0:
            match_percentage = round(
                (len(matched_skills) / total_required) * 100,
                2
            )
        else:
            match_percentage = 0

        return {
            "agent": "Skill Gap Agent",
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "match_percentage": match_percentage,
            "total_required_skills": total_required,
            "matched_skill_count": len(matched_skills),
            "missing_skill_count": len(missing_skills)
        }