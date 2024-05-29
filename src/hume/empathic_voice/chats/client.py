# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.query_encoder import encode_query
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ..types.return_chat_paged_events import ReturnChatPagedEvents
from ..types.return_paged_chats import ReturnPagedChats


class ChatsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_chats(
        self,
        *,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReturnPagedChats:
        """
        Parameters
        ----------
        page_number : typing.Optional[int]
            The page number of the results to return.

        page_size : typing.Optional[int]
            The maximum number of results to include per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReturnPagedChats
            Success

        Examples
        --------
        from hume.client import HumeClient

        client = HumeClient(
            api_key="YOUR_API_KEY",
        )
        client.empathic_voice.chats.list_chats()
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v0/evi/chats"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "page_number": page_number,
                            "page_size": page_size,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
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
            return pydantic_v1.parse_obj_as(ReturnPagedChats, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_chat_events(
        self,
        id: str,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReturnChatPagedEvents:
        """
        Parameters
        ----------
        id : str
            Identifier for a chat. Formatted as a UUID.

        page_size : typing.Optional[int]
            The maximum number of results to include per page.

        page_number : typing.Optional[int]
            The page number of the results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReturnChatPagedEvents
            Success

        Examples
        --------
        from hume.client import HumeClient

        client = HumeClient(
            api_key="YOUR_API_KEY",
        )
        client.empathic_voice.chats.list_chat_events(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v0/evi/chats/{jsonable_encoder(id)}"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "page_size": page_size,
                            "page_number": page_number,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
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
            return pydantic_v1.parse_obj_as(ReturnChatPagedEvents, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncChatsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_chats(
        self,
        *,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReturnPagedChats:
        """
        Parameters
        ----------
        page_number : typing.Optional[int]
            The page number of the results to return.

        page_size : typing.Optional[int]
            The maximum number of results to include per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReturnPagedChats
            Success

        Examples
        --------
        from hume.client import AsyncHumeClient

        client = AsyncHumeClient(
            api_key="YOUR_API_KEY",
        )
        await client.empathic_voice.chats.list_chats()
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v0/evi/chats"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "page_number": page_number,
                            "page_size": page_size,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
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
            return pydantic_v1.parse_obj_as(ReturnPagedChats, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_chat_events(
        self,
        id: str,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReturnChatPagedEvents:
        """
        Parameters
        ----------
        id : str
            Identifier for a chat. Formatted as a UUID.

        page_size : typing.Optional[int]
            The maximum number of results to include per page.

        page_number : typing.Optional[int]
            The page number of the results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReturnChatPagedEvents
            Success

        Examples
        --------
        from hume.client import AsyncHumeClient

        client = AsyncHumeClient(
            api_key="YOUR_API_KEY",
        )
        await client.empathic_voice.chats.list_chat_events(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v0/evi/chats/{jsonable_encoder(id)}"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "page_size": page_size,
                            "page_number": page_number,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
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
            return pydantic_v1.parse_obj_as(ReturnChatPagedEvents, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
