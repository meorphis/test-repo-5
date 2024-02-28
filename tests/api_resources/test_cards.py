# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_22 import MeorphisTest22, AsyncMeorphisTest22
from meorphis_test_22.types import (
    Card,
    CardProvisionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MeorphisTest22) -> None:
        card = client.cards.create(
            type="VIRTUAL",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MeorphisTest22) -> None:
        card = client.cards.create(
            type="VIRTUAL",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_program_token="00000000-0000-0000-1000-000000000000",
            carrier={"qr_code_url": "string"},
            digital_card_art_token="00000000-0000-0000-1000-000000000000",
            exp_month="06",
            exp_year="2027",
            memo="New Card",
            pin="string",
            product_id="1",
            shipping_address={
                "first_name": "Michael",
                "last_name": "Bluth",
                "line2_text": "The Bluth Company",
                "address1": "5 Broad Street",
                "address2": "Unit 25A",
                "city": "NEW YORK",
                "state": "NY",
                "postal_code": "10001-1809",
                "country": "USA",
                "email": "johnny@appleseed.com",
                "phone_number": "+12124007676",
            },
            shipping_method="STANDARD",
            spend_limit=1000,
            spend_limit_duration="TRANSACTION",
            state="OPEN",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MeorphisTest22) -> None:
        response = client.cards.with_raw_response.create(
            type="VIRTUAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MeorphisTest22) -> None:
        with client.cards.with_streaming_response.create(
            type="VIRTUAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: MeorphisTest22) -> None:
        card = client.cards.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MeorphisTest22) -> None:
        response = client.cards.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MeorphisTest22) -> None:
        with client.cards.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MeorphisTest22) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            client.cards.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: MeorphisTest22) -> None:
        card = client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: MeorphisTest22) -> None:
        card = client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auth_rule_token="string",
            digital_card_art_token="00000000-0000-0000-1000-000000000000",
            memo="Updated Name",
            pin="string",
            spend_limit=100,
            spend_limit_duration="FOREVER",
            state="OPEN",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: MeorphisTest22) -> None:
        response = client.cards.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: MeorphisTest22) -> None:
        with client.cards.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: MeorphisTest22) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            client.cards.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_provision(self, client: MeorphisTest22) -> None:
        card = client.cards.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardProvisionResponse, card, path=["response"])

    @parametrize
    def test_method_provision_with_all_params(self, client: MeorphisTest22) -> None:
        card = client.cards.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            certificate="U3RhaW5sZXNzIHJvY2tz",
            digital_wallet="GOOGLE_PAY",
            nonce="U3RhaW5sZXNzIHJvY2tz",
            nonce_signature="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(CardProvisionResponse, card, path=["response"])

    @parametrize
    def test_raw_response_provision(self, client: MeorphisTest22) -> None:
        response = client.cards.with_raw_response.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardProvisionResponse, card, path=["response"])

    @parametrize
    def test_streaming_response_provision(self, client: MeorphisTest22) -> None:
        with client.cards.with_streaming_response.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardProvisionResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_provision(self, client: MeorphisTest22) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            client.cards.with_raw_response.provision(
                "",
            )


class TestAsyncCards:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMeorphisTest22) -> None:
        card = await async_client.cards.create(
            type="VIRTUAL",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMeorphisTest22) -> None:
        card = await async_client.cards.create(
            type="VIRTUAL",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_program_token="00000000-0000-0000-1000-000000000000",
            carrier={"qr_code_url": "string"},
            digital_card_art_token="00000000-0000-0000-1000-000000000000",
            exp_month="06",
            exp_year="2027",
            memo="New Card",
            pin="string",
            product_id="1",
            shipping_address={
                "first_name": "Michael",
                "last_name": "Bluth",
                "line2_text": "The Bluth Company",
                "address1": "5 Broad Street",
                "address2": "Unit 25A",
                "city": "NEW YORK",
                "state": "NY",
                "postal_code": "10001-1809",
                "country": "USA",
                "email": "johnny@appleseed.com",
                "phone_number": "+12124007676",
            },
            shipping_method="STANDARD",
            spend_limit=1000,
            spend_limit_duration="TRANSACTION",
            state="OPEN",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMeorphisTest22) -> None:
        response = await async_client.cards.with_raw_response.create(
            type="VIRTUAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMeorphisTest22) -> None:
        async with async_client.cards.with_streaming_response.create(
            type="VIRTUAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMeorphisTest22) -> None:
        card = await async_client.cards.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMeorphisTest22) -> None:
        response = await async_client.cards.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMeorphisTest22) -> None:
        async with async_client.cards.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMeorphisTest22) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            await async_client.cards.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMeorphisTest22) -> None:
        card = await async_client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMeorphisTest22) -> None:
        card = await async_client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auth_rule_token="string",
            digital_card_art_token="00000000-0000-0000-1000-000000000000",
            memo="Updated Name",
            pin="string",
            spend_limit=100,
            spend_limit_duration="FOREVER",
            state="OPEN",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMeorphisTest22) -> None:
        response = await async_client.cards.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMeorphisTest22) -> None:
        async with async_client.cards.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMeorphisTest22) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            await async_client.cards.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_provision(self, async_client: AsyncMeorphisTest22) -> None:
        card = await async_client.cards.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardProvisionResponse, card, path=["response"])

    @parametrize
    async def test_method_provision_with_all_params(self, async_client: AsyncMeorphisTest22) -> None:
        card = await async_client.cards.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            certificate="U3RhaW5sZXNzIHJvY2tz",
            digital_wallet="GOOGLE_PAY",
            nonce="U3RhaW5sZXNzIHJvY2tz",
            nonce_signature="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(CardProvisionResponse, card, path=["response"])

    @parametrize
    async def test_raw_response_provision(self, async_client: AsyncMeorphisTest22) -> None:
        response = await async_client.cards.with_raw_response.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardProvisionResponse, card, path=["response"])

    @parametrize
    async def test_streaming_response_provision(self, async_client: AsyncMeorphisTest22) -> None:
        async with async_client.cards.with_streaming_response.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardProvisionResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_provision(self, async_client: AsyncMeorphisTest22) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            await async_client.cards.with_raw_response.provision(
                "",
            )
