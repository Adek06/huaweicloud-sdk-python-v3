# coding: utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

from requests.exceptions import ConnectionError
from urllib3.exceptions import SSLError, NewConnectionError

from huaweicloudsdkcore.exceptions import exceptions


class SdkResponse:
    def __init__(self, code, headers, body):
        self.status_code = code
        self.header_params = headers
        self.body = body


class FutureSdkResponse:
    def __init__(self, future, logger):
        self.__future = future
        self.__logger = logger

    def result(self):
        try:
            response = self.__future.result().data
        except ConnectionError as connectionError:
            for each in connectionError.args:
                if isinstance(each.reason, SSLError):
                    self.__logger.error("Sync SslHandShakeException occurred. %s" % str(each.reason))
                    raise exceptions.SslHandShakeException(str(each.reason))
                if isinstance(each.reason, NewConnectionError):
                    self.__logger.error("Sync ConnectionException occurred. %s" % str(each.reason))
                    raise exceptions.ConnectionException(str(each.reason))
            self.__logger.error("ConnectionException occurred. %s" % str(connectionError))
            raise exceptions.ConnectionException(str(connectionError))
        return response
