from resume_agent import ResumeAnalysisAgent
from job_agent import JobIntelligenceAgent
from skill_gap_agent import SkillGapAgent
from career_strategy_agent import CareerStrategyAgent
from learning_agent import LearningPlanAgent
from interview_agent import InterviewPreparationAgent


class CareerOrchestrator:

    def __init__(self):

        self.resume_agent = ResumeAnalysisAgent()
        self.job_agent = JobIntelligenceAgent()
        self.skill_gap_agent = SkillGapAgent()
        self.strategy_agent = CareerStrategyAgent()
        self.learning_agent = LearningPlanAgent()
        self.interview_agent = InterviewPreparationAgent()

    def analyze(
        self,
        resume_text,
        job_text,
        target_role="AI/ML Engineer"
    ):

        # 1. Resume Analysis
        resume_result = self.resume_agent.analyze(
            resume_text
        )

        # 2. Job Analysis
        job_result = self.job_agent.analyze(
            job_text
        )

        # 3. Skill Gap Analysis
        skill_gap_result = self.skill_gap_agent.analyze(
            resume_result["skills"],
            job_result["required_skills"]
        )

        # 4. Career Strategy
        strategy_result = self.strategy_agent.analyze(
            skill_gap_result["missing_skills"],
            target_role
        )

        # 5. Learning Plan
        learning_result = self.learning_agent.analyze(
            strategy_result["priority_skills"],
            target_role
        )

        # 6. Interview Preparation
        interview_result = self.interview_agent.analyze(
            resume_result["skills"],
            job_result["required_skills"],
            skill_gap_result["missing_skills"],
            target_role
        )

        # Final result
        return {
            "system": "CareerLens AI",
            "orchestrator": "Career Orchestrator",

            "resume_analysis": resume_result,

            "job_analysis": job_result,

            "skill_gap_analysis": skill_gap_result,

            "career_strategy": strategy_result,

            "learning_plan": learning_result,

            "interview_preparation": interview_result
        }