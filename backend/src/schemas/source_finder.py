from pydantic import BaseModel, BeforeValidator
from typing import Optional, List, Union, Dict, Any, Literal, Annotated
from enum import Enum
from datetime import datetime
import re

# -------------------------
# Validators
# -------------------------
YOUTUBE_ID_REGEX = re.compile(r"A-Za-z0-9_-]{10}[AEIMQUYcgkosw048]")
YOUTUBE_PATTERNS = [
    r"https?://(www\.)?youtube\.com/watch\?v=([^&]+)",
    r"https?://youtu\.be/([^?&]+)",
    r"https?://(www\.)?youtube\.com/embed/([^?&]+)",
    r"https?://(www\.)?youtube\.com/shorts/([^?&]+)"
]

def validate_and_normalize_url(value: str) -> str:
    for pattern in YOUTUBE_PATTERNS:
        match = re.match(pattern, value)
        if match:
            video_id = match.group(2) if len(match.groups()) > 1 else match.group(1)
            if re.match(YOUTUBE_ID_REGEX, video_id):
                return f"https://www.youtube.com/watch?v={video_id}"
    raise ValueError(f"Invalid YouTube URL: {value}")

# -------------------------
# Enums
# -------------------------
class Source(str, Enum):
    YOUTUBE = "youtube"
    TIKTOK = "tiktok"

class InputMode(str, Enum):
    QUERY = "query"
    URLS = "urls"

# -------------------------
# Video
# -------------------------
class VideoResult(BaseModel):
    """
    Represents a video result from a source finder.
    """
    id: str
    url: Annotated[str, BeforeValidator(validate_and_normalize_url)]
    source: Source
    title: str
    duration_sec: int
    resolution: Optional[str] = None
    language: Optional[str] = None
    fetched_at: Optional[datetime] = datetime.now()

# -------------------------
# SourceFinder Input
# -------------------------
class QueryModelInput(BaseModel):
    query: str
    sources: List[Source]

class URLListInput(BaseModel):
    urls: List[str]

SourceFinderInput = Union[QueryModelInput, URLListInput]

# -------------------------
# SourceFinder Output
# -------------------------
class SourceFinderOutput(BaseModel):
    videos: list[VideoResult]
    total_duration_sec: int
    sources_used: List[Source]
    warnings: Optional[List[str]] = None

# -------------------------
# SourceCapability
# -------------------------
class SourceCapability(BaseModel):
    supported_input_modes: List[InputMode]
    constraints: Dict[str, Any] = {}

# -------------------------
# SourceFinderError
# -------------------------
class SourceFinderError(BaseModel):
    message: str
    source: Optional[Source] = None

class SkippableError(SourceFinderError):
    kind: Literal["skippable"] = "skippable"

class FatalError(SourceFinderError):
    kind: Literal["fatal"] = "fatal"