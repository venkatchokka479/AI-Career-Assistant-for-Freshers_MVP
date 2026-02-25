from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.match import MatchRequest, MatchResponse
from app.services.matcher import ATSMatcher
from app.services.text_extraction import TextExtractionError, extract_resume_text

router = APIRouter(prefix="/match", tags=["matching"])


@router.post("/resume-text", response_model=MatchResponse)
def match_from_text(payload: MatchRequest):
    result = ATSMatcher.run_match(
        resume_text=payload.resume_text,
        job_title=payload.job_title,
        job_description=payload.job_description,
    )
    result.pop("embeddings", None)
    return result


@router.post("/resume-file", response_model=MatchResponse)
async def match_from_file(
    job_title: str,
    job_description: str,
    file: UploadFile = File(...),
):
    try:
        content = await file.read()
        resume_text = extract_resume_text(content, file.filename or "resume.pdf")
    except TextExtractionError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    result = ATSMatcher.run_match(
        resume_text=resume_text,
        job_title=job_title,
        job_description=job_description,
    )
    result.pop("embeddings", None)
    return result
