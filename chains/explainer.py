from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

prompt_template = ChatPromptTemplate.from_template(
"""Explain {topic} in an elegant and structured manner for a learning dashboard.
Use the following exact layout structure with Bullet points:

CONCEPT:
[1-2 sentences explaining it simply and clearly]

ANALOGY:
[A relatable real-world comparison]

3 KEY TAKEAWAYS:
• [Takeaway Point 1]
• [Takeaway Point 2]
• [Takeaway Point 3]"""
)

chain = prompt_template | model | StrOutputParser()
