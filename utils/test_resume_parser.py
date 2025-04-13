from utils.resume_parser import extract_text
import os

#base_dir = os.getcwd()  # current working directory
#resume_path = os.path.join(base_dir,"Resume.pdf")

resume_path = "/workspaces/resume_review_aiagent/data/resumes/Resume.pdf"

print(resume_path)

text = extract_text(resume_path)

print(len(text))  # Print first 1000 characters
