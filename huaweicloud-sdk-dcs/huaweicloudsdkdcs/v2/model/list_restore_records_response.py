# coding: utf-8

import pprint
import re

import six


class ListRestoreRecordsResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'restore_record_response': 'list[InstanceRestoreInfo]',
        'total_num': 'int'
    }

    attribute_map = {
        'restore_record_response': 'restore_record_response',
        'total_num': 'total_num'
    }

    def __init__(self, restore_record_response=None, total_num=None):  # noqa: E501
        """ListRestoreRecordsResponse - a model defined in huaweicloud sdk"""

        self._restore_record_response = None
        self._total_num = None
        self.discriminator = None

        if restore_record_response is not None:
            self.restore_record_response = restore_record_response
        if total_num is not None:
            self.total_num = total_num

    @property
    def restore_record_response(self):
        """Gets the restore_record_response of this ListRestoreRecordsResponse.

        实例恢复记录的详情数组。

        :return: The restore_record_response of this ListRestoreRecordsResponse.
        :rtype: list[InstanceRestoreInfo]
        """
        return self._restore_record_response

    @restore_record_response.setter
    def restore_record_response(self, restore_record_response):
        """Sets the restore_record_response of this ListRestoreRecordsResponse.

        实例恢复记录的详情数组。

        :param restore_record_response: The restore_record_response of this ListRestoreRecordsResponse.
        :type: list[InstanceRestoreInfo]
        """
        self._restore_record_response = restore_record_response

    @property
    def total_num(self):
        """Gets the total_num of this ListRestoreRecordsResponse.

        返回记录数。

        :return: The total_num of this ListRestoreRecordsResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this ListRestoreRecordsResponse.

        返回记录数。

        :param total_num: The total_num of this ListRestoreRecordsResponse.
        :type: int
        """
        self._total_num = total_num

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
        if not isinstance(other, ListRestoreRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
