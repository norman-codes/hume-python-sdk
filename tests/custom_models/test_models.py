# This file was auto-generated by Fern from our API Definition.

import pytest
from hume.client import AsyncHumeClient, HumeClient

from ..utilities import validate_response


async def test_get_model_details(client: HumeClient, async_client: AsyncHumeClient) -> None:
    expected_response = {
        "id": "id",
        "name": "name",
        "created_on": 1,
        "modified_on": 1,
        "total_stars": 1,
        "model_is_starred_by_user": True,
        "archived": True,
        "latest_version": {
            "id": "id",
            "model_id": "model_id",
            "user_id": "user_id",
            "version": "version",
            "source_uri": "source_uri",
            "dataset_version_id": "dataset_version_id",
            "created_on": 1,
            "metadata": {"metadata": {}},
            "description": "description",
            "tags": [{"key": "key", "value": "value"}],
            "file_type": "video",
            "target_feature": "target_feature",
            "task_type": "task_type",
            "training_job_id": "training_job_id",
        },
        "is_publicly_shared": True,
    }
    expected_types = {
        "id": None,
        "name": None,
        "created_on": "integer",
        "modified_on": "integer",
        "total_stars": "integer",
        "model_is_starred_by_user": None,
        "archived": None,
        "latest_version": {
            "id": None,
            "model_id": None,
            "user_id": None,
            "version": None,
            "source_uri": None,
            "dataset_version_id": None,
            "created_on": "integer",
            "metadata": ("dict", {0: (None, ("dict", {}))}),
            "description": None,
            "tags": ("list", {0: {"key": None, "value": None}}),
            "file_type": None,
            "target_feature": None,
            "task_type": None,
            "training_job_id": None,
        },
        "is_publicly_shared": None,
    }
    response = client.custom_models.models.get_model_details(id="id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.custom_models.models.get_model_details(id="id")
    validate_response(async_response, expected_response, expected_types)


async def test_update_model_name(client: HumeClient, async_client: AsyncHumeClient) -> None:
    expected_response = {
        "id": "id",
        "name": "name",
        "created_on": 1,
        "modified_on": 1,
        "total_stars": 1,
        "model_is_starred_by_user": True,
        "archived": True,
        "latest_version": {
            "id": "id",
            "model_id": "model_id",
            "user_id": "user_id",
            "version": "version",
            "source_uri": "source_uri",
            "dataset_version_id": "dataset_version_id",
            "created_on": 1,
            "metadata": {"metadata": {}},
            "description": "description",
            "tags": [{"key": "key", "value": "value"}],
            "file_type": "video",
            "target_feature": "target_feature",
            "task_type": "task_type",
            "training_job_id": "training_job_id",
        },
        "is_publicly_shared": True,
    }
    expected_types = {
        "id": None,
        "name": None,
        "created_on": "integer",
        "modified_on": "integer",
        "total_stars": "integer",
        "model_is_starred_by_user": None,
        "archived": None,
        "latest_version": {
            "id": None,
            "model_id": None,
            "user_id": None,
            "version": None,
            "source_uri": None,
            "dataset_version_id": None,
            "created_on": "integer",
            "metadata": ("dict", {0: (None, ("dict", {}))}),
            "description": None,
            "tags": ("list", {0: {"key": None, "value": None}}),
            "file_type": None,
            "target_feature": None,
            "task_type": None,
            "training_job_id": None,
        },
        "is_publicly_shared": None,
    }
    response = client.custom_models.models.update_model_name(id="id", name="name")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.custom_models.models.update_model_name(id="id", name="name")
    validate_response(async_response, expected_response, expected_types)

async def test_list_model_versions(client: HumeClient, async_client: AsyncHumeClient) -> None:
    expected_response = [
        {
            "id": "id",
            "model_id": "model_id",
            "user_id": "user_id",
            "version": "version",
            "source_uri": "source_uri",
            "dataset_version_id": "dataset_version_id",
            "created_on": 1,
            "metadata": {"metadata": {}},
            "description": "description",
            "tags": [{"key": "key", "value": "value"}],
            "file_type": "video",
            "target_feature": "target_feature",
            "task_type": "task_type",
            "training_job_id": "training_job_id",
        }
    ]
    expected_types = (
        "list",
        {
            0: {
                "id": None,
                "model_id": None,
                "user_id": None,
                "version": None,
                "source_uri": None,
                "dataset_version_id": None,
                "created_on": "integer",
                "metadata": ("dict", {0: (None, ("dict", {}))}),
                "description": None,
                "tags": ("list", {0: {"key": None, "value": None}}),
                "file_type": None,
                "target_feature": None,
                "task_type": None,
                "training_job_id": None,
            }
        },
    )
    response = client.custom_models.models.list_model_versions()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.custom_models.models.list_model_versions()
    validate_response(async_response, expected_response, expected_types)


async def test_get_model_version(client: HumeClient, async_client: AsyncHumeClient) -> None:
    expected_response = {
        "id": "id",
        "model_id": "model_id",
        "user_id": "user_id",
        "version": "version",
        "source_uri": "source_uri",
        "dataset_version_id": "dataset_version_id",
        "created_on": 1,
        "metadata": {"metadata": {"metadata": {"key": "value"}}},
        "description": "description",
        "tags": [{"key": "key", "value": "value"}],
        "file_type": "video",
        "target_feature": "target_feature",
        "task_type": "task_type",
        "training_job_id": "training_job_id",
    }
    expected_types = {
        "id": None,
        "model_id": None,
        "user_id": None,
        "version": None,
        "source_uri": None,
        "dataset_version_id": None,
        "created_on": "integer",
        "metadata": ("dict", {0: (None, ("dict", {0: (None, None)}))}),
        "description": None,
        "tags": ("list", {0: {"key": None, "value": None}}),
        "file_type": None,
        "target_feature": None,
        "task_type": None,
        "training_job_id": None,
    }
    response = client.custom_models.models.get_model_version(id="id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.custom_models.models.get_model_version(id="id")
    validate_response(async_response, expected_response, expected_types)


async def test_update_model_description(client: HumeClient, async_client: AsyncHumeClient) -> None:
    expected_response = {
        "id": "id",
        "model_id": "model_id",
        "user_id": "user_id",
        "version": "version",
        "source_uri": "source_uri",
        "dataset_version_id": "dataset_version_id",
        "created_on": 1,
        "metadata": {"metadata": {"metadata": {"key": "value"}}},
        "description": "description",
        "tags": [{"key": "key", "value": "value"}],
        "file_type": "video",
        "target_feature": "target_feature",
        "task_type": "task_type",
        "training_job_id": "training_job_id",
    }
    expected_types = {
        "id": None,
        "model_id": None,
        "user_id": None,
        "version": None,
        "source_uri": None,
        "dataset_version_id": None,
        "created_on": "integer",
        "metadata": ("dict", {0: (None, ("dict", {0: (None, None)}))}),
        "description": None,
        "tags": ("list", {0: {"key": None, "value": None}}),
        "file_type": None,
        "target_feature": None,
        "task_type": None,
        "training_job_id": None,
    }
    response = client.custom_models.models.update_model_description(id="id", request="string")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.custom_models.models.update_model_description(id="id", request="string")
    validate_response(async_response, expected_response, expected_types)
