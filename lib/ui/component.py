from typing import Protocol, runtime_checkable

from pygame import Surface

type BBox = tuple[int, int, int, int]
type Size = tuple[int | None, int | None]
type Point = tuple[int, int]


@runtime_checkable
class Component(Protocol):
    """
    Represents a UI component.
    """

    def render(self, target: Surface, bbox: BBox):
        """
        Render the component to a target surface.
        """
        ...

    def size(self) -> Size:
        """
        Returns the size of the component.

        The tuple returned is (width, height).
        If any of them are None, it means the component stretches across the most available space.
        """
        ...

    def point_to(self, point: Point, bbox: BBox) -> "Component":
        """
        Returns the point an "actionable" component.

        The default implementation will default to whether the point lies within
        the bounding box at all. Containers should override this method to
        return the child present at that point.

        Arguments:
        point -- point where a component could be
        bbox  -- bounding box of where the search takes place
        """

        point_x, point_y = point
        bbox_x, bbox_y, bbox_w, bbox_h = bbox

        if point_x < bbox_x or point_x >= bbox_x + bbox_w:
            return None

        if point_y < bbox_y or point_y >= bbox_y + bbox_h:
            return None

        return self
