# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cards import FinancialTransaction
from ..._base_client import (
    make_request_options,
)

__all__ = ["FinancialTransactions", "AsyncFinancialTransactions"]


class FinancialTransactions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FinancialTransactionsWithRawResponse:
        return FinancialTransactionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FinancialTransactionsWithStreamingResponse:
        return FinancialTransactionsWithStreamingResponse(self)

    def retrieve(
        self,
        financial_transaction_token: str,
        *,
        card_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialTransaction:
        """
        Get the card financial transaction for the provided token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        if not financial_transaction_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_transaction_token` but received {financial_transaction_token!r}"
            )
        return self._get(
            f"/cards/{card_token}/financial_transactions/{financial_transaction_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialTransaction,
        )


class AsyncFinancialTransactions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFinancialTransactionsWithRawResponse:
        return AsyncFinancialTransactionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFinancialTransactionsWithStreamingResponse:
        return AsyncFinancialTransactionsWithStreamingResponse(self)

    async def retrieve(
        self,
        financial_transaction_token: str,
        *,
        card_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialTransaction:
        """
        Get the card financial transaction for the provided token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        if not financial_transaction_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_transaction_token` but received {financial_transaction_token!r}"
            )
        return await self._get(
            f"/cards/{card_token}/financial_transactions/{financial_transaction_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialTransaction,
        )


class FinancialTransactionsWithRawResponse:
    def __init__(self, financial_transactions: FinancialTransactions) -> None:
        self._financial_transactions = financial_transactions

        self.retrieve = to_raw_response_wrapper(
            financial_transactions.retrieve,
        )


class AsyncFinancialTransactionsWithRawResponse:
    def __init__(self, financial_transactions: AsyncFinancialTransactions) -> None:
        self._financial_transactions = financial_transactions

        self.retrieve = async_to_raw_response_wrapper(
            financial_transactions.retrieve,
        )


class FinancialTransactionsWithStreamingResponse:
    def __init__(self, financial_transactions: FinancialTransactions) -> None:
        self._financial_transactions = financial_transactions

        self.retrieve = to_streamed_response_wrapper(
            financial_transactions.retrieve,
        )


class AsyncFinancialTransactionsWithStreamingResponse:
    def __init__(self, financial_transactions: AsyncFinancialTransactions) -> None:
        self._financial_transactions = financial_transactions

        self.retrieve = async_to_streamed_response_wrapper(
            financial_transactions.retrieve,
        )
