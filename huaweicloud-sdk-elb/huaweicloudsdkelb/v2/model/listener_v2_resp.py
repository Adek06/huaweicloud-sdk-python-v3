# coding: utf-8

import pprint
import re

import six





class ListenerV2Resp:


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
        'tenant_id': 'str',
        'name': 'str',
        'description': 'str',
        'admin_state_up': 'bool',
        'loadbalancers': 'list[ResourceList]',
        'connection_limit': 'int',
        'http2_enable': 'bool',
        'protocol': 'str',
        'protocol_port': 'int',
        'default_pool_id': 'str',
        'default_tls_container_ref': 'str',
        'client_ca_tls_container_ref': 'str',
        'sni_container_refs': 'list[str]',
        'tags': 'list[str]',
        'created_at': 'str',
        'updated_at': 'str',
        'insert_headers': 'InsertHeader',
        'project_id': 'str',
        'tls_ciphers_policy': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
        'loadbalancers': 'loadbalancers',
        'connection_limit': 'connection_limit',
        'http2_enable': 'http2_enable',
        'protocol': 'protocol',
        'protocol_port': 'protocol_port',
        'default_pool_id': 'default_pool_id',
        'default_tls_container_ref': 'default_tls_container_ref',
        'client_ca_tls_container_ref': 'client_ca_tls_container_ref',
        'sni_container_refs': 'sni_container_refs',
        'tags': 'tags',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'insert_headers': 'insert_headers',
        'project_id': 'project_id',
        'tls_ciphers_policy': 'tls_ciphers_policy'
    }

    def __init__(self, id=None, tenant_id=None, name=None, description=None, admin_state_up=None, loadbalancers=None, connection_limit=None, http2_enable=None, protocol=None, protocol_port=None, default_pool_id=None, default_tls_container_ref=None, client_ca_tls_container_ref=None, sni_container_refs=None, tags=None, created_at=None, updated_at=None, insert_headers=None, project_id=None, tls_ciphers_policy=None):
        """ListenerV2Resp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._tenant_id = None
        self._name = None
        self._description = None
        self._admin_state_up = None
        self._loadbalancers = None
        self._connection_limit = None
        self._http2_enable = None
        self._protocol = None
        self._protocol_port = None
        self._default_pool_id = None
        self._default_tls_container_ref = None
        self._client_ca_tls_container_ref = None
        self._sni_container_refs = None
        self._tags = None
        self._created_at = None
        self._updated_at = None
        self._insert_headers = None
        self._project_id = None
        self._tls_ciphers_policy = None
        self.discriminator = None

        self.id = id
        self.tenant_id = tenant_id
        self.name = name
        self.description = description
        self.admin_state_up = admin_state_up
        self.loadbalancers = loadbalancers
        self.connection_limit = connection_limit
        self.http2_enable = http2_enable
        self.protocol = protocol
        self.protocol_port = protocol_port
        self.default_pool_id = default_pool_id
        self.default_tls_container_ref = default_tls_container_ref
        self.client_ca_tls_container_ref = client_ca_tls_container_ref
        self.sni_container_refs = sni_container_refs
        self.tags = tags
        self.created_at = created_at
        self.updated_at = updated_at
        self.insert_headers = insert_headers
        self.project_id = project_id
        self.tls_ciphers_policy = tls_ciphers_policy

    @property
    def id(self):
        """Gets the id of this ListenerV2Resp.

        监听器ID

        :return: The id of this ListenerV2Resp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListenerV2Resp.

        监听器ID

        :param id: The id of this ListenerV2Resp.
        :type: str
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ListenerV2Resp.

        监听器所在的项目ID。

        :return: The tenant_id of this ListenerV2Resp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ListenerV2Resp.

        监听器所在的项目ID。

        :param tenant_id: The tenant_id of this ListenerV2Resp.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this ListenerV2Resp.

        监听器名称。

        :return: The name of this ListenerV2Resp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListenerV2Resp.

        监听器名称。

        :param name: The name of this ListenerV2Resp.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListenerV2Resp.

        监听器的描述信息

        :return: The description of this ListenerV2Resp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListenerV2Resp.

        监听器的描述信息

        :param description: The description of this ListenerV2Resp.
        :type: str
        """
        self._description = description

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListenerV2Resp.

        监听器的管理状态。只支持设定为true，该字段的值无实际意义。

        :return: The admin_state_up of this ListenerV2Resp.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListenerV2Resp.

        监听器的管理状态。只支持设定为true，该字段的值无实际意义。

        :param admin_state_up: The admin_state_up of this ListenerV2Resp.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def loadbalancers(self):
        """Gets the loadbalancers of this ListenerV2Resp.

        监听器绑定的负载均衡器ID的列表。

        :return: The loadbalancers of this ListenerV2Resp.
        :rtype: list[ResourceList]
        """
        return self._loadbalancers

    @loadbalancers.setter
    def loadbalancers(self, loadbalancers):
        """Sets the loadbalancers of this ListenerV2Resp.

        监听器绑定的负载均衡器ID的列表。

        :param loadbalancers: The loadbalancers of this ListenerV2Resp.
        :type: list[ResourceList]
        """
        self._loadbalancers = loadbalancers

    @property
    def connection_limit(self):
        """Gets the connection_limit of this ListenerV2Resp.

        监听器的最大连接数。该字段为预留字段，暂未启用。默认为-1。

        :return: The connection_limit of this ListenerV2Resp.
        :rtype: int
        """
        return self._connection_limit

    @connection_limit.setter
    def connection_limit(self, connection_limit):
        """Sets the connection_limit of this ListenerV2Resp.

        监听器的最大连接数。该字段为预留字段，暂未启用。默认为-1。

        :param connection_limit: The connection_limit of this ListenerV2Resp.
        :type: int
        """
        self._connection_limit = connection_limit

    @property
    def http2_enable(self):
        """Gets the http2_enable of this ListenerV2Resp.

        HTTP2功能的开启状态。该字段只有当监听器的协议是TERMINATED_HTTPS时生效。

        :return: The http2_enable of this ListenerV2Resp.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this ListenerV2Resp.

        HTTP2功能的开启状态。该字段只有当监听器的协议是TERMINATED_HTTPS时生效。

        :param http2_enable: The http2_enable of this ListenerV2Resp.
        :type: bool
        """
        self._http2_enable = http2_enable

    @property
    def protocol(self):
        """Gets the protocol of this ListenerV2Resp.

        监听器的监听协议

        :return: The protocol of this ListenerV2Resp.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListenerV2Resp.

        监听器的监听协议

        :param protocol: The protocol of this ListenerV2Resp.
        :type: str
        """
        self._protocol = protocol

    @property
    def protocol_port(self):
        """Gets the protocol_port of this ListenerV2Resp.

        监听器的监听端口。

        :return: The protocol_port of this ListenerV2Resp.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this ListenerV2Resp.

        监听器的监听端口。

        :param protocol_port: The protocol_port of this ListenerV2Resp.
        :type: int
        """
        self._protocol_port = protocol_port

    @property
    def default_pool_id(self):
        """Gets the default_pool_id of this ListenerV2Resp.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。

        :return: The default_pool_id of this ListenerV2Resp.
        :rtype: str
        """
        return self._default_pool_id

    @default_pool_id.setter
    def default_pool_id(self, default_pool_id):
        """Sets the default_pool_id of this ListenerV2Resp.

        监听器的默认后端云服务器组ID。当请求没有匹配的转发策略时，转发到默认后端云服务器上处理。

        :param default_pool_id: The default_pool_id of this ListenerV2Resp.
        :type: str
        """
        self._default_pool_id = default_pool_id

    @property
    def default_tls_container_ref(self):
        """Gets the default_tls_container_ref of this ListenerV2Resp.

        监听器使用的服务器证书ID。

        :return: The default_tls_container_ref of this ListenerV2Resp.
        :rtype: str
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        """Sets the default_tls_container_ref of this ListenerV2Resp.

        监听器使用的服务器证书ID。

        :param default_tls_container_ref: The default_tls_container_ref of this ListenerV2Resp.
        :type: str
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def client_ca_tls_container_ref(self):
        """Gets the client_ca_tls_container_ref of this ListenerV2Resp.

        监听器使用的CA证书ID。

        :return: The client_ca_tls_container_ref of this ListenerV2Resp.
        :rtype: str
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        """Sets the client_ca_tls_container_ref of this ListenerV2Resp.

        监听器使用的CA证书ID。

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this ListenerV2Resp.
        :type: str
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def sni_container_refs(self):
        """Gets the sni_container_refs of this ListenerV2Resp.

        监听器使用的SNI证书（带域名的服务器证书）ID的列表。

        :return: The sni_container_refs of this ListenerV2Resp.
        :rtype: list[str]
        """
        return self._sni_container_refs

    @sni_container_refs.setter
    def sni_container_refs(self, sni_container_refs):
        """Sets the sni_container_refs of this ListenerV2Resp.

        监听器使用的SNI证书（带域名的服务器证书）ID的列表。

        :param sni_container_refs: The sni_container_refs of this ListenerV2Resp.
        :type: list[str]
        """
        self._sni_container_refs = sni_container_refs

    @property
    def tags(self):
        """Gets the tags of this ListenerV2Resp.

        监听器的标签。

        :return: The tags of this ListenerV2Resp.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListenerV2Resp.

        监听器的标签。

        :param tags: The tags of this ListenerV2Resp.
        :type: list[str]
        """
        self._tags = tags

    @property
    def created_at(self):
        """Gets the created_at of this ListenerV2Resp.

        监听器的创建时间。

        :return: The created_at of this ListenerV2Resp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ListenerV2Resp.

        监听器的创建时间。

        :param created_at: The created_at of this ListenerV2Resp.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ListenerV2Resp.

        监听器的更新时间。

        :return: The updated_at of this ListenerV2Resp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ListenerV2Resp.

        监听器的更新时间。

        :param updated_at: The updated_at of this ListenerV2Resp.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def insert_headers(self):
        """Gets the insert_headers of this ListenerV2Resp.


        :return: The insert_headers of this ListenerV2Resp.
        :rtype: InsertHeader
        """
        return self._insert_headers

    @insert_headers.setter
    def insert_headers(self, insert_headers):
        """Sets the insert_headers of this ListenerV2Resp.


        :param insert_headers: The insert_headers of this ListenerV2Resp.
        :type: InsertHeader
        """
        self._insert_headers = insert_headers

    @property
    def project_id(self):
        """Gets the project_id of this ListenerV2Resp.

        监听器所在的项目ID。

        :return: The project_id of this ListenerV2Resp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListenerV2Resp.

        监听器所在的项目ID。

        :param project_id: The project_id of this ListenerV2Resp.
        :type: str
        """
        self._project_id = project_id

    @property
    def tls_ciphers_policy(self):
        """Gets the tls_ciphers_policy of this ListenerV2Resp.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效，且默认值为tls-1-0。  取值包括：tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict多种安全策略

        :return: The tls_ciphers_policy of this ListenerV2Resp.
        :rtype: str
        """
        return self._tls_ciphers_policy

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, tls_ciphers_policy):
        """Sets the tls_ciphers_policy of this ListenerV2Resp.

        监听器使用的安全策略，仅对TERMINATED_HTTPS协议类型的监听器有效，且默认值为tls-1-0。  取值包括：tls-1-0, tls-1-1, tls-1-2, tls-1-2-strict多种安全策略

        :param tls_ciphers_policy: The tls_ciphers_policy of this ListenerV2Resp.
        :type: str
        """
        self._tls_ciphers_policy = tls_ciphers_policy

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
        if not isinstance(other, ListenerV2Resp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other