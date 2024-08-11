import os

from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers.openai_tools import JsonOutputKeyToolsParser
from langchain_openai import ChatOpenAI

from classes.parser_classes import Resume_Classifier, Resume_Experiences, Resume_Certification
from prompts import RESUME_CLASSIFIER, EXPERIENCE_REWRITER, CERTIFICATION

class Resume_Builder():
    def __init__(self, resume, job_description, job_post_raw, job_skills):
        self.resume = resume
        self.job_description = job_description
        self.job_post_raw = job_post_raw
        self.job_skills = job_skills
        self.llm = ChatOpenAI(model_name="gpt-4o",
                              api_key=os.environ["OPENAI_API_KEY"])
        
    def write_skills(self):
        self.llm = self.llm.bind_tools([Resume_Classifier])
        prompt_skills = ChatPromptTemplate.from_template(RESUME_CLASSIFIER)
        parser = JsonOutputKeyToolsParser(key_name='Resume_Classifier')
        self.parsed_job = (prompt_skills | self.llm | parser)
        self.categories = self.parsed_job.invoke({
            "job_description": self.job_post_raw,
        })
        
        res = {}
        for category in self.categories[0]['category']:
            if category == "software engineering":
                res['Front End'] = self.resume["skills"]["front_end"]
                res['Back End'] = self.resume["skills"]["back_end"]
            if category == "machine learning":
                res['Machine Learning'] = self.resume["skills"]["machine_learning"]
        return res
    
    def write_experinence(self):
        res = []
        for category in self.categories[0]['category']:
            if category == "software engineering":
                rewrite_responsibilities = self._rewrite_experiences(self.resume["experience"]["software_engineering"][0]["responsibilities"])
                temp = self.resume["experience"]["software_engineering"][0]
                temp['responsibilities'] = rewrite_responsibilities["responsibilities"]
                res.append(temp)
            elif category == "machine learning":
                rewrite_responsibilities = self._rewrite_experiences(self.resume["experience"]["machine_learning"][0]["responsibilities"])
                temp = self.resume["experience"]["machine_learning"][0]
                temp['responsibilities'] = rewrite_responsibilities["responsibilities"]
                res.append(temp)
        return res
    
    def _rewrite_experiences(self, responsibilities):
        self.llm = self.llm.bind_tools([Resume_Experiences])
        prompt_skills = ChatPromptTemplate.from_template(EXPERIENCE_REWRITER)
        parser = JsonOutputKeyToolsParser(key_name='Resume_Experiences')
        self.parsed_job = (prompt_skills | self.llm | parser)
        return self.parsed_job.invoke({
            "job_description": self.job_description["job_summary"],
            "resume_experience": responsibilities,
            "technical_skills": self.job_skills['technical_skills'],
            "non_technical_skills": self.job_skills['non_technical_skills']  
        })[0]
    
    def write_projects(self):
        res = []
        for category in self.categories[0]['category']:
            if category == "software engineering":
                if len(self.categories[0]['category']) > 1:
                    project = self.resume["projects"]["software_engineering"][0]
                    rewrite_responsibilities = self._rewrite_experiences(project["details"])
                    project["details"] = rewrite_responsibilities["responsibilities"]
                    res.append(project)
                else:
                    for project in self.resume["projects"]["software_engineering"]:
                        # project = self.resume["projects"]["software_engineering"][0]
                        rewrite_responsibilities = self._rewrite_experiences(project["details"])
                        project["details"] = rewrite_responsibilities["responsibilities"]
                        res.append(project)
                        
            elif category == "machine learning":
                if len(self.categories[0]['category']) > 1:
                    project = self.resume["projects"]["machine_learning"][0]
                    rewrite_responsibilities = self._rewrite_experiences(project["details"])
                    project["details"] = rewrite_responsibilities["responsibilities"]
                    res.append(project)
                else:
                    for project in self.resume["projects"]["machine_learning"]:
                        # project = self.resume["projects"]["machine_learning"][0]
                        rewrite_responsibilities = self._rewrite_experiences(project["details"])
                        project["details"] = rewrite_responsibilities["responsibilities"]
                        res.append(project)
        return res
    
    def write_certificate(self):
        res = []
        for certificate in self.resume["certifications"]:
            is_relevant = self._relevant_certification(certificate)
            if is_relevant:
                res.append(certificate)
        return res
    
    def _relevant_certification(self, certificate):
        self.llm = self.llm.bind_tools([Resume_Certification])
        prompt_skills = ChatPromptTemplate.from_template(CERTIFICATION)
        parser = JsonOutputKeyToolsParser(key_name='Resume_Certification')
        self.parsed_job = (prompt_skills | self.llm | parser)
        return self.parsed_job.invoke({
            "job_description": self.job_description["job_summary"],
            "technical_skills": self.job_skills['technical_skills'],
            "certification": certificate
        })[0]
        
            
    
        