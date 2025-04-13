from agents.analyzer_agent import analyze_resume
from utils.resume_parser import extract_text

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Path to your sample resume
resume_path = "/workspaces/resume_review_aiagent/Resume.pdf"
resume_text = extract_text(resume_path)

# Get analysis feedback from the agent
feedback = analyze_resume(resume_text)

print("Feedback:")
print(feedback)