# from google.adk.agents import LlmAgent

# research_agent = LlmAgent(
#     name="research_agent",
#     model="gemini-2.5-flash",
#     description="Research specialist",
#     instruction="""
#     You are a senior research analyst.

#     Responsibilities:
#     - Explain concepts
#     - Analyze information
#     - Compare technologies
#     - Answer technical questions
#     """
# )
#---------------------------------------------------------------------------------------------------------------
#commenting the above one, as the routing agent was routing all reporting questions to Research agent 
# and not to reporting agent, so optimizing the instructions

from google.adk.agents import LlmAgent
research_agent = LlmAgent(
    name="research_agent",
    model="gemini-2.5-flash",
    description="""
    Expert for:
    - technical explanations
    - concept clarification
    - technology analysis
    - comparisons

    Do NOT create executive summaries or reports.
    """,
    instruction="""
    You are a Senior Technical Research Analyst.

    Focus on:
    - technical explanations
    - deep analysis
    - comparisons
    - reasoning

    Never generate executive summaries.
    Never generate business reports.
    """
)