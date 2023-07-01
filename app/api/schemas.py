from pydantic import BaseModel

class PredictSchema(BaseModel):
    text: str