# coding: utf-8

import pprint
import re

import six


class UserVmrDTO(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'vmr_id': 'str',
        'vmr_name': 'str',
        'vmr_pkg_id': 'str',
        'vmr_pkg_name': 'str',
        'vmr_pkg_parties': 'int',
        'vmr_pkg_length': 'int',
        'status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'vmr_id': 'vmrId',
        'vmr_name': 'vmrName',
        'vmr_pkg_id': 'vmrPkgId',
        'vmr_pkg_name': 'vmrPkgName',
        'vmr_pkg_parties': 'vmrPkgParties',
        'vmr_pkg_length': 'vmrPkgLength',
        'status': 'status'
    }

    def __init__(self, id=None, vmr_id=None, vmr_name=None, vmr_pkg_id=None, vmr_pkg_name=None, vmr_pkg_parties=None, vmr_pkg_length=None, status=None):  # noqa: E501
        """UserVmrDTO - a model defined in huaweicloud sdk"""

        self._id = None
        self._vmr_id = None
        self._vmr_name = None
        self._vmr_pkg_id = None
        self._vmr_pkg_name = None
        self._vmr_pkg_parties = None
        self._vmr_pkg_length = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vmr_id is not None:
            self.vmr_id = vmr_id
        if vmr_name is not None:
            self.vmr_name = vmr_name
        if vmr_pkg_id is not None:
            self.vmr_pkg_id = vmr_pkg_id
        if vmr_pkg_name is not None:
            self.vmr_pkg_name = vmr_pkg_name
        if vmr_pkg_parties is not None:
            self.vmr_pkg_parties = vmr_pkg_parties
        if vmr_pkg_length is not None:
            self.vmr_pkg_length = vmr_pkg_length
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this UserVmrDTO.

        云会议室的唯一标识

        :return: The id of this UserVmrDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserVmrDTO.

        云会议室的唯一标识

        :param id: The id of this UserVmrDTO.
        :type: str
        """
        self._id = id

    @property
    def vmr_id(self):
        """Gets the vmr_id of this UserVmrDTO.

        云会议室ID即预约会议的id，分为两种，一种是创建用户时生成的，为用户个人的，另一种是企业管理员分配的专用云会议室

        :return: The vmr_id of this UserVmrDTO.
        :rtype: str
        """
        return self._vmr_id

    @vmr_id.setter
    def vmr_id(self, vmr_id):
        """Sets the vmr_id of this UserVmrDTO.

        云会议室ID即预约会议的id，分为两种，一种是创建用户时生成的，为用户个人的，另一种是企业管理员分配的专用云会议室

        :param vmr_id: The vmr_id of this UserVmrDTO.
        :type: str
        """
        self._vmr_id = vmr_id

    @property
    def vmr_name(self):
        """Gets the vmr_name of this UserVmrDTO.

        云会议室名称

        :return: The vmr_name of this UserVmrDTO.
        :rtype: str
        """
        return self._vmr_name

    @vmr_name.setter
    def vmr_name(self, vmr_name):
        """Sets the vmr_name of this UserVmrDTO.

        云会议室名称

        :param vmr_name: The vmr_name of this UserVmrDTO.
        :type: str
        """
        self._vmr_name = vmr_name

    @property
    def vmr_pkg_id(self):
        """Gets the vmr_pkg_id of this UserVmrDTO.

        云会议室套餐包的id，仅专用云会议室返回

        :return: The vmr_pkg_id of this UserVmrDTO.
        :rtype: str
        """
        return self._vmr_pkg_id

    @vmr_pkg_id.setter
    def vmr_pkg_id(self, vmr_pkg_id):
        """Sets the vmr_pkg_id of this UserVmrDTO.

        云会议室套餐包的id，仅专用云会议室返回

        :param vmr_pkg_id: The vmr_pkg_id of this UserVmrDTO.
        :type: str
        """
        self._vmr_pkg_id = vmr_pkg_id

    @property
    def vmr_pkg_name(self):
        """Gets the vmr_pkg_name of this UserVmrDTO.

        云会议室套餐包的名称，仅专用云会议室返回

        :return: The vmr_pkg_name of this UserVmrDTO.
        :rtype: str
        """
        return self._vmr_pkg_name

    @vmr_pkg_name.setter
    def vmr_pkg_name(self, vmr_pkg_name):
        """Sets the vmr_pkg_name of this UserVmrDTO.

        云会议室套餐包的名称，仅专用云会议室返回

        :param vmr_pkg_name: The vmr_pkg_name of this UserVmrDTO.
        :type: str
        """
        self._vmr_pkg_name = vmr_pkg_name

    @property
    def vmr_pkg_parties(self):
        """Gets the vmr_pkg_parties of this UserVmrDTO.

        云会议室套餐包的会议并发方数，仅专用云会议室返回

        :return: The vmr_pkg_parties of this UserVmrDTO.
        :rtype: int
        """
        return self._vmr_pkg_parties

    @vmr_pkg_parties.setter
    def vmr_pkg_parties(self, vmr_pkg_parties):
        """Sets the vmr_pkg_parties of this UserVmrDTO.

        云会议室套餐包的会议并发方数，仅专用云会议室返回

        :param vmr_pkg_parties: The vmr_pkg_parties of this UserVmrDTO.
        :type: int
        """
        self._vmr_pkg_parties = vmr_pkg_parties

    @property
    def vmr_pkg_length(self):
        """Gets the vmr_pkg_length of this UserVmrDTO.

        云会议室套餐包的与会时间，若为0则代表无限时长，仅专用云会议室返回

        :return: The vmr_pkg_length of this UserVmrDTO.
        :rtype: int
        """
        return self._vmr_pkg_length

    @vmr_pkg_length.setter
    def vmr_pkg_length(self, vmr_pkg_length):
        """Sets the vmr_pkg_length of this UserVmrDTO.

        云会议室套餐包的与会时间，若为0则代表无限时长，仅专用云会议室返回

        :param vmr_pkg_length: The vmr_pkg_length of this UserVmrDTO.
        :type: int
        """
        self._vmr_pkg_length = vmr_pkg_length

    @property
    def status(self):
        """Gets the status of this UserVmrDTO.

        云会议室状态。 * 0.正常 * 1.停用 * 2.未分配 

        :return: The status of this UserVmrDTO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserVmrDTO.

        云会议室状态。 * 0.正常 * 1.停用 * 2.未分配 

        :param status: The status of this UserVmrDTO.
        :type: int
        """
        self._status = status

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
        if not isinstance(other, UserVmrDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other