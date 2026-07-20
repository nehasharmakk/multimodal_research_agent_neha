# from google.adk.agents import LlmAgent

# report_agent = LlmAgent(
#     name="report_agent",
#     model="gemini-2.5-flash",
#     description="Reporting specialist",
#     instruction="""
#     You are an executive reporting specialist.

#     Responsibilities:
#     - Create executive summaries
#     - Create reports
#     - Create consultant-style outputs
#     """
# )

#---------------------------------------------------------------------------------------------------------------
#commenting the above one, as the routing agent was routing all reporting questions to Research agent 
# and not to reporting agent, so optimizing the instructions

from google.adk.agents import LlmAgent
report_agent = LlmAgent(
    name="report_agent",
    model="gemini-2.5-flash",
    description="""
    Expert for:
    - executive summaries
    - business reports
    - consulting deliverables
    - presentations

    Do NOT perform detailed technical analysis.
    """,
    instruction="""
    You are a Management Consultant.

    Focus on:
    - executive summaries
    - structured reports
    - business communication
    - recommendations

    Format all responses professionally.
    """
)