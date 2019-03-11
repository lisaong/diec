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


class SortField(object):
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
        'sort_direction': 'str',
        'field': 'str'
    }

    attribute_map = {
        'sort_direction': 'sortDirection',
        'field': 'field'
    }

    def __init__(self, sort_direction=None, field=None):  # noqa: E501
        """SortField - a model defined in Swagger"""  # noqa: E501

        self._sort_direction = None
        self._field = None
        self.discriminator = None

        if sort_direction is not None:
            self.sort_direction = sort_direction
        if field is not None:
            self.field = field

    @property
    def sort_direction(self):
        """Gets the sort_direction of this SortField.  # noqa: E501


        :return: The sort_direction of this SortField.  # noqa: E501
        :rtype: str
        """
        return self._sort_direction

    @sort_direction.setter
    def sort_direction(self, sort_direction):
        """Sets the sort_direction of this SortField.


        :param sort_direction: The sort_direction of this SortField.  # noqa: E501
        :type: str
        """
        allowed_values = ["ASC", "DESC"]  # noqa: E501
        if sort_direction not in allowed_values:
            raise ValueError(
                "Invalid value for `sort_direction` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_direction, allowed_values)
            )

        self._sort_direction = sort_direction

    @property
    def field(self):
        """Gets the field of this SortField.  # noqa: E501


        :return: The field of this SortField.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this SortField.


        :param field: The field of this SortField.  # noqa: E501
        :type: str
        """

        self._field = field

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
        if issubclass(SortField, dict):
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
        if not isinstance(other, SortField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
