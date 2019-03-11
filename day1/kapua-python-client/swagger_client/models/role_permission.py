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

from swagger_client.models.permission import Permission  # noqa: F401,E501


class RolePermission(object):
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
        'role_id': 'str',
        'type': 'str',
        'permission': 'Permission',
        'scope_id': 'str',
        'id': 'str',
        'created_on': 'datetime',
        'created_by': 'str'
    }

    attribute_map = {
        'role_id': 'roleId',
        'type': 'type',
        'permission': 'permission',
        'scope_id': 'scopeId',
        'id': 'id',
        'created_on': 'createdOn',
        'created_by': 'createdBy'
    }

    def __init__(self, role_id=None, type=None, permission=None, scope_id=None, id=None, created_on=None, created_by=None):  # noqa: E501
        """RolePermission - a model defined in Swagger"""  # noqa: E501

        self._role_id = None
        self._type = None
        self._permission = None
        self._scope_id = None
        self._id = None
        self._created_on = None
        self._created_by = None
        self.discriminator = None

        if role_id is not None:
            self.role_id = role_id
        if type is not None:
            self.type = type
        if permission is not None:
            self.permission = permission
        if scope_id is not None:
            self.scope_id = scope_id
        if id is not None:
            self.id = id
        if created_on is not None:
            self.created_on = created_on
        if created_by is not None:
            self.created_by = created_by

    @property
    def role_id(self):
        """Gets the role_id of this RolePermission.  # noqa: E501


        :return: The role_id of this RolePermission.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this RolePermission.


        :param role_id: The role_id of this RolePermission.  # noqa: E501
        :type: str
        """

        self._role_id = role_id

    @property
    def type(self):
        """Gets the type of this RolePermission.  # noqa: E501


        :return: The type of this RolePermission.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RolePermission.


        :param type: The type of this RolePermission.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def permission(self):
        """Gets the permission of this RolePermission.  # noqa: E501


        :return: The permission of this RolePermission.  # noqa: E501
        :rtype: Permission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this RolePermission.


        :param permission: The permission of this RolePermission.  # noqa: E501
        :type: Permission
        """

        self._permission = permission

    @property
    def scope_id(self):
        """Gets the scope_id of this RolePermission.  # noqa: E501


        :return: The scope_id of this RolePermission.  # noqa: E501
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this RolePermission.


        :param scope_id: The scope_id of this RolePermission.  # noqa: E501
        :type: str
        """

        self._scope_id = scope_id

    @property
    def id(self):
        """Gets the id of this RolePermission.  # noqa: E501


        :return: The id of this RolePermission.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RolePermission.


        :param id: The id of this RolePermission.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_on(self):
        """Gets the created_on of this RolePermission.  # noqa: E501


        :return: The created_on of this RolePermission.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this RolePermission.


        :param created_on: The created_on of this RolePermission.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def created_by(self):
        """Gets the created_by of this RolePermission.  # noqa: E501


        :return: The created_by of this RolePermission.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this RolePermission.


        :param created_by: The created_by of this RolePermission.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

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
        if issubclass(RolePermission, dict):
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
        if not isinstance(other, RolePermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
