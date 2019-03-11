# coding: utf-8

"""
    Eclipse Kapua REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class KapuaDataChannel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'semantic_parts': 'list[str]'
    }

    attribute_map = {
        'semantic_parts': 'semanticParts'
    }

    def __init__(self, semantic_parts=None):  # noqa: E501
        """KapuaDataChannel - a model defined in Swagger"""  # noqa: E501

        self._semantic_parts = None
        self.discriminator = None

        if semantic_parts is not None:
            self.semantic_parts = semantic_parts

    @property
    def semantic_parts(self):
        """Gets the semantic_parts of this KapuaDataChannel.  # noqa: E501


        :return: The semantic_parts of this KapuaDataChannel.  # noqa: E501
        :rtype: list[str]
        """
        return self._semantic_parts

    @semantic_parts.setter
    def semantic_parts(self, semantic_parts):
        """Sets the semantic_parts of this KapuaDataChannel.


        :param semantic_parts: The semantic_parts of this KapuaDataChannel.  # noqa: E501
        :type: list[str]
        """

        self._semantic_parts = semantic_parts

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(KapuaDataChannel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KapuaDataChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
