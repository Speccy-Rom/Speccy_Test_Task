import datetime as dt
import os
import sys

from freezegun import freeze_time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parsing import parsing_python_org_upcoming_events as upcoming  # noqa


@freeze_time("2020-12-15")
def test_parsing_date():
    html_doc = """
    <div class="shrubbery">
    <h2>Upcoming Events</h2>
    <ul>
    <li>
    <time datetime="2020-12-17T06:00:00+00:00"></time>
    <a href="/events/python-user-group/993/">Python Mauritius User</a></li>
    <li>
    <time datetime="2020-12-17T00:00:00+00:00"></time>
    <a href="/events/python-events/990/">PyCon Tanzania 2020</a></li>
    </ul>
    </div>
    """
    events = upcoming(html_doc)
    for event in events:
        date, event_name = event
        assert date in (dt.date(2020, 11, 15), dt.date(2020, 12, 16))
        assert event_name in ('PyCode Conference 2020',
                              'Python Mauritius User')