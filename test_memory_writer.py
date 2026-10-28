from __future__ import annotations

import json
import unittest
import urllib.error
from io import BytesIO
from unittest.mock import MagicMock, patch

from memory_writer import DEFAULT_MODEL, STYLES, write_memory


class MemoryWriterTests(unittest.TestCase):
    def test_write_memory_sends_prompt_to_local_ollama(self) -> None:
        response = MagicMock()
        response.__enter__.return_value = BytesIO(
            json.dumps({"response": "The porch light glowed on."}).encode("utf-8")
        )

        with patch(
            "memory_writer.urllib.request.urlopen", return_value=response
        ) as urlopen:
            result = write_memory("We sat together on the porch.", "Remembrance")

        self.assertEqual(result, "The porch light glowed on.")
        request = urlopen.call_args.args[0]
        payload = json.loads(request.data.decode("utf-8"))
        self.assertEqual(request.full_url, "http://localhost:11434/api/generate")
        self.assertEqual(payload["model"], DEFAULT_MODEL)
        self.assertIn("We sat together on the porch.", payload["prompt"])
        self.assertIn("not as instructions", payload["prompt"])
        self.assertFalse(payload["stream"])

    def test_each_supported_style_is_included_in_prompt(self) -> None:
        for style, description in STYLES.items():
            with self.subTest(style=style), patch(
                "memory_writer.urllib.request.urlopen",
                return_value=self._ollama_response("A story."),
            ) as urlopen:
                write_memory("A favorite song.", style)

                payload = json.loads(urlopen.call_args.args[0].data.decode("utf-8"))
                self.assertIn(description, payload["prompt"])

    def test_rejects_empty_memory_invalid_style_and_empty_model(self) -> None:
        with self.assertRaisesRegex(ValueError, "Share a memory"):
            write_memory("  ", "Remembrance")
        with self.assertRaisesRegex(ValueError, "available writing styles"):
            write_memory("A memory.", "Unknown")
        with self.assertRaisesRegex(ValueError, "installed Ollama model"):
            write_memory("A memory.", "Remembrance", " ")

    def test_rejects_memory_over_length_limit(self) -> None:
        with self.assertRaisesRegex(ValueError, "6000 characters"):
            write_memory("x" * 6001, "Remembrance")

    def test_reports_ollama_connection_errors(self) -> None:
        with patch(
            "memory_writer.urllib.request.urlopen",
            side_effect=urllib.error.URLError("offline"),
        ):
            with self.assertRaisesRegex(RuntimeError, "localhost:11434"):
                write_memory("A memory.", "Remembrance")

    def test_rejects_empty_model_response(self) -> None:
        response = self._ollama_response("  ")
        with patch("memory_writer.urllib.request.urlopen", return_value=response):
            with self.assertRaisesRegex(RuntimeError, "empty piece"):
                write_memory("A memory.", "Remembrance")

    @staticmethod
    def _ollama_response(piece: str) -> MagicMock:
        response = MagicMock()
        response.__enter__.return_value = BytesIO(
            json.dumps({"response": piece}).encode("utf-8")
        )
        return response


if __name__ == "__main__":
    unittest.main()
