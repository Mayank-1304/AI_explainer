from fastapi import APIRouter, HTTPException
from models.request import TopicRequest
from chains.explainer import chain

router = APIRouter()

@router.post("/explain")
async def explain_topic(request: TopicRequest):
    try:
        if not request.topic:
            raise HTTPException(status_code=400, detail="Topic cannot be empty")
        
        result = chain.invoke({"topic": request.topic})
        return {"explanation": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
