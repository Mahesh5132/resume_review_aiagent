from langchain.llms import LlamaCpp  # Or use OpenAI if you prefer
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# Initialize LLM (replace with your model's path)
llm = LlamaCpp(model_path= "/workspaces/resume_review_aiagent/models/models/deepseek-llm-7b-chat.Q4_K_M.gguf", n_ctx=2048)  # Replace with actual model path

# Define the feedback prompt template
feedback_prompt = PromptTemplate(
    input_variables=["resume_text"],
    template="""
        You are a resume analyzer. Given the following resume text, provide feedback in bullet points on:
        - Strengths
        - Weaknesses
        - Areas for improvement
        - Missing information or skills
        - Overall clarity
        
        Resume Text:
        {resume_text}
    """
)

# Create a chain with LLM and the template
chain = LLMChain(prompt=feedback_prompt, llm=llm)

def analyze_resume(resume_text: str) -> str:
    return chain.run(resume_text=resume_text)
