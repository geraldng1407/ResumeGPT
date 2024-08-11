import os

from datetime import datetime


import utils
import json


from job_extractor import Job_Extractor
from resume_builder import Resume_Builder
from latex_template import get_modules, get_end, get_header, get_education, get_skills, get_experience, get_projects, get_certificates
latex_string = ""
latex_string += get_modules()
latex_string += get_header()
latex_string += get_education()

job_file = "job.txt"
raw_resume_file = "raw_resume.json"
directory = './results'

job_post = utils.read_jobfile(job_file)

job_extractor = Job_Extractor()
job_description = job_extractor.extract_description(job_post)


job_skills = job_extractor.extract_skills(job_post)


with open(raw_resume_file, 'r') as file:
    resume = json.load(file)


resume_builder = Resume_Builder(resume, job_description, job_post, job_skills)
skills = resume_builder.write_skills()


latex_string += get_skills(skills)
experiences = resume_builder.write_experinence()
latex_string += get_experience(experiences)

projects = resume_builder.write_projects()
latex_string += get_projects(projects)

certificates = resume_builder.write_certificate()
if len(certificates) > 0:
    latex_string += get_certificates(certificates)

latex_string += get_end()

file_name = "Resume.tex"
file_path = os.path.join(directory, file_name)

with open(file_path, 'w') as file:
    file.write(latex_string)
    
os.system(f"cd results && pdflatex -interaction=nonstopmode Resume.tex")

new_file_name_tex = f"{job_description['company']} - {job_description['job_title']}.tex"
new_file_name_pdf = f"{job_description['company']} - {job_description['job_title']}.pdf"

new_file_path_tex = os.path.join(directory, new_file_name_tex)
new_file_path_pdf = os.path.join(directory, new_file_name_pdf)

os.rename(file_path, new_file_path_tex)
os.rename("results/Resume.pdf", new_file_path_pdf)
os.remove("results/Resume.aux")
os.remove("results/Resume.log")
