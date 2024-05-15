# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .bounding_box import BoundingBox
from .descriptions_score import DescriptionsScore
from .emotion_score import EmotionScore
from .facs_score import FacsScore


class FacePrediction(pydantic_v1.BaseModel):
    frame: int = pydantic_v1.Field()
    """
    Frame number
    """

    time: float = pydantic_v1.Field()
    """
    Time in seconds when face detection occurred.
    """

    prob: float = pydantic_v1.Field()
    """
    The predicted probability that a detected face was actually a face.
    """

    box: BoundingBox
    emotions: typing.List[EmotionScore] = pydantic_v1.Field()
    """
    A high-dimensional embedding in emotion space.
    """

    facs: typing.Optional[typing.List[FacsScore]] = pydantic_v1.Field(default=None)
    """
    FACS 2.0 features and their scores.
    """

    descriptions: typing.Optional[typing.List[DescriptionsScore]] = pydantic_v1.Field(default=None)
    """
    Modality-specific descriptive features and their scores.
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