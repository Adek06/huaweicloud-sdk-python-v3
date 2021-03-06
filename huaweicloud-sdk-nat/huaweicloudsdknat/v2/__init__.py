# coding: utf-8

from __future__ import absolute_import

# import NatClient
from huaweicloudsdknat.v2.nat_client import NatClient
from huaweicloudsdknat.v2.nat_async_client import NatAsyncClient
# import models into sdk package
from huaweicloudsdknat.v2.model.batch_create_dnat_rules_request import BatchCreateDnatRulesRequest
from huaweicloudsdknat.v2.model.batch_create_dnat_rules_request_body import BatchCreateDnatRulesRequestBody
from huaweicloudsdknat.v2.model.batch_create_dnat_rules_response import BatchCreateDnatRulesResponse
from huaweicloudsdknat.v2.model.create_nat_gateway_dnat_option import CreateNatGatewayDnatOption
from huaweicloudsdknat.v2.model.create_nat_gateway_dnat_rule_option import CreateNatGatewayDnatRuleOption
from huaweicloudsdknat.v2.model.create_nat_gateway_dnat_rule_request import CreateNatGatewayDnatRuleRequest
from huaweicloudsdknat.v2.model.create_nat_gateway_dnat_rule_response import CreateNatGatewayDnatRuleResponse
from huaweicloudsdknat.v2.model.create_nat_gateway_option import CreateNatGatewayOption
from huaweicloudsdknat.v2.model.create_nat_gateway_request import CreateNatGatewayRequest
from huaweicloudsdknat.v2.model.create_nat_gateway_request_body import CreateNatGatewayRequestBody
from huaweicloudsdknat.v2.model.create_nat_gateway_response import CreateNatGatewayResponse
from huaweicloudsdknat.v2.model.create_nat_gateway_snat_rule_option import CreateNatGatewaySnatRuleOption
from huaweicloudsdknat.v2.model.create_nat_gateway_snat_rule_request import CreateNatGatewaySnatRuleRequest
from huaweicloudsdknat.v2.model.create_nat_gateway_snat_rule_request_option import CreateNatGatewaySnatRuleRequestOption
from huaweicloudsdknat.v2.model.create_nat_gateway_snat_rule_response import CreateNatGatewaySnatRuleResponse
from huaweicloudsdknat.v2.model.delete_nat_gateway_dnat_rule_request import DeleteNatGatewayDnatRuleRequest
from huaweicloudsdknat.v2.model.delete_nat_gateway_dnat_rule_response import DeleteNatGatewayDnatRuleResponse
from huaweicloudsdknat.v2.model.delete_nat_gateway_request import DeleteNatGatewayRequest
from huaweicloudsdknat.v2.model.delete_nat_gateway_response import DeleteNatGatewayResponse
from huaweicloudsdknat.v2.model.delete_nat_gateway_snat_rule_request import DeleteNatGatewaySnatRuleRequest
from huaweicloudsdknat.v2.model.delete_nat_gateway_snat_rule_response import DeleteNatGatewaySnatRuleResponse
from huaweicloudsdknat.v2.model.list_nat_gateway_dnat_rules_request import ListNatGatewayDnatRulesRequest
from huaweicloudsdknat.v2.model.list_nat_gateway_dnat_rules_response import ListNatGatewayDnatRulesResponse
from huaweicloudsdknat.v2.model.list_nat_gateway_snat_rules_request import ListNatGatewaySnatRulesRequest
from huaweicloudsdknat.v2.model.list_nat_gateway_snat_rules_response import ListNatGatewaySnatRulesResponse
from huaweicloudsdknat.v2.model.list_nat_gateways_request import ListNatGatewaysRequest
from huaweicloudsdknat.v2.model.list_nat_gateways_response import ListNatGatewaysResponse
from huaweicloudsdknat.v2.model.nat_gateway_dnat_rule_response_body import NatGatewayDnatRuleResponseBody
from huaweicloudsdknat.v2.model.nat_gateway_response_body import NatGatewayResponseBody
from huaweicloudsdknat.v2.model.nat_gateway_snat_rule_response_body import NatGatewaySnatRuleResponseBody
from huaweicloudsdknat.v2.model.show_nat_gateway_dnat_rule_request import ShowNatGatewayDnatRuleRequest
from huaweicloudsdknat.v2.model.show_nat_gateway_dnat_rule_response import ShowNatGatewayDnatRuleResponse
from huaweicloudsdknat.v2.model.show_nat_gateway_request import ShowNatGatewayRequest
from huaweicloudsdknat.v2.model.show_nat_gateway_response import ShowNatGatewayResponse
from huaweicloudsdknat.v2.model.show_nat_gateway_snat_rule_request import ShowNatGatewaySnatRuleRequest
from huaweicloudsdknat.v2.model.show_nat_gateway_snat_rule_response import ShowNatGatewaySnatRuleResponse
from huaweicloudsdknat.v2.model.update_nat_gateway_dnat_rule_option import UpdateNatGatewayDnatRuleOption
from huaweicloudsdknat.v2.model.update_nat_gateway_dnat_rule_request import UpdateNatGatewayDnatRuleRequest
from huaweicloudsdknat.v2.model.update_nat_gateway_dnat_rule_request_body import UpdateNatGatewayDnatRuleRequestBody
from huaweicloudsdknat.v2.model.update_nat_gateway_dnat_rule_response import UpdateNatGatewayDnatRuleResponse
from huaweicloudsdknat.v2.model.update_nat_gateway_option import UpdateNatGatewayOption
from huaweicloudsdknat.v2.model.update_nat_gateway_request import UpdateNatGatewayRequest
from huaweicloudsdknat.v2.model.update_nat_gateway_request_body import UpdateNatGatewayRequestBody
from huaweicloudsdknat.v2.model.update_nat_gateway_response import UpdateNatGatewayResponse
from huaweicloudsdknat.v2.model.update_nat_gateway_snat_rule_option import UpdateNatGatewaySnatRuleOption
from huaweicloudsdknat.v2.model.update_nat_gateway_snat_rule_request import UpdateNatGatewaySnatRuleRequest
from huaweicloudsdknat.v2.model.update_nat_gateway_snat_rule_request_option import UpdateNatGatewaySnatRuleRequestOption
from huaweicloudsdknat.v2.model.update_nat_gateway_snat_rule_response import UpdateNatGatewaySnatRuleResponse

