"""Stream type classes for tap-jiratempo."""

from __future__ import annotations

import typing as t
from importlib import resources

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_jiratempo.client import JiraTempoStream

SCHEMAS_DIR = resources.files(__package__) / "schemas"


class WorklogsStream(JiraTempoStream):
    """Define custom stream."""
    name = "worklogs"
    path = "/worklogs"
    primary_keys: t.ClassVar[list[str]] = ["tempoWorklogId"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "worklogs.json"  # noqa: ERA001


class AccountsStream(JiraTempoStream):
    """Define custom stream."""

    name = "accounts"
    path = "/accounts"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "accounts.json"