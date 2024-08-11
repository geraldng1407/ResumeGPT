import os

from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers.openai_tools import JsonOutputKeyToolsParser
from langchain_openai import ChatOpenAI

from classes.parser_classes import Job_Description, Job_Skills
from prompts import JOB_DESCRIPTION, JOB_SKILLS


class Job_Extractor:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4o",
                            api_key=os.environ["OPENAI_API_KEY"])
        
    def extract_description(self, jd):
        self.llm = self.llm.bind_tools([Job_Description])
        prompt_description = ChatPromptTemplate.from_template(JOB_DESCRIPTION)
        parser = JsonOutputKeyToolsParser(key_name='Job_Description')

        self.parsed_job = (prompt_description | self.llm | parser)
        
        return self.parsed_job.invoke({
            "input": jd
        })[0]
        
    def extract_skills(self, jd):
        self.llm = self.llm.bind_tools([Job_Skills])
        prompt_skills = ChatPromptTemplate.from_template(JOB_SKILLS)
        parser = JsonOutputKeyToolsParser(key_name='Job_Skills')

        self.parsed_job = (prompt_skills | self.llm | parser)
        
        return self.parsed_job.invoke({
            "input": jd
        })[0]