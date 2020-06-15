# coding: utf-8

import pprint
import re

import six


class CelebrityRecognitionReq(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'image': 'str',
        'url': 'str',
        'threshold': 'float'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'threshold': 'threshold'
    }

    def __init__(self, image=None, url=None, threshold=None):  # noqa: E501
        """CelebrityRecognitionReq - a model defined in huaweicloud sdk"""

        self._image = None
        self._url = None
        self._threshold = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if threshold is not None:
            self.threshold = threshold

    @property
    def image(self):
        """Gets the image of this CelebrityRecognitionReq.

        与url二选一  图片文件Base64编码字符串。要求base64编码后大小不超过10M。  政治人物检测人脸部分不小于40*40像素。  支持JPG/PNG/BMP格式。 

        :return: The image of this CelebrityRecognitionReq.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this CelebrityRecognitionReq.

        与url二选一  图片文件Base64编码字符串。要求base64编码后大小不超过10M。  政治人物检测人脸部分不小于40*40像素。  支持JPG/PNG/BMP格式。 

        :param image: The image of this CelebrityRecognitionReq.
        :type: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this CelebrityRecognitionReq.

        与image二选一  图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[配置OBS服务的访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)。  > 说明：  - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。  - 请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 

        :return: The url of this CelebrityRecognitionReq.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CelebrityRecognitionReq.

        与image二选一  图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[配置OBS服务的访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)。  > 说明：  - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。  - 请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 

        :param url: The url of this CelebrityRecognitionReq.
        :type: str
        """
        self._url = url

    @property
    def threshold(self):
        """Gets the threshold of this CelebrityRecognitionReq.

        置信度的阈值（0~1），低于此置信数的标签，将不会返回。  默认值：0.48。 

        :return: The threshold of this CelebrityRecognitionReq.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this CelebrityRecognitionReq.

        置信度的阈值（0~1），低于此置信数的标签，将不会返回。  默认值：0.48。 

        :param threshold: The threshold of this CelebrityRecognitionReq.
        :type: float
        """
        self._threshold = threshold

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
        if not isinstance(other, CelebrityRecognitionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
