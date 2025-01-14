

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request model
class QueryRequest(BaseModel):
    platform: str
    question: str

@app.post("/query")
def get_answer(request: QueryRequest):
    # Simulate a response based on the platform
    platform_responses = {
        "segment": "To set up a new source in Segment, go to the Sources page, click Add Source, and follow the steps.",
        "mparticle": "To create a user profile in mParticle, use the Profiles API or the mParticle dashboard.",
        "lytics": "To build an audience in Lytics, go to the Audiences section and define your segmentation criteria.",
        "zeotap": "To integrate data with Zeotap, configure data pipelines in the Zeotap dashboard."
    }
    # Return the corresponding response or a default message
    answer = platform_responses.get(request.platform.lower(), "No specific information available for this platform.")
    return {"answer": answer}
