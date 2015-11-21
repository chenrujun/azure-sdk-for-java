# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 0.13.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Serializer, Deserializer
from msrest.service_client import async_request
from msrest.exceptions import DeserializationError, HttpOperationError
from msrestazure.azure_exceptions import CloudError
import uuid

from ..models import *


class pagingOperations(object):

    def __init__(self, client, config, serializer, derserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = derserializer

        self.config = config

    @async_request
    def get_single_pages(self, custom_headers={}, raw=False, callback=None):
        """

        A paging operation that finishes on the first call without a nextlink

        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: object or (object, requests.response) or
        concurrent.futures.Future
        """

        def internal_paging(next_link=None, raw=False):

            if next_link is None:
                # Construct URL
                url = '/paging/single'

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(request, header_parameters)

            if response.status_code not in [200]:
                raise CloudError(self._deserialize, response)

            return response

        response = internal_paging()

        # Deserialize response
        deserialized = ProductPaged(response, internal_paging, self._deserialize.dependencies)

        if raw:
            return deserialized, response

        return deserialized

    @async_request
    def get_multiple_pages(self, client_request_id=None, custom_headers={}, raw=False, callback=None):
        """

        A paging operation that includes a nextLink that has 10 pages

        :param client_request_id:
        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type client_request_id: str or none
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: object or (object, requests.response) or
        concurrent.futures.Future
        """

        def internal_paging(next_link=None, raw=False):

            if next_link is None:
                # Construct URL
                url = '/paging/multiple'

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if client_request_id is not None:
                header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(request, header_parameters)

            if response.status_code not in [200]:
                raise CloudError(self._deserialize, response)

            return response

        response = internal_paging()

        # Deserialize response
        deserialized = ProductPaged(response, internal_paging, self._deserialize.dependencies)

        if raw:
            return deserialized, response

        return deserialized

    @async_request
    def get_multiple_pages_retry_first(self, custom_headers={}, raw=False, callback=None):
        """

        A paging operation that fails on the first call with 500 and then
        retries and then get a response including a nextLink that has 10 pages

        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: object or (object, requests.response) or
        concurrent.futures.Future
        """

        def internal_paging(next_link=None, raw=False):

            if next_link is None:
                # Construct URL
                url = '/paging/multiple/retryfirst'

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(request, header_parameters)

            if response.status_code not in [200]:
                raise CloudError(self._deserialize, response)

            return response

        response = internal_paging()

        # Deserialize response
        deserialized = ProductPaged(response, internal_paging, self._deserialize.dependencies)

        if raw:
            return deserialized, response

        return deserialized

    @async_request
    def get_multiple_pages_retry_second(self, custom_headers={}, raw=False, callback=None):
        """

        A paging operation that includes a nextLink that has 10 pages, of
        which the 2nd call fails first with 500. The client should retry and
        finish all 10 pages eventually.

        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: object or (object, requests.response) or
        concurrent.futures.Future
        """

        def internal_paging(next_link=None, raw=False):

            if next_link is None:
                # Construct URL
                url = '/paging/multiple/retrysecond'

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(request, header_parameters)

            if response.status_code not in [200]:
                raise CloudError(self._deserialize, response)

            return response

        response = internal_paging()

        # Deserialize response
        deserialized = ProductPaged(response, internal_paging, self._deserialize.dependencies)

        if raw:
            return deserialized, response

        return deserialized

    @async_request
    def get_single_pages_failure(self, custom_headers={}, raw=False, callback=None):
        """

        A paging operation that receives a 400 on the first call

        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: object or (object, requests.response) or
        concurrent.futures.Future
        """

        def internal_paging(next_link=None, raw=False):

            if next_link is None:
                # Construct URL
                url = '/paging/single/failure'

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(request, header_parameters)

            if response.status_code not in [200]:
                raise CloudError(self._deserialize, response)

            return response

        response = internal_paging()

        # Deserialize response
        deserialized = ProductPaged(response, internal_paging, self._deserialize.dependencies)

        if raw:
            return deserialized, response

        return deserialized

    @async_request
    def get_multiple_pages_failure(self, custom_headers={}, raw=False, callback=None):
        """

        A paging operation that receives a 400 on the second call

        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: object or (object, requests.response) or
        concurrent.futures.Future
        """

        def internal_paging(next_link=None, raw=False):

            if next_link is None:
                # Construct URL
                url = '/paging/multiple/failure'

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(request, header_parameters)

            if response.status_code not in [200]:
                raise CloudError(self._deserialize, response)

            return response

        response = internal_paging()

        # Deserialize response
        deserialized = ProductPaged(response, internal_paging, self._deserialize.dependencies)

        if raw:
            return deserialized, response

        return deserialized

    @async_request
    def get_multiple_pages_failure_uri(self, custom_headers={}, raw=False, callback=None):
        """

        A paging operation that receives an invalid nextLink

        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: object or (object, requests.response) or
        concurrent.futures.Future
        """

        def internal_paging(next_link=None, raw=False):

            if next_link is None:
                # Construct URL
                url = '/paging/multiple/failureuri'

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(request, header_parameters)

            if response.status_code not in [200]:
                raise CloudError(self._deserialize, response)

            return response

        response = internal_paging()

        # Deserialize response
        deserialized = ProductPaged(response, internal_paging, self._deserialize.dependencies)

        if raw:
            return deserialized, response

        return deserialized
