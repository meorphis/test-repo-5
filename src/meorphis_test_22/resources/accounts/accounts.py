# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import AccountConfiguration, account_update_params
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
from .credit_configuration import (
    CreditConfiguration,
    AsyncCreditConfiguration,
    CreditConfigurationWithRawResponse,
    AsyncCreditConfigurationWithRawResponse,
    CreditConfigurationWithStreamingResponse,
    AsyncCreditConfigurationWithStreamingResponse,
)

__all__ = ["Accounts", "AsyncAccounts"]


class Accounts(SyncAPIResource):
    @cached_property
    def credit_configuration(self) -> CreditConfiguration:
        return CreditConfiguration(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsWithRawResponse:
        return AccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsWithStreamingResponse:
        return AccountsWithStreamingResponse(self)

    def retrieve(
        self,
        account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountConfiguration:
        """
        Get account configuration such as spend limits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return self._get(
            f"/accounts/{account_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountConfiguration,
        )

    def update(
        self,
        account_token: str,
        *,
        daily_spend_limit: int | NotGiven = NOT_GIVEN,
        lifetime_spend_limit: int | NotGiven = NOT_GIVEN,
        monthly_spend_limit: int | NotGiven = NOT_GIVEN,
        state: Literal["ACTIVE", "PAUSED"] | NotGiven = NOT_GIVEN,
        verification_address: account_update_params.VerificationAddress | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountConfiguration:
        """Update account configuration such as spend limits and verification address.

        Can
        only be run on accounts that are part of the program managed by this API key.

        Accounts that are in the `PAUSED` state will not be able to transact or create
        new cards.

        Args:
          daily_spend_limit: Amount (in cents) for the account's daily spend limit. By default the daily
              spend limit is set to $1,250.

          lifetime_spend_limit: Amount (in cents) for the account's lifetime spend limit. Once this limit is
              reached, no transactions will be accepted on any card created for this account
              until the limit is updated. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the
              account limit. This behavior differs from the daily spend limit and the monthly
              spend limit.

          monthly_spend_limit: Amount (in cents) for the account's monthly spend limit. By default the monthly
              spend limit is set to $5,000.

          state: Account states.

          verification_address: Address used during Address Verification Service (AVS) checks during
              transactions if enabled via Auth Rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return self._patch(
            f"/accounts/{account_token}",
            body=maybe_transform(
                {
                    "daily_spend_limit": daily_spend_limit,
                    "lifetime_spend_limit": lifetime_spend_limit,
                    "monthly_spend_limit": monthly_spend_limit,
                    "state": state,
                    "verification_address": verification_address,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountConfiguration,
        )


class AsyncAccounts(AsyncAPIResource):
    @cached_property
    def credit_configuration(self) -> AsyncCreditConfiguration:
        return AsyncCreditConfiguration(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsWithRawResponse:
        return AsyncAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsWithStreamingResponse:
        return AsyncAccountsWithStreamingResponse(self)

    async def retrieve(
        self,
        account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountConfiguration:
        """
        Get account configuration such as spend limits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return await self._get(
            f"/accounts/{account_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountConfiguration,
        )

    async def update(
        self,
        account_token: str,
        *,
        daily_spend_limit: int | NotGiven = NOT_GIVEN,
        lifetime_spend_limit: int | NotGiven = NOT_GIVEN,
        monthly_spend_limit: int | NotGiven = NOT_GIVEN,
        state: Literal["ACTIVE", "PAUSED"] | NotGiven = NOT_GIVEN,
        verification_address: account_update_params.VerificationAddress | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountConfiguration:
        """Update account configuration such as spend limits and verification address.

        Can
        only be run on accounts that are part of the program managed by this API key.

        Accounts that are in the `PAUSED` state will not be able to transact or create
        new cards.

        Args:
          daily_spend_limit: Amount (in cents) for the account's daily spend limit. By default the daily
              spend limit is set to $1,250.

          lifetime_spend_limit: Amount (in cents) for the account's lifetime spend limit. Once this limit is
              reached, no transactions will be accepted on any card created for this account
              until the limit is updated. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the
              account limit. This behavior differs from the daily spend limit and the monthly
              spend limit.

          monthly_spend_limit: Amount (in cents) for the account's monthly spend limit. By default the monthly
              spend limit is set to $5,000.

          state: Account states.

          verification_address: Address used during Address Verification Service (AVS) checks during
              transactions if enabled via Auth Rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return await self._patch(
            f"/accounts/{account_token}",
            body=maybe_transform(
                {
                    "daily_spend_limit": daily_spend_limit,
                    "lifetime_spend_limit": lifetime_spend_limit,
                    "monthly_spend_limit": monthly_spend_limit,
                    "state": state,
                    "verification_address": verification_address,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountConfiguration,
        )


class AccountsWithRawResponse:
    def __init__(self, accounts: Accounts) -> None:
        self._accounts = accounts

        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            accounts.update,
        )

    @cached_property
    def credit_configuration(self) -> CreditConfigurationWithRawResponse:
        return CreditConfigurationWithRawResponse(self._accounts.credit_configuration)


class AsyncAccountsWithRawResponse:
    def __init__(self, accounts: AsyncAccounts) -> None:
        self._accounts = accounts

        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            accounts.update,
        )

    @cached_property
    def credit_configuration(self) -> AsyncCreditConfigurationWithRawResponse:
        return AsyncCreditConfigurationWithRawResponse(self._accounts.credit_configuration)


class AccountsWithStreamingResponse:
    def __init__(self, accounts: Accounts) -> None:
        self._accounts = accounts

        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            accounts.update,
        )

    @cached_property
    def credit_configuration(self) -> CreditConfigurationWithStreamingResponse:
        return CreditConfigurationWithStreamingResponse(self._accounts.credit_configuration)


class AsyncAccountsWithStreamingResponse:
    def __init__(self, accounts: AsyncAccounts) -> None:
        self._accounts = accounts

        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )

    @cached_property
    def credit_configuration(self) -> AsyncCreditConfigurationWithStreamingResponse:
        return AsyncCreditConfigurationWithStreamingResponse(self._accounts.credit_configuration)
