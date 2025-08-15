
from attrs import frozen, field
from pgsn import helpers


@frozen
class DebugInfo:
    source: str = field(validator=helpers.not_none)
    location: int = field(validator=helpers.not_none)
