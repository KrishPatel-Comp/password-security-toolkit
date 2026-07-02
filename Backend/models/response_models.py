from pydantic import BaseModel


class PasswordAnalysisResponse(BaseModel):
    score: int
    strength: str
    entropy: float
    crack_time: str

    length: int

    has_uppercase: bool
    has_lowercase: bool
    has_number: bool
    has_special: bool

    has_repeated_characters: bool
    has_sequential_pattern: bool
    has_keyboard_pattern: bool
    is_common_password: bool

    suggestions: list[str]