"""JiraTempo entry point."""

from __future__ import annotations

from tap_jiratempo.tap import TapJiraTempo

TapJiraTempo.cli()
