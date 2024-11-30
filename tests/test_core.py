"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_tap_test_class

from tap_jiratempo.tap import TapJiraTempo

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    # TODO: Initialize minimal tap config
}


# Run standard built-in tap tests from the SDK:
TestTapJiraTempo = get_tap_test_class(
    tap_class=TapJiraTempo,
    config=SAMPLE_CONFIG,
)


# TODO: Create additional tests as appropriate for your tap.
