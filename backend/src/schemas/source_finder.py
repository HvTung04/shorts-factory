from pydantic import BaseModel
from typing import Optional, List, Union, Dict, Any, Literal
from enum import Enum
from datetime import datetime

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
    url: str
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