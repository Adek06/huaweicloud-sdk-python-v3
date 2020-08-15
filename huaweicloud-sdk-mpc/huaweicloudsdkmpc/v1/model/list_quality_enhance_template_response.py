# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListQualityEnhanceTemplateResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_array': 'list[QualityEnhanceTemplateInfo]',
        'total': 'int'
    }

    attribute_map = {
        'task_array': 'task_array',
        'total': 'total'
    }

    def __init__(self, task_array=None, total=None):
        """ListQualityEnhanceTemplateResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._task_array = None
        self._total = None
        self.discriminator = None

        if task_array is not None:
            self.task_array = task_array
        if total is not None:
            self.total = total

    @property
    def task_array(self):
        """Gets the task_array of this ListQualityEnhanceTemplateResponse.

        任务列表

        :return: The task_array of this ListQualityEnhanceTemplateResponse.
        :rtype: list[QualityEnhanceTemplateInfo]
        """
        return self._task_array

    @task_array.setter
    def task_array(self, task_array):
        """Sets the task_array of this ListQualityEnhanceTemplateResponse.

        任务列表

        :param task_array: The task_array of this ListQualityEnhanceTemplateResponse.
        :type: list[QualityEnhanceTemplateInfo]
        """
        self._task_array = task_array

    @property
    def total(self):
        """Gets the total of this ListQualityEnhanceTemplateResponse.

        查询结果数量

        :return: The total of this ListQualityEnhanceTemplateResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListQualityEnhanceTemplateResponse.

        查询结果数量

        :param total: The total of this ListQualityEnhanceTemplateResponse.
        :type: int
        """
        self._total = total

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
        if not isinstance(other, ListQualityEnhanceTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other