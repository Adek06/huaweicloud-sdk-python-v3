# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListDomainTrafficSummaryV2Response(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'traffic_list': 'list[TrafficSummaryData]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'traffic_list': 'traffic_list',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, traffic_list=None, x_request_id=None):
        """ListDomainTrafficSummaryV2Response - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._traffic_list = None
        self._x_request_id = None
        self.discriminator = None

        if traffic_list is not None:
            self.traffic_list = traffic_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def traffic_list(self):
        """Gets the traffic_list of this ListDomainTrafficSummaryV2Response.

        域名对应的流量汇总列表。

        :return: The traffic_list of this ListDomainTrafficSummaryV2Response.
        :rtype: list[TrafficSummaryData]
        """
        return self._traffic_list

    @traffic_list.setter
    def traffic_list(self, traffic_list):
        """Sets the traffic_list of this ListDomainTrafficSummaryV2Response.

        域名对应的流量汇总列表。

        :param traffic_list: The traffic_list of this ListDomainTrafficSummaryV2Response.
        :type: list[TrafficSummaryData]
        """
        self._traffic_list = traffic_list

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListDomainTrafficSummaryV2Response.


        :return: The x_request_id of this ListDomainTrafficSummaryV2Response.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListDomainTrafficSummaryV2Response.


        :param x_request_id: The x_request_id of this ListDomainTrafficSummaryV2Response.
        :type: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListDomainTrafficSummaryV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other