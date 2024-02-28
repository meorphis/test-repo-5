# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_22 import MeorphisTest22, AsyncMeorphisTest22
from meorphis_test_22.types.accounts import BusinessAccount

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreditConfiguration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: MeorphisTest22) -> None:
        credit_configuration = client.accounts.credit_configuration.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MeorphisTest22) -> None:
        response = client.accounts.credit_configuration.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_configuration = response.parse()
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MeorphisTest22) -> None:
        with client.accounts.credit_configuration.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_configuration = response.parse()
            assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MeorphisTest22) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_token` but received ''"):
            client.accounts.credit_configuration.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: MeorphisTest22) -> None:
        credit_configuration = client.accounts.credit_configuration.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: MeorphisTest22) -> None:
        credit_configuration = client.accounts.credit_configuration.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            billing_period=0,
            credit_limit=0,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_period=0,
        )
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: MeorphisTest22) -> None:
        response = client.accounts.credit_configuration.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_configuration = response.parse()
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: MeorphisTest22) -> None:
        with client.accounts.credit_configuration.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_configuration = response.parse()
            assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: MeorphisTest22) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_token` but received ''"):
            client.accounts.credit_configuration.with_raw_response.update(
                "",
            )


class TestAsyncCreditConfiguration:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMeorphisTest22) -> None:
        credit_configuration = await async_client.accounts.credit_configuration.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMeorphisTest22) -> None:
        response = await async_client.accounts.credit_configuration.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_configuration = await response.parse()
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMeorphisTest22) -> None:
        async with async_client.accounts.credit_configuration.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_configuration = await response.parse()
            assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMeorphisTest22) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_token` but received ''"):
            await async_client.accounts.credit_configuration.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMeorphisTest22) -> None:
        credit_configuration = await async_client.accounts.credit_configuration.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMeorphisTest22) -> None:
        credit_configuration = await async_client.accounts.credit_configuration.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            billing_period=0,
            credit_limit=0,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_period=0,
        )
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMeorphisTest22) -> None:
        response = await async_client.accounts.credit_configuration.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_configuration = await response.parse()
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMeorphisTest22) -> None:
        async with async_client.accounts.credit_configuration.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_configuration = await response.parse()
            assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMeorphisTest22) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_token` but received ''"):
            await async_client.accounts.credit_configuration.with_raw_response.update(
                "",
            )
