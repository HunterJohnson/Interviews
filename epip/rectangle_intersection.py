# write a program that tests if 2 rectangles have a non-empty intersection
# if intersection is nonempty, return the rect. formed by their intersection

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height')) # x, y = left lower point

def intersect_rectangle(R1, R2):
  def is_intersect(R1, R2):
    return (R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x
             and R1.y <= R2.y + R2.height and R1.y + R1.height >= R2.y)
  if not is_intersect(R1,R2):
    return Rectangle(0,0,-1,-1) # No intersection
  return Rectangle(
    max(R1.x, R2.x), max(R1.y, R2.y)
    min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x)
    min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y))

# time complexity O(1)
