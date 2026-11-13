from streaming.event_processor import Event, EventProcessor

def test_event_processor_deduplicates_and_prioritizes():
    p = EventProcessor()
    a = Event("E1","C1","DECLINED",1,100.0)
    b = Event("E2","C2","DECLINED",2,500.0)
    assert p.process(a) is True
    assert p.process(a) is False
    assert p.process(b) is True
    assert p.highest_value_exception().event_id == "E2"
