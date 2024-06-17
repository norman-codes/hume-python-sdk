"""Sender for streaming audio from a microphone."""

import json
import logging
from dataclasses import dataclass
from typing import Protocol

from hume._voice.microphone.microphone import Microphone
from hume._voice.voice_socket import VoiceSocket

logger = logging.getLogger(__name__)


class Sender(Protocol):
    """Protocol for sending streaming audio to an EVI connection."""

    async def send(self, *, socket: VoiceSocket) -> None:
        """Send audio data over an EVI socket.

        Args:
            socket (VoiceSocket): EVI socket.
        """
        raise NotImplementedError()

    async def send_tool_response(self, *, socket: VoiceSocket, tool_call_id: str, content: str) -> None:
        """Send a tool response over an EVI socket.

        Args:
            socket (VoiceSocket): EVI socket.
            tool_call_id (str): Tool call ID.
            content (str): Tool response content.
        """
        raise NotImplementedError()


@dataclass
class MicrophoneSender(Sender):
    """Sender for streaming audio from a microphone."""

    microphone: Microphone
    send_audio: bool

    @classmethod
    def new(cls, *, microphone: Microphone) -> "MicrophoneSender":
        """Create a new microphone sender.

        Args:
            microphone (Microphone): Microphone instance.
        """
        return cls(microphone=microphone, send_audio=True)

    async def send(self, *, socket: VoiceSocket) -> None:
        """Send audio data over an EVI socket.

        Args:
            socket (VoiceSocket): EVI socket.
        """
        async for byte_str in self.microphone:
            if self.send_audio:
                await socket.send(byte_str)

    async def send_tool_response(self, *, socket: VoiceSocket, tool_call_id: str, content: str) -> None:
        """Send a tool response over an EVI socket.

        Args:
            socket (VoiceSocket): EVI socket.
            tool_call_id (str): Tool call ID.
            content (str): Tool response content.
        """
        response_message = {
            "type": "tool_response",
            "tool_call_id": tool_call_id,
            "content": content,
        }
        await socket.send(json.dumps(response_message).encode("utf-8"))
