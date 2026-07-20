# from google.adk.agents import LlmAgent

# from agents.research.agent import research_agent
# from agents.reporting.agent import report_agent

# coordinator_agent = LlmAgent(
#     name="coordinator_agent",
#     model="gemini-2.5-flash",
#     description="Routes requests",

#     instruction="""
#     Route requests:

#     Research questions → research_agent

#     Report generation →
#     report_agent
#     """,

#     sub_agents=[
#         research_agent,
#         report_agent
#     ]
# )

#---------------------------------------------------------------------------------------------------------------
#commenting the above one, as the routing agent was routing all reporting questions to Research agent 
# and not to reporting agent, so optimizing the instructions as it vague above, making more descriptive



from google.adk.agents import LlmAgent

from agents.research.agent import research_agent
from agents.reporting.agent import report_agent

##adding new

from agents.document.agent import document_agent

coordinator_agent = LlmAgent(
    name="coordinator_agent",
    model="gemini-2.5-flash",
    description="Routes requests",

   instruction="""
You are a routing specialist.

Route to document_agent when:

- user refers to uploaded documents
- user asks about PDFs
- user asks to summarize documents
- user asks document-specific questions

Route to research_agent when:
- user asks what, why, how
- user wants explanations
- user wants technical comparison
- user wants analysis

Route to report_agent when:
- user says executive summary
- user says report
- user says presentation
- user says key findings
- user says recommendations
- user says consultant-style output

Always delegate work to a specialist.
"""
,

    sub_agents=[
        document_agent,
        research_agent,
        report_agent
    ]
)

