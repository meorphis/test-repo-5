# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_22 import MeorphisTest22, AsyncMeorphisTest22
from meorphis_test_22.types import StatusGetStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatuses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_status(self, client: MeorphisTest22) -> None:
        status = client.statuses.get_status()
        assert_matches_type(StatusGetStatusResponse, status, path=["response"])

    @parametrize
    def test_raw_response_get_status(self, client: MeorphisTest22) -> None:
        response = client.statuses.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(StatusGetStatusResponse, status, path=["response"])

    @parametrize
    def test_streaming_response_get_status(self, client: MeorphisTest22) -> None:
        with client.statuses.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(StatusGetStatusResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStatuses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_status(self, async_client: AsyncMeorphisTest22) -> None:
        status = await async_client.statuses.get_status()
        assert_matches_type(StatusGetStatusResponse, status, path=["response"])

    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncMeorphisTest22) -> None:
        response = await async_client.statuses.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(StatusGetStatusResponse, status, path=["response"])

    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncMeorphisTest22) -> None:
        async with async_client.statuses.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(StatusGetStatusResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True
