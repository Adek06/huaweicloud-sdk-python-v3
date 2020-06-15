# coding: utf-8

import pprint
import re

import six


class ListScalingTagInfosByTenantIdResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'tags': 'list[TagsMultiValue]'
    }

    attribute_map = {
        'tags': 'tags'
    }

    def __init__(self, tags=None):  # noqa: E501
        """ListScalingTagInfosByTenantIdResponse - a model defined in huaweicloud sdk"""

        self._tags = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags

    @property
    def tags(self):
        """Gets the tags of this ListScalingTagInfosByTenantIdResponse.

        资源标签。

        :return: The tags of this ListScalingTagInfosByTenantIdResponse.
        :rtype: list[TagsMultiValue]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListScalingTagInfosByTenantIdResponse.

        资源标签。

        :param tags: The tags of this ListScalingTagInfosByTenantIdResponse.
        :type: list[TagsMultiValue]
        """
        self._tags = tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListScalingTagInfosByTenantIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
