from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List, Literal


class Job_Description(BaseModel):
    """Description of a job posting"""

    company: str = Field(
        ..., description="Name of the company that has the job opening"
    )
    job_title: str = Field(..., description="Job title")
    job_summary: str = Field(
        ..., description="Brief summary of the job, not exceeding 100 words"
    )
    duties: List[str] = Field(
        ...,
        description="The role, responsibilities and duties of the job as an itemized list, not exceeding 500 words",
    )
    qualifications: List[str] = Field(
        ...,
        description="The qualifications, skills, and experience required for the job as an itemized list, not exceeding 500 words",
    )
    
    
class Job_Skills(BaseModel):
    """Skills required for a job posting"""
    technical_skills: List[str] = Field(
        ...,
        description="An list of technical skills, including programming languages, technologies, and tools.",
    )
    non_technical_skills: List[str] = Field(
        ...,
        description="An list of non-technical Soft skills.",
    )


# class Resume_Skill(BaseModel):
#     skill_category: str = Field(
#         ..., description="Category of the skill")
#     skills: List[str] = Field(...,
#                               description="List of skills in the category")

# class Resume_Skills(BaseModel):
#     skills: List[Resume_Skill] = Field(...,
#                                        description="List of skill categories and their respective skills")

# class Resume_Skills(BaseModel):
#     technical_skills: List[str] = Field(
#         ...,
#         description="Skills from the resume that match or is similar to the technical skills required by the job posting.",
#     )

class Resume_Classifier(BaseModel):
    category: List[Literal["machine learning", "software engineering"]] = Field(..., description="Type of job based on the job posting.")
    
    
class Resume_Experiences(BaseModel):
    responsibilities: List[str] = Field(
        ...,
        description="List of experiences and responsibilities for a job posting that matches the ideal candidate's skills and qualifications.",
    )
    
class Resume_Certification(BaseModel):
    certification: bool = Field(
        ...,
        description="True or False if the certification is relevant to the job posting.",
    )