# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .return_config_spec import ReturnConfigSpec


class ReturnChat(pydantic_v1.BaseModel):
    """
    A description of chat and its status
    """

    id: str = pydantic_v1.Field()
    """
    Identifier for a chat. Formatted as a UUID.
    """

    tag: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Optional tag applied to this chat used to group chats by user, application, etc.
    """

    status: str = pydantic_v1.Field()
    """
    The status of the chat. Values from the ChatStatus enum.
    """

    start_timestamp: int = pydantic_v1.Field()
    """
    The timestamp when the chat started, formatted as a Unix epoch milliseconds.
    """

    end_timestamp: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    The timestamp when the chat ended, formatted as a Unix epoch milliseconds.
    """

    event_count: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    The total number of events currently in this chat.
    """

    metadata: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Stringified JSON with additional metadata about the chat.
    """

    config: typing.Optional[ReturnConfigSpec] = None

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
