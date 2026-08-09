from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


point_spec = spec_from_file_location("point", Path(__file__).with_name("05.02.2026_point.py"))
point_module = module_from_spec(point_spec)
point_spec.loader.exec_module(point_module)
Point = point_module.Point


def test_point_movement_and_string():
    point = Point(5.4, 8.1)
    point.move_right(2.5)
    point.move_up(3)
    assert str(point) == "Point(x=7.9, y=11.1)"
