# This file was auto-generated by Fern from our API Definition.

from hume.client import AsyncHumeClient, HumeClient
from hume.custom_models import FileInput, FileWithAttributesInput

from ..utilities import validate_response


async def test_create_files(client: HumeClient, async_client: AsyncHumeClient) -> None:
    expected_response = [
        {
            "file": {
                "id": "id",
                "name": "name",
                "uri": "uri",
                "upload_uri": "upload_uri",
                "thumbnail_uri": "thumbnail_uri",
                "user_id": "user_id",
                "data_type": "data_type",
                "created_on": 1,
                "modified_on": 1,
                "metadata": {"metadata": {}},
                "hume_storage": True,
                "hume_storage_upload_timestamp": 1,
                "is_sanitized": True,
                "is_owned_by_reader": True,
                "is_linked_to_publicly_shared": True,
                "is_linked_to_hume_model": True,
            },
            "attributes": [{"name": "name", "value": "value"}],
        }
    ]
    expected_types = (
        "list",
        {
            0: {
                "file": {
                    "id": None,
                    "name": None,
                    "uri": None,
                    "upload_uri": None,
                    "thumbnail_uri": None,
                    "user_id": None,
                    "data_type": None,
                    "created_on": "integer",
                    "modified_on": "integer",
                    "metadata": ("dict", {0: (None, ("dict", {}))}),
                    "hume_storage": None,
                    "hume_storage_upload_timestamp": "integer",
                    "is_sanitized": None,
                    "is_owned_by_reader": None,
                    "is_linked_to_publicly_shared": None,
                    "is_linked_to_hume_model": None,
                },
                "attributes": ("list", {0: {"name": None, "value": None}}),
            }
        },
    )
    response = client.custom_models.files.create_files(
        request=[
            FileWithAttributesInput(
                file=FileInput(name="name", hume_storage=True, data_type="data_type")
            )
        ]
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.custom_models.files.create_files(
        request=[
            FileWithAttributesInput(
                file=FileInput(name="name", hume_storage=True, data_type="data_type")
            )
        ]
    )
    validate_response(async_response, expected_response, expected_types)


async def test_get_file(client: HumeClient, async_client: AsyncHumeClient) -> None:
    expected_response = {
        "file": {
            "id": "id",
            "name": "name",
            "uri": "uri",
            "upload_uri": "upload_uri",
            "thumbnail_uri": "thumbnail_uri",
            "user_id": "user_id",
            "data_type": "data_type",
            "created_on": 1,
            "modified_on": 1,
            "metadata": {"metadata": {}},
            "hume_storage": True,
            "hume_storage_upload_timestamp": 1,
            "is_sanitized": True,
            "is_owned_by_reader": True,
            "is_linked_to_publicly_shared": True,
            "is_linked_to_hume_model": True,
        },
        "attributes": [{"name": "name", "value": "value"}],
    }
    expected_types = {
        "file": {
            "id": None,
            "name": None,
            "uri": None,
            "upload_uri": None,
            "thumbnail_uri": None,
            "user_id": None,
            "data_type": None,
            "created_on": "integer",
            "modified_on": "integer",
            "metadata": ("dict", {0: (None, ("dict", {}))}),
            "hume_storage": None,
            "hume_storage_upload_timestamp": "integer",
            "is_sanitized": None,
            "is_owned_by_reader": None,
            "is_linked_to_publicly_shared": None,
            "is_linked_to_hume_model": None,
        },
        "attributes": ("list", {0: {"name": None, "value": None}}),
    }
    response = client.custom_models.files.get_file(id="id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.custom_models.files.get_file(id="id")
    validate_response(async_response, expected_response, expected_types)


async def test_delete_file(client: HumeClient, async_client: AsyncHumeClient) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.custom_models.files.delete_file(id="id") is None  # type: ignore[func-returns-value]

    assert await async_client.custom_models.files.delete_file(id="id") is None  # type: ignore[func-returns-value]


async def test_update_file_name(
    client: HumeClient, async_client: AsyncHumeClient
) -> None:
    expected_response = {
        "file": {
            "id": "id",
            "name": "name",
            "uri": "uri",
            "upload_uri": "upload_uri",
            "thumbnail_uri": "thumbnail_uri",
            "user_id": "user_id",
            "data_type": "data_type",
            "created_on": 1,
            "modified_on": 1,
            "metadata": {"metadata": {}},
            "hume_storage": True,
            "hume_storage_upload_timestamp": 1,
            "is_sanitized": True,
            "is_owned_by_reader": True,
            "is_linked_to_publicly_shared": True,
            "is_linked_to_hume_model": True,
        },
        "attributes": [{"name": "name", "value": "value"}],
    }
    expected_types = {
        "file": {
            "id": None,
            "name": None,
            "uri": None,
            "upload_uri": None,
            "thumbnail_uri": None,
            "user_id": None,
            "data_type": None,
            "created_on": "integer",
            "modified_on": "integer",
            "metadata": ("dict", {0: (None, ("dict", {}))}),
            "hume_storage": None,
            "hume_storage_upload_timestamp": "integer",
            "is_sanitized": None,
            "is_owned_by_reader": None,
            "is_linked_to_publicly_shared": None,
            "is_linked_to_hume_model": None,
        },
        "attributes": ("list", {0: {"name": None, "value": None}}),
    }
    response = client.custom_models.files.update_file_name(id="id", name="name")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.custom_models.files.update_file_name(
        id="id", name="name"
    )
    validate_response(async_response, expected_response, expected_types)


async def test_get_file_predictions(
    client: HumeClient, async_client: AsyncHumeClient
) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.custom_models.files.get_file_predictions(id="id") is None  # type: ignore[func-returns-value]

    assert await async_client.custom_models.files.get_file_predictions(id="id") is None  # type: ignore[func-returns-value]
