# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import (
    Card,
    CardProvisionResponse,
    card_create_params,
    card_update_params,
    card_provision_params,
)
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
from ..._base_client import (
    make_request_options,
)
from .financial_transactions import (
    FinancialTransactions,
    AsyncFinancialTransactions,
    FinancialTransactionsWithRawResponse,
    AsyncFinancialTransactionsWithRawResponse,
    FinancialTransactionsWithStreamingResponse,
    AsyncFinancialTransactionsWithStreamingResponse,
)

__all__ = ["Cards", "AsyncCards"]


class Cards(SyncAPIResource):
    @cached_property
    def financial_transactions(self) -> FinancialTransactions:
        return FinancialTransactions(self._client)

    @cached_property
    def with_raw_response(self) -> CardsWithRawResponse:
        return CardsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardsWithStreamingResponse:
        return CardsWithStreamingResponse(self)

    def create(
        self,
        *,
        type: Literal["VIRTUAL", "PHYSICAL", "MERCHANT_LOCKED", "SINGLE_USE"],
        account_token: str | NotGiven = NOT_GIVEN,
        card_program_token: str | NotGiven = NOT_GIVEN,
        carrier: card_create_params.Carrier | NotGiven = NOT_GIVEN,
        digital_card_art_token: str | NotGiven = NOT_GIVEN,
        exp_month: str | NotGiven = NOT_GIVEN,
        exp_year: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        shipping_address: card_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_method: Literal["STANDARD", "STANDARD_WITH_TRACKING", "PRIORITY", "EXPRESS", "2_DAY", "EXPEDITED"]
        | NotGiven = NOT_GIVEN,
        spend_limit: int | NotGiven = NOT_GIVEN,
        spend_limit_duration: Literal["ANNUALLY", "FOREVER", "MONTHLY", "TRANSACTION"] | NotGiven = NOT_GIVEN,
        state: Literal["OPEN", "PAUSED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """Create a new virtual or physical card.

        Parameters `pin`, `shipping_address`, and
        `product_id` only apply to physical cards.

        Args:
          type:
              Card types:

              - `VIRTUAL` - Card will authorize at any merchant and can be added to a digital
                wallet like Apple Pay or Google Pay (if the card program is digital
                wallet-enabled).
              - `PHYSICAL` - Manufactured and sent to the cardholder. We offer white label
                branding, credit, ATM, PIN debit, chip/EMV, NFC and magstripe functionality.
                Reach out at [acme.com/contact](https://acme.com/contact) for more
                information.
              - `SINGLE_USE` - Card is closed upon first successful authorization.
              - `MERCHANT_LOCKED` - _[Deprecated]_ Card is locked to the first merchant that
                successfully authorizes the card.

          account_token: Globally unique identifier for the account that the card will be associated
              with. Required for programs enrolling users using the
              [/account_holders endpoint](https://docs.acme.com/docs/account-holders-kyc). See
              [Managing Your Program](doc:managing-your-program) for more information.

          card_program_token: For card programs with more than one BIN range. This must be configured with
              Acme before use. Identifies the card program/BIN range under which to create the
              card. If omitted, will utilize the program's default `card_program_token`. In
              Sandbox, use 00000000-0000-0000-1000-000000000000 and
              00000000-0000-0000-2000-000000000000 to test creating cards on specific card
              programs.

          digital_card_art_token: Specifies the digital card art to be displayed in the user’s digital wallet
              after tokenization. This artwork must be approved by Mastercard and configured
              by Acme to use. See
              [Flexible Card Art Guide](https://docs.acme.com/docs/about-digital-wallets#flexible-card-art).

          exp_month: Two digit (MM) expiry month. If neither `exp_month` nor `exp_year` is provided,
              an expiration date will be generated.

          exp_year: Four digit (yyyy) expiry year. If neither `exp_month` nor `exp_year` is
              provided, an expiration date will be generated.

          memo: Friendly name to identify the card. We recommend against using this field to
              store JSON data as it can cause unexpected behavior.

          pin: Encrypted PIN block (in base64). Only applies to cards of type `PHYSICAL` and
              `VIRTUAL`. See
              [Encrypted PIN Block](https://docs.acme.com/docs/cards#encrypted-pin-block-enterprise).

          product_id: Only applicable to cards of type `PHYSICAL`. This must be configured with Acme
              before use. Specifies the configuration (i.e., physical card art) that the card
              should be manufactured with.

          shipping_method: Shipping method for the card. Only applies to cards of type PHYSICAL. Use of
              options besides `STANDARD` require additional permissions.

              - `STANDARD` - USPS regular mail or similar international option, with no
                tracking
              - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
                with tracking
              - `PRIORITY` - USPS Priority, 1-3 day shipping, with tracking
              - `EXPRESS` - FedEx Express, 3-day shipping, with tracking
              - `2_DAY` - FedEx 2-day shipping, with tracking
              - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
                tracking

          spend_limit: Amount (in cents) to limit approved authorizations. Transaction requests above
              the spend limit will be declined. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the card
              limit.

          spend_limit_duration:
              Spend limit duration values:

              - `ANNUALLY` - Card will authorize transactions up to spend limit in a calendar
                year.
              - `FOREVER` - Card will authorize only up to spend limit for the entire lifetime
                of the card.
              - `MONTHLY` - Card will authorize transactions up to spend limit for the
                trailing month. Month is calculated as this calendar date one month prior.
              - `TRANSACTION` - Card will authorize multiple transactions if each individual
                transaction is under the spend limit.

          state:
              Card state values:

              - `OPEN` - Card will approve authorizations (if they match card and account
                parameters).
              - `PAUSED` - Card will decline authorizations, but can be resumed at a later
                time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cards",
            body=maybe_transform(
                {
                    "type": type,
                    "account_token": account_token,
                    "card_program_token": card_program_token,
                    "carrier": carrier,
                    "digital_card_art_token": digital_card_art_token,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "memo": memo,
                    "pin": pin,
                    "product_id": product_id,
                    "shipping_address": shipping_address,
                    "shipping_method": shipping_method,
                    "spend_limit": spend_limit,
                    "spend_limit_duration": spend_limit_duration,
                    "state": state,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def retrieve(
        self,
        card_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """
        Get card configuration such as spend limit and state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return self._get(
            f"/cards/{card_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def update(
        self,
        card_token: str,
        *,
        auth_rule_token: str | NotGiven = NOT_GIVEN,
        digital_card_art_token: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        spend_limit: int | NotGiven = NOT_GIVEN,
        spend_limit_duration: Literal["ANNUALLY", "FOREVER", "MONTHLY", "TRANSACTION"] | NotGiven = NOT_GIVEN,
        state: Literal["CLOSED", "OPEN", "PAUSED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """Update the specified properties of the card.

        Unsupplied properties will remain
        unchanged. `pin` parameter only applies to physical cards.

        _Note: setting a card to a `CLOSED` state is a final action that cannot be
        undone._

        Args:
          auth_rule_token: Identifier for any Auth Rules that will be applied to transactions taking place
              with the card.

          digital_card_art_token: Specifies the digital card art to be displayed in the user’s digital wallet
              after tokenization. This artwork must be approved by Mastercard and configured
              by Acme to use. See
              [Flexible Card Art Guide](https://docs.acme.com/docs/about-digital-wallets#flexible-card-art).

          memo: Friendly name to identify the card. We recommend against using this field to
              store JSON data as it can cause unexpected behavior.

          pin: Encrypted PIN block (in base64). Only applies to cards of type `PHYSICAL` and
              `VIRTUAL`. See
              [Encrypted PIN Block](https://docs.acme.com/docs/cards#encrypted-pin-block-enterprise).

          spend_limit: Amount (in cents) to limit approved authorizations. Transaction requests above
              the spend limit will be declined. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the card
              limit.

          spend_limit_duration:
              Spend limit duration values:

              - `ANNUALLY` - Card will authorize transactions up to spend limit in a calendar
                year.
              - `FOREVER` - Card will authorize only up to spend limit for the entire lifetime
                of the card.
              - `MONTHLY` - Card will authorize transactions up to spend limit for the
                trailing month. Month is calculated as this calendar date one month prior.
              - `TRANSACTION` - Card will authorize multiple transactions if each individual
                transaction is under the spend limit.

          state:
              Card state values:

              - `CLOSED` - Card will no longer approve authorizations. Closing a card cannot
                be undone.
              - `OPEN` - Card will approve authorizations (if they match card and account
                parameters).
              - `PAUSED` - Card will decline authorizations, but can be resumed at a later
                time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return self._patch(
            f"/cards/{card_token}",
            body=maybe_transform(
                {
                    "auth_rule_token": auth_rule_token,
                    "digital_card_art_token": digital_card_art_token,
                    "memo": memo,
                    "pin": pin,
                    "spend_limit": spend_limit,
                    "spend_limit_duration": spend_limit_duration,
                    "state": state,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def provision(
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
    ) -> CardProvisionResponse:
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
                card_provision_params.CardProvisionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardProvisionResponse,
        )


class AsyncCards(AsyncAPIResource):
    @cached_property
    def financial_transactions(self) -> AsyncFinancialTransactions:
        return AsyncFinancialTransactions(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCardsWithRawResponse:
        return AsyncCardsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardsWithStreamingResponse:
        return AsyncCardsWithStreamingResponse(self)

    async def create(
        self,
        *,
        type: Literal["VIRTUAL", "PHYSICAL", "MERCHANT_LOCKED", "SINGLE_USE"],
        account_token: str | NotGiven = NOT_GIVEN,
        card_program_token: str | NotGiven = NOT_GIVEN,
        carrier: card_create_params.Carrier | NotGiven = NOT_GIVEN,
        digital_card_art_token: str | NotGiven = NOT_GIVEN,
        exp_month: str | NotGiven = NOT_GIVEN,
        exp_year: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        shipping_address: card_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_method: Literal["STANDARD", "STANDARD_WITH_TRACKING", "PRIORITY", "EXPRESS", "2_DAY", "EXPEDITED"]
        | NotGiven = NOT_GIVEN,
        spend_limit: int | NotGiven = NOT_GIVEN,
        spend_limit_duration: Literal["ANNUALLY", "FOREVER", "MONTHLY", "TRANSACTION"] | NotGiven = NOT_GIVEN,
        state: Literal["OPEN", "PAUSED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """Create a new virtual or physical card.

        Parameters `pin`, `shipping_address`, and
        `product_id` only apply to physical cards.

        Args:
          type:
              Card types:

              - `VIRTUAL` - Card will authorize at any merchant and can be added to a digital
                wallet like Apple Pay or Google Pay (if the card program is digital
                wallet-enabled).
              - `PHYSICAL` - Manufactured and sent to the cardholder. We offer white label
                branding, credit, ATM, PIN debit, chip/EMV, NFC and magstripe functionality.
                Reach out at [acme.com/contact](https://acme.com/contact) for more
                information.
              - `SINGLE_USE` - Card is closed upon first successful authorization.
              - `MERCHANT_LOCKED` - _[Deprecated]_ Card is locked to the first merchant that
                successfully authorizes the card.

          account_token: Globally unique identifier for the account that the card will be associated
              with. Required for programs enrolling users using the
              [/account_holders endpoint](https://docs.acme.com/docs/account-holders-kyc). See
              [Managing Your Program](doc:managing-your-program) for more information.

          card_program_token: For card programs with more than one BIN range. This must be configured with
              Acme before use. Identifies the card program/BIN range under which to create the
              card. If omitted, will utilize the program's default `card_program_token`. In
              Sandbox, use 00000000-0000-0000-1000-000000000000 and
              00000000-0000-0000-2000-000000000000 to test creating cards on specific card
              programs.

          digital_card_art_token: Specifies the digital card art to be displayed in the user’s digital wallet
              after tokenization. This artwork must be approved by Mastercard and configured
              by Acme to use. See
              [Flexible Card Art Guide](https://docs.acme.com/docs/about-digital-wallets#flexible-card-art).

          exp_month: Two digit (MM) expiry month. If neither `exp_month` nor `exp_year` is provided,
              an expiration date will be generated.

          exp_year: Four digit (yyyy) expiry year. If neither `exp_month` nor `exp_year` is
              provided, an expiration date will be generated.

          memo: Friendly name to identify the card. We recommend against using this field to
              store JSON data as it can cause unexpected behavior.

          pin: Encrypted PIN block (in base64). Only applies to cards of type `PHYSICAL` and
              `VIRTUAL`. See
              [Encrypted PIN Block](https://docs.acme.com/docs/cards#encrypted-pin-block-enterprise).

          product_id: Only applicable to cards of type `PHYSICAL`. This must be configured with Acme
              before use. Specifies the configuration (i.e., physical card art) that the card
              should be manufactured with.

          shipping_method: Shipping method for the card. Only applies to cards of type PHYSICAL. Use of
              options besides `STANDARD` require additional permissions.

              - `STANDARD` - USPS regular mail or similar international option, with no
                tracking
              - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
                with tracking
              - `PRIORITY` - USPS Priority, 1-3 day shipping, with tracking
              - `EXPRESS` - FedEx Express, 3-day shipping, with tracking
              - `2_DAY` - FedEx 2-day shipping, with tracking
              - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
                tracking

          spend_limit: Amount (in cents) to limit approved authorizations. Transaction requests above
              the spend limit will be declined. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the card
              limit.

          spend_limit_duration:
              Spend limit duration values:

              - `ANNUALLY` - Card will authorize transactions up to spend limit in a calendar
                year.
              - `FOREVER` - Card will authorize only up to spend limit for the entire lifetime
                of the card.
              - `MONTHLY` - Card will authorize transactions up to spend limit for the
                trailing month. Month is calculated as this calendar date one month prior.
              - `TRANSACTION` - Card will authorize multiple transactions if each individual
                transaction is under the spend limit.

          state:
              Card state values:

              - `OPEN` - Card will approve authorizations (if they match card and account
                parameters).
              - `PAUSED` - Card will decline authorizations, but can be resumed at a later
                time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cards",
            body=maybe_transform(
                {
                    "type": type,
                    "account_token": account_token,
                    "card_program_token": card_program_token,
                    "carrier": carrier,
                    "digital_card_art_token": digital_card_art_token,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "memo": memo,
                    "pin": pin,
                    "product_id": product_id,
                    "shipping_address": shipping_address,
                    "shipping_method": shipping_method,
                    "spend_limit": spend_limit,
                    "spend_limit_duration": spend_limit_duration,
                    "state": state,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    async def retrieve(
        self,
        card_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """
        Get card configuration such as spend limit and state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return await self._get(
            f"/cards/{card_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    async def update(
        self,
        card_token: str,
        *,
        auth_rule_token: str | NotGiven = NOT_GIVEN,
        digital_card_art_token: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        spend_limit: int | NotGiven = NOT_GIVEN,
        spend_limit_duration: Literal["ANNUALLY", "FOREVER", "MONTHLY", "TRANSACTION"] | NotGiven = NOT_GIVEN,
        state: Literal["CLOSED", "OPEN", "PAUSED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """Update the specified properties of the card.

        Unsupplied properties will remain
        unchanged. `pin` parameter only applies to physical cards.

        _Note: setting a card to a `CLOSED` state is a final action that cannot be
        undone._

        Args:
          auth_rule_token: Identifier for any Auth Rules that will be applied to transactions taking place
              with the card.

          digital_card_art_token: Specifies the digital card art to be displayed in the user’s digital wallet
              after tokenization. This artwork must be approved by Mastercard and configured
              by Acme to use. See
              [Flexible Card Art Guide](https://docs.acme.com/docs/about-digital-wallets#flexible-card-art).

          memo: Friendly name to identify the card. We recommend against using this field to
              store JSON data as it can cause unexpected behavior.

          pin: Encrypted PIN block (in base64). Only applies to cards of type `PHYSICAL` and
              `VIRTUAL`. See
              [Encrypted PIN Block](https://docs.acme.com/docs/cards#encrypted-pin-block-enterprise).

          spend_limit: Amount (in cents) to limit approved authorizations. Transaction requests above
              the spend limit will be declined. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the card
              limit.

          spend_limit_duration:
              Spend limit duration values:

              - `ANNUALLY` - Card will authorize transactions up to spend limit in a calendar
                year.
              - `FOREVER` - Card will authorize only up to spend limit for the entire lifetime
                of the card.
              - `MONTHLY` - Card will authorize transactions up to spend limit for the
                trailing month. Month is calculated as this calendar date one month prior.
              - `TRANSACTION` - Card will authorize multiple transactions if each individual
                transaction is under the spend limit.

          state:
              Card state values:

              - `CLOSED` - Card will no longer approve authorizations. Closing a card cannot
                be undone.
              - `OPEN` - Card will approve authorizations (if they match card and account
                parameters).
              - `PAUSED` - Card will decline authorizations, but can be resumed at a later
                time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return await self._patch(
            f"/cards/{card_token}",
            body=maybe_transform(
                {
                    "auth_rule_token": auth_rule_token,
                    "digital_card_art_token": digital_card_art_token,
                    "memo": memo,
                    "pin": pin,
                    "spend_limit": spend_limit,
                    "spend_limit_duration": spend_limit_duration,
                    "state": state,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    async def provision(
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
    ) -> CardProvisionResponse:
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
                card_provision_params.CardProvisionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardProvisionResponse,
        )


class CardsWithRawResponse:
    def __init__(self, cards: Cards) -> None:
        self._cards = cards

        self.create = to_raw_response_wrapper(
            cards.create,
        )
        self.retrieve = to_raw_response_wrapper(
            cards.retrieve,
        )
        self.update = to_raw_response_wrapper(
            cards.update,
        )
        self.provision = to_raw_response_wrapper(
            cards.provision,
        )

    @cached_property
    def financial_transactions(self) -> FinancialTransactionsWithRawResponse:
        return FinancialTransactionsWithRawResponse(self._cards.financial_transactions)


class AsyncCardsWithRawResponse:
    def __init__(self, cards: AsyncCards) -> None:
        self._cards = cards

        self.create = async_to_raw_response_wrapper(
            cards.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            cards.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            cards.update,
        )
        self.provision = async_to_raw_response_wrapper(
            cards.provision,
        )

    @cached_property
    def financial_transactions(self) -> AsyncFinancialTransactionsWithRawResponse:
        return AsyncFinancialTransactionsWithRawResponse(self._cards.financial_transactions)


class CardsWithStreamingResponse:
    def __init__(self, cards: Cards) -> None:
        self._cards = cards

        self.create = to_streamed_response_wrapper(
            cards.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            cards.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            cards.update,
        )
        self.provision = to_streamed_response_wrapper(
            cards.provision,
        )

    @cached_property
    def financial_transactions(self) -> FinancialTransactionsWithStreamingResponse:
        return FinancialTransactionsWithStreamingResponse(self._cards.financial_transactions)


class AsyncCardsWithStreamingResponse:
    def __init__(self, cards: AsyncCards) -> None:
        self._cards = cards

        self.create = async_to_streamed_response_wrapper(
            cards.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            cards.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            cards.update,
        )
        self.provision = async_to_streamed_response_wrapper(
            cards.provision,
        )

    @cached_property
    def financial_transactions(self) -> AsyncFinancialTransactionsWithStreamingResponse:
        return AsyncFinancialTransactionsWithStreamingResponse(self._cards.financial_transactions)
