from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from resume_agent import ResumeAnalysisAgent
from job_agent import JobIntelligenceAgent
from skill_gap_agent import SkillGapAgent
from career_agent import CareerOrchestrator


# =====================================================
# FASTAPI APPLICATION
# =====================================================

app = FastAPI(
    title="CareerLens AI Service",
    description="Multi-Agent AI Service for CareerLens AI",
    version="1.0"
)


# =====================================================
# CORS CONFIGURATION
# =====================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# =====================================================
# AI AGENTS
# =====================================================

resume_agent = ResumeAnalysisAgent()

job_agent = JobIntelligenceAgent()

skill_gap_agent = SkillGapAgent()

career_orchestrator = CareerOrchestrator()


# =====================================================
# REQUEST MODELS
# =====================================================

class ResumeRequest(BaseModel):
    text: str


class JobRequest(BaseModel):
    text: str


class SkillGapRequest(BaseModel):
    resume_skills: list[str]
    job_skills: list[str]


class CareerAnalysisRequest(BaseModel):
    resume_text: str
    job_text: str
    target_role: str = "AI/ML Engineer"


# =====================================================
# HOME
# =====================================================

@app.get("/")
def home():

    return {
        "message": "CareerLens AI Service is running 🚀",

        "team": "IDEALENS",

        "agents": [
            "Resume Analysis Agent",
            "Job Intelligence Agent",
            "Skill Gap Agent",
            "Career Strategy Agent",
            "Learning Plan Agent",
            "Interview Preparation Agent"
        ]
    }


# =====================================================
# RESUME AGENT
# =====================================================

@app.post("/api/agent/resume/analyze")
def analyze_resume(request: ResumeRequest):

    return resume_agent.analyze(
        request.text
    )


# =====================================================
# JOB AGENT
# =====================================================

@app.post("/api/agent/job/analyze")
def analyze_job(request: JobRequest):

    return job_agent.analyze(
        request.text
    )


# =====================================================
# SKILL GAP AGENT
# =====================================================

@app.post("/api/agent/skill-gap/analyze")
def analyze_skill_gap(
    request: SkillGapRequest
):

    return skill_gap_agent.analyze(
        request.resume_skills,
        request.job_skills
    )


# =====================================================
# CAREER ORCHESTRATOR
# =====================================================

@app.post("/api/career/analyze")
def analyze_career(
    request: CareerAnalysisRequest
):

    return career_orchestrator.analyze(

        request.resume_text,

        request.job_text,

        request.target_role

    )