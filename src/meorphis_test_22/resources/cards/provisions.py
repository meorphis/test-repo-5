# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cards import ProvisionPostProvisionResponse, provision_post_provision_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["Provisions", "AsyncProvisions"]


class Provisions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProvisionsWithRawResponse:
        return ProvisionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProvisionsWithStreamingResponse:
        return ProvisionsWithStreamingResponse(self)

    def post_provision(
        self,
        card_token: str,
        *,
        certificate: str | NotGiven = NOT_GIVEN,
        digital_wallet: Literal["APPLE_PAY", "GOOGLE_PAY", "SAMSUNG_PAY"] | NotGiven = NOT_GIVEN,
        nonce: str | NotGiven = NOT_GIVEN,
        nonce_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProvisionPostProvisionResponse:
        """
        Allow your cardholders to directly add payment cards to the device's digital
        wallet (e.g. Apple Pay) with one touch from your app.

        This requires some additional setup and configuration. Please
        [Contact Us](https://acme.com/contact) or your Customer Success representative
        for more information.

        Args:
          certificate: Only applicable if `digital_wallet` is `APPLE_PAY`. Omit to receive only
              `activationData` in the response. Apple's public leaf certificate. Base64
              encoded in PEM format with headers `(-----BEGIN CERTIFICATE-----)` and trailers
              omitted. Provided by the device's wallet.

          digital_wallet: Name of digital wallet provider.

          nonce: Only applicable if `digital_wallet` is `APPLE_PAY`. Omit to receive only
              `activationData` in the response. Base64 cryptographic nonce provided by the
              device's wallet.

          nonce_signature: Only applicable if `digital_wallet` is `APPLE_PAY`. Omit to receive only
              `activationData` in the response. Base64 cryptographic nonce provided by the
              device's wallet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return self._post(
            f"/cards/{card_token}/provision",
            body=maybe_transform(
                {
                    "certificate": certificate,
                    "digital_wallet": digital_wallet,
                    "nonce": nonce,
                    "nonce_signature": nonce_signature,
                },
                provision_post_provision_params.ProvisionPostProvisionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProvisionPostProvisionResponse,
        )


class AsyncProvisions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProvisionsWithRawResponse:
        return AsyncProvisionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProvisionsWithStreamingResponse:
        return AsyncProvisionsWithStreamingResponse(self)

    async def post_provision(
        self,
        card_token: str,
        *,
        certificate: str | NotGiven = NOT_GIVEN,
        digital_wallet: Literal["APPLE_PAY", "GOOGLE_PAY", "SAMSUNG_PAY"] | NotGiven = NOT_GIVEN,
        nonce: str | NotGiven = NOT_GIVEN,
        nonce_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProvisionPostProvisionResponse:
        """
        Allow your cardholders to directly add payment cards to the device's digital
        wallet (e.g. Apple Pay) with one touch from your app.

        This requires some additional setup and configuration. Please
        [Contact Us](https://acme.com/contact) or your Customer Success representative
        for more information.

        Args:
          certificate: Only applicable if `digital_wallet` is `APPLE_PAY`. Omit to receive only
              `activationData` in the response. Apple's public leaf certificate. Base64
              encoded in PEM format with headers `(-----BEGIN CERTIFICATE-----)` and trailers
              omitted. Provided by the device's wallet.

          digital_wallet: Name of digital wallet provider.

          nonce: Only applicable if `digital_wallet` is `APPLE_PAY`. Omit to receive only
              `activationData` in the response. Base64 cryptographic nonce provided by the
              device's wallet.

          nonce_signature: Only applicable if `digital_wallet` is `APPLE_PAY`. Omit to receive only
              `activationData` in the response. Base64 cryptographic nonce provided by the
              device's wallet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return await self._post(
            f"/cards/{card_token}/provision",
            body=maybe_transform(
                {
                    "certificate": certificate,
                    "digital_wallet": digital_wallet,
                    "nonce": nonce,
                    "nonce_signature": nonce_signature,
                },
                provision_post_provision_params.ProvisionPostProvisionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProvisionPostProvisionResponse,
        )


class ProvisionsWithRawResponse:
    def __init__(self, provisions: Provisions) -> None:
        self._provisions = provisions

        self.post_provision = to_raw_response_wrapper(
            provisions.post_provision,
        )


class AsyncProvisionsWithRawResponse:
    def __init__(self, provisions: AsyncProvisions) -> None:
        self._provisions = provisions

        self.post_provision = async_to_raw_response_wrapper(
            provisions.post_provision,
        )


class ProvisionsWithStreamingResponse:
    def __init__(self, provisions: Provisions) -> None:
        self._provisions = provisions

        self.post_provision = to_streamed_response_wrapper(
            provisions.post_provision,
        )


class AsyncProvisionsWithStreamingResponse:
    def __init__(self, provisions: AsyncProvisions) -> None:
        self._provisions = provisions

        self.post_provision = async_to_streamed_response_wrapper(
            provisions.post_provision,
        )
