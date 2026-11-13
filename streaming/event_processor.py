from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from heapq import heappush, heappop
from typing import Dict, Set, Deque, List, Tuple

@dataclass(frozen=True)
class Event:
    event_id: str
    customer_id: str
    event_type: str
    ts_epoch: int
    amount: float = 0.0

class EventProcessor:
    """Demonstrates practical OOP + data structures for streaming systems."""
    def __init__(self) -> None:
        self.seen: Set[str] = set()                     # deduplication
        self.state: Dict[str, str] = {}                # event -> status
        self.window: Deque[Event] = deque(maxlen=1000) # rolling window
        self.priority: List[Tuple[float, int, Event]] = []

    def process(self, event: Event) -> bool:
        if event.event_id in self.seen:
            return False
        self.seen.add(event.event_id)
        self.state[event.event_id] = "PROCESSED"
        self.window.append(event)
        heappush(self.priority, (-event.amount, event.ts_epoch, event))
        return True

    def highest_value_exception(self) -> Event | None:
        return heappop(self.priority)[2] if self.priority else None
