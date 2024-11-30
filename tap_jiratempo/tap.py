"""JiraTempo tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_jiratempo import streams


class TapJiraTempo(Tap):
    """JiraTempo tap class."""

    name = "tap-jiratempo"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            default = "Bearer uHjigKWHYjSV4idYNDGdpbOcYIpt06-us",
            title="Auth Token",
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "api_url",
            th.StringType,
            title="API URL",
            default="https://api.tempo.io/4",
            description="The url for the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.JiraTempoStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.WorklogsStream(self),
            streams.AccountsStream(self),
        ]


if __name__ == "__main__":
    TapJiraTempo.cli()
