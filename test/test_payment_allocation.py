# coding: utf-8

"""
    Sage Business Cloud Accounting - Accounts

    Documentation of the Sage Business Cloud Accounting API.  # noqa: E501

    The version of the OpenAPI document: 3.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.payment_allocation import PaymentAllocation  # noqa: E501
from openapi_client.rest import ApiException

class TestPaymentAllocation(unittest.TestCase):
    """PaymentAllocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentAllocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.payment_allocation.PaymentAllocation()  # noqa: E501
        if include_optional :
            return PaymentAllocation(
                links = [
                    openapi_client.models.link.Link(
                        href = '0', 
                        rel = '0', 
                        type = '0', )
                    ], 
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                type = '0', 
                reference = '0', 
                amount = 1.337, 
                discount = 1.337, 
                stripe_transaction_id = '0', 
                contact_allocation = openapi_client.models.contact_allocation.ContactAllocation(
                    legacy_id = 56, 
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    links = [
                        openapi_client.models.link.Link(
                            href = '0', 
                            rel = '0', 
                            type = '0', )
                        ], 
                    transaction = openapi_client.models.base.Base(
                        legacy_id = 56, 
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    transaction_type = openapi_client.models.base.Base(
                        legacy_id = 56, 
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    contact = openapi_client.models.base.Base(
                        legacy_id = 56, 
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    allocated_artefacts = [
                        openapi_client.models.allocated_artefact.AllocatedArtefact(
                            legacy_id = 56, 
                            id = '0', 
                            artefact = openapi_client.models.generic.Generic(
                                legacy_id = 56, 
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            amount = 1.337, )
                        ], ), 
                artefact = openapi_client.models.generic.Generic(
                    legacy_id = 56, 
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', 
                    links = [
                        openapi_client.models.link.Link(
                            href = '0', 
                            rel = '0', 
                            type = '0', )
                        ], ), 
                contact_payment = openapi_client.models.contact_payment.ContactPayment(
                    legacy_id = 56, 
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    links = [
                        openapi_client.models.link.Link(
                            href = '0', 
                            rel = '0', 
                            type = '0', )
                        ], 
                    transaction = openapi_client.models.base.Base(
                        legacy_id = 56, 
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    transaction_type = openapi_client.models.base.Base(
                        legacy_id = 56, 
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    payment_method = openapi_client.models.base.Base(
                        legacy_id = 56, 
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    contact = openapi_client.models.base.Base(
                        legacy_id = 56, 
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    bank_account = openapi_client.models.base.Base(
                        legacy_id = 56, 
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    net_amount = 1.337, 
                    tax_amount = 1.337, 
                    total_amount = 1.337, 
                    currency = openapi_client.models.base.Base(
                        legacy_id = 56, 
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    exchange_rate = 1.337, 
                    base_currency_net_amount = 1.337, 
                    base_currency_tax_amount = 1.337, 
                    base_currency_total_amount = 1.337, 
                    base_currency_currency_charge = 1.337, 
                    reference = '0', 
                    allocated_artefacts = [
                        openapi_client.models.allocated_payment_artefact.AllocatedPaymentArtefact(
                            legacy_id = 56, 
                            id = '0', 
                            artefact = openapi_client.models.generic.Generic(
                                legacy_id = 56, 
                                id = '0', 
                                displayed_as = '0', 
                                __path = '0', ), 
                            amount = 1.337, 
                            discount = 1.337, )
                        ], 
                    tax_rate = openapi_client.models.base.Base(
                        legacy_id = 56, 
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', ), 
                    payment_on_account = openapi_client.models.payment_on_account.PaymentOnAccount(
                        legacy_id = 56, 
                        id = '0', 
                        displayed_as = '0', 
                        __path = '0', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        contact_name = '0', 
                        contact_reference = '0', 
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        reference = '0', 
                        net_amount = 1.337, 
                        tax_amount = 1.337, 
                        total_amount = 1.337, 
                        outstanding_amount = 1.337, 
                        exchange_rate = 1.337, 
                        base_currency_net_amount = 1.337, 
                        base_currency_tax_amount = 1.337, 
                        base_currency_total_amount = 1.337, 
                        base_currency_outstanding_amount = 1.337, 
                        status = openapi_client.models.base.Base(
                            legacy_id = 56, 
                            id = '0', 
                            displayed_as = '0', 
                            __path = '0', ), ), 
                    editable = True, ), 
                displayed_as = '0', 
                negative_payment = True
            )
        else :
            return PaymentAllocation(
        )

    def testPaymentAllocation(self):
        """Test PaymentAllocation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
