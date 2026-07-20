from google.adk.agents import LlmAgent

document_agent = LlmAgent(
    name="document_agent",
    model="gemini-2.5-flash",
    description="""
    Expert for processing documents,
    PDFs and extracted text.
    """,
    instruction="""
    You are a document analysis specialist.

    Responsibilities:
    - analyze PDF content
    - summarize documents
    - locate information
    - answer questions about documents
    """
)