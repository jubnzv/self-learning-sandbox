# This file was generated by jschema_to_python version 1.2.3.

import attr


@attr.s
class TestRoot(object):
    """A geographical coordinate."""

    latitude = attr.ib(metadata={"schema_property_name": "latitude"})
    longitude = attr.ib(metadata={"schema_property_name": "longitude"})
