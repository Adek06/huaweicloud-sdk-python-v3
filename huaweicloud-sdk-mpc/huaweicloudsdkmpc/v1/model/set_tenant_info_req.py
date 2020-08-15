# coding: utf-8

import pprint
import re

import six





class SetTenantInfoReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_open': 'int'
    }

    attribute_map = {
        'is_open': 'is_open'
    }

    def __init__(self, is_open=None):
        """SetTenantInfoReq - a model defined in huaweicloud sdk"""
        
        

        self._is_open = None
        self.discriminator = None

        if is_open is not None:
            self.is_open = is_open

    @property
    def is_open(self):
        """Gets the is_open of this SetTenantInfoReq.

        是否已开通服务，0标示否，1标示已开通 

        :return: The is_open of this SetTenantInfoReq.
        :rtype: int
        """
        return self._is_open

    @is_open.setter
    def is_open(self, is_open):
        """Sets the is_open of this SetTenantInfoReq.

        是否已开通服务，0标示否，1标示已开通 

        :param is_open: The is_open of this SetTenantInfoReq.
        :type: int
        """
        self._is_open = is_open

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
        if not isinstance(other, SetTenantInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other