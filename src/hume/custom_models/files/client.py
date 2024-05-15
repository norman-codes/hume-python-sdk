# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ... import core
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ..types.file_page import FilePage
from ..types.file_with_attributes import FileWithAttributes
from ..types.file_with_attributes_input import FileWithAttributesInput

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class FilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_files(
        self,
        *,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        shared_assets: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilePage:
        """
        Returns 200 if successful

        Parameters
        ----------
        page_number : typing.Optional[int]
            Index of the first result

        page_size : typing.Optional[int]
            Maximum number of results

        shared_assets : typing.Optional[bool]
            `True` Will show all assets owned by you and shared with you. `False` Will show only your assets. Default: `False`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilePage
            Success

        Examples
        --------
        from hume.client import HumeClient

        client = HumeClient(
            api_key="YOUR_API_KEY",
        )
        client.custom_models.files.list_files()
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "files"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "shared_assets": shared_assets,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FilePage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_files(
        self,
        *,
        request: typing.Sequence[FileWithAttributesInput],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FileWithAttributes]:
        """
        Returns 201 if successful

        Parameters
        ----------
        request : typing.Sequence[FileWithAttributesInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FileWithAttributes]
            Success

        Examples
        --------
        from hume.client import HumeClient
        from hume.custom_models import FileInput, FileWithAttributesInput

        client = HumeClient(
            api_key="YOUR_API_KEY",
        )
        client.custom_models.files.create_files(
            request=[
                FileWithAttributesInput(
                    file=FileInput(
                        name="name",
                        hume_storage=True,
                        data_type="data_type",
                    ),
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "files"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[FileWithAttributes], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def upload_file(
        self,
        *,
        file: core.File,
        attributes: typing.Optional[core.File] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileWithAttributes:
        """
        Upload a file synchronously. Returns 201 if successful. Files must have a name. Files must specify Content-Type. Request bodies, and therefore files, are limited to 100MB

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        attributes : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileWithAttributes
            Success

        Examples
        --------
        from hume.client import HumeClient

        client = HumeClient(
            api_key="YOUR_API_KEY",
        )
        client.custom_models.files.upload_file()
        """
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "files/upload"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            data=jsonable_encoder(remove_none_from_dict({}))
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(remove_none_from_dict({})),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            files=core.convert_file_dict_to_httpx_tuples(
                remove_none_from_dict({"file": file, "attributes": attributes})
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FileWithAttributes, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_file(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> FileWithAttributes:
        """
        Returns 200 if successful

        Parameters
        ----------
        id : str
            Hume-generated ID of a File

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileWithAttributes
            Success

        Examples
        --------
        from hume.client import HumeClient

        client = HumeClient(
            api_key="YOUR_API_KEY",
        )
        client.custom_models.files.get_file(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FileWithAttributes, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_file(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns 204 if successful

        Parameters
        ----------
        id : str
            Hume-generated ID of a File

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from hume.client import HumeClient

        client = HumeClient(
            api_key="YOUR_API_KEY",
        )
        client.custom_models.files.delete_file(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_file_name(
        self, id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FileWithAttributes:
        """
        Returns 200 if successful

        Parameters
        ----------
        id : str
            Hume-generated ID of a File

        name : str
            New File name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileWithAttributes
            Success

        Examples
        --------
        from hume.client import HumeClient

        client = HumeClient(
            api_key="YOUR_API_KEY",
        )
        client.custom_models.files.update_file_name(
            id="id",
            name="name",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="PATCH",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "name": name,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FileWithAttributes, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_file_predictions(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns 200 if successful

        Parameters
        ----------
        id : str
            Hume-generated ID of a File

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from hume.client import HumeClient

        client = HumeClient(
            api_key="YOUR_API_KEY",
        )
        client.custom_models.files.get_file_predictions(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(id)}/predictions"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_files(
        self,
        *,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        shared_assets: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilePage:
        """
        Returns 200 if successful

        Parameters
        ----------
        page_number : typing.Optional[int]
            Index of the first result

        page_size : typing.Optional[int]
            Maximum number of results

        shared_assets : typing.Optional[bool]
            `True` Will show all assets owned by you and shared with you. `False` Will show only your assets. Default: `False`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilePage
            Success

        Examples
        --------
        from hume.client import AsyncHumeClient

        client = AsyncHumeClient(
            api_key="YOUR_API_KEY",
        )
        await client.custom_models.files.list_files()
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "files"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "shared_assets": shared_assets,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FilePage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_files(
        self,
        *,
        request: typing.Sequence[FileWithAttributesInput],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FileWithAttributes]:
        """
        Returns 201 if successful

        Parameters
        ----------
        request : typing.Sequence[FileWithAttributesInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FileWithAttributes]
            Success

        Examples
        --------
        from hume.client import AsyncHumeClient
        from hume.custom_models import FileInput, FileWithAttributesInput

        client = AsyncHumeClient(
            api_key="YOUR_API_KEY",
        )
        await client.custom_models.files.create_files(
            request=[
                FileWithAttributesInput(
                    file=FileInput(
                        name="name",
                        hume_storage=True,
                        data_type="data_type",
                    ),
                )
            ],
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "files"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[FileWithAttributes], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def upload_file(
        self,
        *,
        file: core.File,
        attributes: typing.Optional[core.File] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileWithAttributes:
        """
        Upload a file synchronously. Returns 201 if successful. Files must have a name. Files must specify Content-Type. Request bodies, and therefore files, are limited to 100MB

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        attributes : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileWithAttributes
            Success

        Examples
        --------
        from hume.client import AsyncHumeClient

        client = AsyncHumeClient(
            api_key="YOUR_API_KEY",
        )
        await client.custom_models.files.upload_file()
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "files/upload"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            data=jsonable_encoder(remove_none_from_dict({}))
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(remove_none_from_dict({})),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            files=core.convert_file_dict_to_httpx_tuples(
                remove_none_from_dict({"file": file, "attributes": attributes})
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FileWithAttributes, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_file(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> FileWithAttributes:
        """
        Returns 200 if successful

        Parameters
        ----------
        id : str
            Hume-generated ID of a File

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileWithAttributes
            Success

        Examples
        --------
        from hume.client import AsyncHumeClient

        client = AsyncHumeClient(
            api_key="YOUR_API_KEY",
        )
        await client.custom_models.files.get_file(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FileWithAttributes, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_file(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns 204 if successful

        Parameters
        ----------
        id : str
            Hume-generated ID of a File

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from hume.client import AsyncHumeClient

        client = AsyncHumeClient(
            api_key="YOUR_API_KEY",
        )
        await client.custom_models.files.delete_file(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_file_name(
        self, id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FileWithAttributes:
        """
        Returns 200 if successful

        Parameters
        ----------
        id : str
            Hume-generated ID of a File

        name : str
            New File name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileWithAttributes
            Success

        Examples
        --------
        from hume.client import AsyncHumeClient

        client = AsyncHumeClient(
            api_key="YOUR_API_KEY",
        )
        await client.custom_models.files.update_file_name(
            id="id",
            name="name",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="PATCH",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "name": name,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FileWithAttributes, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_file_predictions(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns 200 if successful

        Parameters
        ----------
        id : str
            Hume-generated ID of a File

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from hume.client import AsyncHumeClient

        client = AsyncHumeClient(
            api_key="YOUR_API_KEY",
        )
        await client.custom_models.files.get_file_predictions(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"files/{jsonable_encoder(id)}/predictions"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)