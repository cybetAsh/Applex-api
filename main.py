import openai
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Apple - X Ai Global Engine")

# වෙබ් අඩවිය සහ API එක අතර සම්බන්ධතාවය තහවුරු කිරීමට (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ඔබ ලබා දුන් API Key එක මෙහි ඇතුළත් කර ඇත
client = openai.OpenAI(api_key="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")

class CodeRequest(BaseModel):
    prompt: str
    tech_stack: str

@app.post("/generate")
async def apple_x_engine(request: CodeRequest):
    try:
        # ChatGPT වෙතින් පිළිතුරක් ලබා ගැනීම
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": "You are Apple - X Ai. Provide a professional website source code with folder structure in JSON format. Return ONLY the JSON object."
                },
                {
                    "role": "user", 
                    "content": f"Create a full website for: {request.prompt}. Use tech: {request.tech_stack}"
                }
            ],
            response_format={ "type": "json_object" }
        )
        return {
            "status": "success",
            "bot": "Apple - X Ai",
            "host": "applexai.zone.id",
            "data": response.choices[0].message.content
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # සර්වර් එක පණගැන්වීම
    uvicorn.run(app, host="0.0.0.0", port=8000)
