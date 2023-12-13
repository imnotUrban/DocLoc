from typing import List
from fastapi import APIRouter, HTTPException
from controllers.document import create_documents
from schemas.document import Document

document = APIRouter()

@document.post("/geolocalize")
async def geolocalize_documents(document: List[Document]):
    try:
        result = await create_documents(document)
        return result
    except HTTPException as e:
        raise e