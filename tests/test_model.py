from typing import Optional, Callable, Generator, Sequence
from pydantic import BaseModel, Field

class TestDataModel(BaseModel):
    class_: Optional[object] = Field(default=Optional[object])
    function: Optional[Callable[[], None]] = Field(default=Optional[Callable[[], None]])
    limit: Optional[int] = Field(default=Optional[int])
    args: Optional[tuple] = Field(default=Optional[tuple])
    kwargs: Optional[dict] = Field(default=Optional[dict])
    url: Optional[str] = Field(default=Optional[str])
    limit: Optional[int] = Field(default=Optional[int])
    
    def __init__(self, **data):
        super().__init__(**data)
        self.url = data.get("url")
        self.limit = data.get("limit")

    def __call__(self, limit: Optional[int] = None, ) -> Generator[Optional[Sequence], None, None]:
        if isinstance(self.function, Callable):
            args = (self.class_, limit)
            kwargs = {}
            return self.function(*args, **kwargs)
        else:
            raise ValueError("Function is not callable")

    def __repr__(self):
        return f"TestModel(class_={self.class_},\n function={self.function},\n limit={self.limit})"

