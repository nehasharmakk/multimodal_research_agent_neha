# from google.adk.agents import LlmAgent

# root_agent = LlmAgent(
#     name="research_assistant",
#     model="gemini-2.5-flash",
#     description="A helpful research assistant",
#     instruction="""
#     You are a professional research assistant.

#     Help users:
#     - Answer questions
#     - Summarize information
#     - Explain concepts clearly
#     - Provide structured responses
#     """
# )

#updated the above one was to only cross check


from agents.coordinator.agent import coordinator_agent

root_agent = coordinator_agent