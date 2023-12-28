# coding: utf-8

"""
    LINE Messaging API(Insight)

    This document describes LINE Messaging API(Insight).  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic.v1 import BaseModel, Field, StrictInt

class GetStatisticsPerUnitResponseMessage(BaseModel):
    """
    GetStatisticsPerUnitResponseMessage
    https://developers.line.biz/en/reference/messaging-api/#get-statistics-per-unit-response
    """
    seq: StrictInt = Field(..., description="Bubble's serial number.")
    impression: Optional[StrictInt] = Field(None, description="Number of times the bubble was displayed.")
    media_played: Optional[StrictInt] = Field(None, alias="mediaPlayed", description="Number of times audio or video in the bubble started playing.")
    media_played25_percent: Optional[StrictInt] = Field(None, alias="mediaPlayed25Percent", description="Number of times audio or video in the bubble started playing and was played 25% of the total time.")
    media_played50_percent: Optional[StrictInt] = Field(None, alias="mediaPlayed50Percent", description="Number of times audio or video in the bubble started playing and was played 50% of the total time.")
    media_played75_percent: Optional[StrictInt] = Field(None, alias="mediaPlayed75Percent", description="Number of times audio or video in the bubble started playing and was played 75% of the total time.")
    media_played100_percent: Optional[StrictInt] = Field(None, alias="mediaPlayed100Percent", description="Number of times audio or video in the bubble started playing and was played 100% of the total time.")
    unique_impression: Optional[StrictInt] = Field(None, alias="uniqueImpression", description="Number of users the bubble was displayed.")
    unique_media_played: Optional[StrictInt] = Field(None, alias="uniqueMediaPlayed", description="Number of users that started playing audio or video in the bubble.")
    unique_media_played25_percent: Optional[StrictInt] = Field(None, alias="uniqueMediaPlayed25Percent", description="Number of users that started playing audio or video in the bubble and played 25% of the total time.")
    unique_media_played50_percent: Optional[StrictInt] = Field(None, alias="uniqueMediaPlayed50Percent", description="Number of users that started playing audio or video in the bubble and played 50% of the total time.")
    unique_media_played75_percent: Optional[StrictInt] = Field(None, alias="uniqueMediaPlayed75Percent", description="Number of users that started playing audio or video in the bubble and played 75% of the total time.")
    unique_media_played100_percent: Optional[StrictInt] = Field(None, alias="uniqueMediaPlayed100Percent", description="Number of users that started playing audio or video in the bubble and played 100% of the total time.")

    __properties = ["seq", "impression", "mediaPlayed", "mediaPlayed25Percent", "mediaPlayed50Percent", "mediaPlayed75Percent", "mediaPlayed100Percent", "uniqueImpression", "uniqueMediaPlayed", "uniqueMediaPlayed25Percent", "uniqueMediaPlayed50Percent", "uniqueMediaPlayed75Percent", "uniqueMediaPlayed100Percent"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GetStatisticsPerUnitResponseMessage:
        """Create an instance of GetStatisticsPerUnitResponseMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if impression (nullable) is None
        # and __fields_set__ contains the field
        if self.impression is None and "impression" in self.__fields_set__:
            _dict['impression'] = None

        # set to None if media_played (nullable) is None
        # and __fields_set__ contains the field
        if self.media_played is None and "media_played" in self.__fields_set__:
            _dict['mediaPlayed'] = None

        # set to None if media_played25_percent (nullable) is None
        # and __fields_set__ contains the field
        if self.media_played25_percent is None and "media_played25_percent" in self.__fields_set__:
            _dict['mediaPlayed25Percent'] = None

        # set to None if media_played50_percent (nullable) is None
        # and __fields_set__ contains the field
        if self.media_played50_percent is None and "media_played50_percent" in self.__fields_set__:
            _dict['mediaPlayed50Percent'] = None

        # set to None if media_played75_percent (nullable) is None
        # and __fields_set__ contains the field
        if self.media_played75_percent is None and "media_played75_percent" in self.__fields_set__:
            _dict['mediaPlayed75Percent'] = None

        # set to None if media_played100_percent (nullable) is None
        # and __fields_set__ contains the field
        if self.media_played100_percent is None and "media_played100_percent" in self.__fields_set__:
            _dict['mediaPlayed100Percent'] = None

        # set to None if unique_impression (nullable) is None
        # and __fields_set__ contains the field
        if self.unique_impression is None and "unique_impression" in self.__fields_set__:
            _dict['uniqueImpression'] = None

        # set to None if unique_media_played (nullable) is None
        # and __fields_set__ contains the field
        if self.unique_media_played is None and "unique_media_played" in self.__fields_set__:
            _dict['uniqueMediaPlayed'] = None

        # set to None if unique_media_played25_percent (nullable) is None
        # and __fields_set__ contains the field
        if self.unique_media_played25_percent is None and "unique_media_played25_percent" in self.__fields_set__:
            _dict['uniqueMediaPlayed25Percent'] = None

        # set to None if unique_media_played50_percent (nullable) is None
        # and __fields_set__ contains the field
        if self.unique_media_played50_percent is None and "unique_media_played50_percent" in self.__fields_set__:
            _dict['uniqueMediaPlayed50Percent'] = None

        # set to None if unique_media_played75_percent (nullable) is None
        # and __fields_set__ contains the field
        if self.unique_media_played75_percent is None and "unique_media_played75_percent" in self.__fields_set__:
            _dict['uniqueMediaPlayed75Percent'] = None

        # set to None if unique_media_played100_percent (nullable) is None
        # and __fields_set__ contains the field
        if self.unique_media_played100_percent is None and "unique_media_played100_percent" in self.__fields_set__:
            _dict['uniqueMediaPlayed100Percent'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetStatisticsPerUnitResponseMessage:
        """Create an instance of GetStatisticsPerUnitResponseMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetStatisticsPerUnitResponseMessage.parse_obj(obj)

        _obj = GetStatisticsPerUnitResponseMessage.parse_obj({
            "seq": obj.get("seq"),
            "impression": obj.get("impression"),
            "media_played": obj.get("mediaPlayed"),
            "media_played25_percent": obj.get("mediaPlayed25Percent"),
            "media_played50_percent": obj.get("mediaPlayed50Percent"),
            "media_played75_percent": obj.get("mediaPlayed75Percent"),
            "media_played100_percent": obj.get("mediaPlayed100Percent"),
            "unique_impression": obj.get("uniqueImpression"),
            "unique_media_played": obj.get("uniqueMediaPlayed"),
            "unique_media_played25_percent": obj.get("uniqueMediaPlayed25Percent"),
            "unique_media_played50_percent": obj.get("uniqueMediaPlayed50Percent"),
            "unique_media_played75_percent": obj.get("uniqueMediaPlayed75Percent"),
            "unique_media_played100_percent": obj.get("uniqueMediaPlayed100Percent")
        })
        return _obj

