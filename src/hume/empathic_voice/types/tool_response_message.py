# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .tool_type import ToolType


class ToolResponseMessage(pydantic_v1.BaseModel):
    """
    When provided, the output is a function call response.
    """

    content: str = pydantic_v1.Field()
    """
    Return value of the tool call.
    """

    custom_session_id: typing.Optional[str] = None
    tool_call_id: str = pydantic_v1.Field()
    """
    ID of the tool call.
    """

    tool_name: typing.Optional[str] = None
    tool_type: typing.Optional[ToolType] = None
    type: typing.Optional[typing.Literal["tool_response"]] = pydantic_v1.Field(default=None)
    """
    The type of message sent through the socket; for a Tool Response message, this must be ‘tool_response’.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
