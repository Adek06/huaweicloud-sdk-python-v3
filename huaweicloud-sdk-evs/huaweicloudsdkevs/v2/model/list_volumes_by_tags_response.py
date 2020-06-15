# coding: utf-8

import pprint
import re

import six


class ListVolumesByTagsResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total_count': 'str',
        'resources': 'list[Resource]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'resources': 'resources'
    }

    def __init__(self, total_count=None, resources=None):  # noqa: E501
        """ListVolumesByTagsResponse - a model defined in huaweicloud sdk"""

        self._total_count = None
        self._resources = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if resources is not None:
            self.resources = resources

    @property
    def total_count(self):
        """Gets the total_count of this ListVolumesByTagsResponse.

        符合查询条件的云硬盘资源个数

        :return: The total_count of this ListVolumesByTagsResponse.
        :rtype: str
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListVolumesByTagsResponse.

        符合查询条件的云硬盘资源个数

        :param total_count: The total_count of this ListVolumesByTagsResponse.
        :type: str
        """
        self._total_count = total_count

    @property
    def resources(self):
        """Gets the resources of this ListVolumesByTagsResponse.

        符合查询条件的资源列表

        :return: The resources of this ListVolumesByTagsResponse.
        :rtype: list[Resource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ListVolumesByTagsResponse.

        符合查询条件的资源列表

        :param resources: The resources of this ListVolumesByTagsResponse.
        :type: list[Resource]
        """
        self._resources = resources

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
        if not isinstance(other, ListVolumesByTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
