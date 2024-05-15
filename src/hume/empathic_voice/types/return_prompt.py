# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class ReturnPrompt(pydantic_v1.BaseModel):
    """
    A specific prompt version returned from the server
    """

    id: str = pydantic_v1.Field()
    """
    Identifier for a Prompt. Formatted as a UUID.
    """

    version: int = pydantic_v1.Field()
    """
    Version number for a Prompt. Version numbers should be integers. The combination of configId and version number is unique.
    """

    version_type: str = pydantic_v1.Field()
    """
    Inidicates whether this prompt is using a fixed version number or auto-updating to the latest version. Values from the VersionType enum.
    """

    version_description: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Description that is appended to a specific version of a Prompt.
    """

    name: str = pydantic_v1.Field()
    """
    Name applied to all versions of a particular Prompt.
    """

    created_on: int = pydantic_v1.Field()
    """
    The timestamp when the first version of this prompt was created.
    """

    modified_on: int = pydantic_v1.Field()
    """
    The timestamp when this version of the prompt was created.
    """

    text: str = pydantic_v1.Field()
    """
    Text used for this version of the Prompt.
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
