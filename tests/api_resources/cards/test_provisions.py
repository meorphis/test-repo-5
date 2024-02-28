# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_22 import MeorphisTest22, AsyncMeorphisTest22
from meorphis_test_22.types.cards import ProvisionPostProvisionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProvisions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_post_provision(self, client: MeorphisTest22) -> None:
        provision = client.cards.provisions.post_provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProvisionPostProvisionResponse, provision, path=["response"])

    @parametrize
    def test_method_post_provision_with_all_params(self, client: MeorphisTest22) -> None:
        provision = client.cards.provisions.post_provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            certificate="U3RhaW5sZXNzIHJvY2tz",
            digital_wallet="GOOGLE_PAY",
            nonce="U3RhaW5sZXNzIHJvY2tz",
            nonce_signature="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(ProvisionPostProvisionResponse, provision, path=["response"])

    @parametrize
    def test_raw_response_post_provision(self, client: MeorphisTest22) -> None:
        response = client.cards.provisions.with_raw_response.post_provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provision = response.parse()
        assert_matches_type(ProvisionPostProvisionResponse, provision, path=["response"])

    @parametrize
    def test_streaming_response_post_provision(self, client: MeorphisTest22) -> None:
        with client.cards.provisions.with_streaming_response.post_provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provision = response.parse()
            assert_matches_type(ProvisionPostProvisionResponse, provision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_post_provision(self, client: MeorphisTest22) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            client.cards.provisions.with_raw_response.post_provision(
                "",
            )


class TestAsyncProvisions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_post_provision(self, async_client: AsyncMeorphisTest22) -> None:
        provision = await async_client.cards.provisions.post_provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProvisionPostProvisionResponse, provision, path=["response"])

    @parametrize
    async def test_method_post_provision_with_all_params(self, async_client: AsyncMeorphisTest22) -> None:
        provision = await async_client.cards.provisions.post_provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            certificate="U3RhaW5sZXNzIHJvY2tz",
            digital_wallet="GOOGLE_PAY",
            nonce="U3RhaW5sZXNzIHJvY2tz",
            nonce_signature="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(ProvisionPostProvisionResponse, provision, path=["response"])

    @parametrize
    async def test_raw_response_post_provision(self, async_client: AsyncMeorphisTest22) -> None:
        response = await async_client.cards.provisions.with_raw_response.post_provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provision = await response.parse()
        assert_matches_type(ProvisionPostProvisionResponse, provision, path=["response"])

    @parametrize
    async def test_streaming_response_post_provision(self, async_client: AsyncMeorphisTest22) -> None:
        async with async_client.cards.provisions.with_streaming_response.post_provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provision = await response.parse()
            assert_matches_type(ProvisionPostProvisionResponse, provision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_post_provision(self, async_client: AsyncMeorphisTest22) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            await async_client.cards.provisions.with_raw_response.post_provision(
                "",
            )
