JOB_DESCRIPTION = """
You are a world class algorithm for extracting information in structured formats.
Use the given format to extract information from the following input:
The job destion is as follows: {input}
Tips: Make sure to answer in the correct format.
"""

JOB_SKILLS ="""
You are a world class algorithm for extracting information in structured formats.
Extract the technical skills from the job description.
Extract the non-technical skills from the job description.
Always output both techincal and non-technical skills in a list format.
The job destion is as follows: {input}
Output in JSON format.
"""

# RESUME_SKILLS = """
# You are an expert resume writer. 
# Your goal is to strictly follow all the provided <Steps> and meet all the given <Criteria>.
# <Job Posting>
# The ideal candidate has the following skills: {technical_skills}
# <Resume>
# Current skills include: {skills}
# <Intructions>
# Extract skills from the <Resume> that match the skills required in the <Job Posting>.
# <Criteria>
# Each skill must be based on what is mentioned in the <Resume>
# Skills are caateogrized into  cateogries such as Frontend, Backend, Machine Learning.
# <Steps>
# - Create a <Plan> for following the <Instruction> while meeting all the <Criteria>.
# - What <Additional Steps> are needed to follow the <Plan>?
# - Follow all steps one by one and show your <Work>
# - Verify that skills are reflective of the <Resume> and not the <Job Posting>. Update if necessary.
# - Verify that all <Criteria> are met, and update if necessary.
# - Output in JSON format.
# """

# RESUME_SKILLS = """
# You are an expert resume writer.

# Task: Select skills from {resume_skills} that are common or similar to the technical skills listed in {job_posting_skills}.

# Inputs:
# - {resume_skills}: A list of skills from the resume.
# - {job_posting_skills}: A list of technical skills required by the job posting.

# Instructions:
# Identify skills that are either common (exact matches) or similar between the resume and the job posting.
# Output only these common or similar skills in a single list.

# Output: Provide the matched skills in JSON format as an array of strings.
# """

# RESUME_SKILLS = """
# Task: Generate skills that are aligned with the skills in both my resume and the job posting.
#  Inputs:
#  - {resume_skills}: A list of skills from the resume.
#  - {job_posting_skills}: A list of technical skills required by the job posting.
#  Output: Matched skills in JSON format as an array of strings.
# """

RESUME_CLASSIFIER = """
You are an expoert classifier of jobs.
Task: Classify the job posting based on the job listing.
Inputs:
- {job_description}: Description of the job posting.
Output: The type of job based on the job posting.
"""

EXPERIENCE_REWRITER = """
You are an expert in rewriting experiences for jobs to fit the ideal candidate.
Task: Rewrite the experiences for the job posting that matches the ideal candidate's skills and qualifications.
Inputs:
- {job_description}: Description of the job posting.
- {resume_experience}: Experience from the resume.
- {technical_skills}: Technical skills required by the job posting.
- {non_technical_skills}: Non-technical skills required by the job posting.
Note: Do not alter the original experiences. Rewrite them to match the job posting.
Output (JSON format):
"""

CERTIFICATION = """
You are a world class algorithm to decide if a certification is relevant to a job posting.
Task: Determine if the certification is relevant to the job posting.
Inputs:
- {job_description}: Description of the job posting.
- {technical_skills}: Technical skills required by the job posting.
- {certification}: Certification mentioned in the resume.
Output: A boolean value indicating if the certification is relevant to the job posting.
"""

