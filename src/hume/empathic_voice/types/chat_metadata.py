# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class ChatMetadata(pydantic_v1.BaseModel):
    """
    When provided, the output is a chat metadata message.
    """

    chat_group_id: str = pydantic_v1.Field()
    """
    ID of the chat group. Used to resume a chat.
    """

    chat_id: str = pydantic_v1.Field()
    """
    ID of the chat.
    """

    custom_session_id: typing.Optional[str] = None
    type: typing.Literal["chat_metadata"] = pydantic_v1.Field(default="chat_metadata")
    """
    The type of message sent through the socket; for a Chat Metadata message, this must be 'chat_metadata'.
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