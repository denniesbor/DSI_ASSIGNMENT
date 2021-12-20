import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon, Polygon
import math
import numpy as np

# A Point class object takes in a tuple of x,y coordinates.
# The instance of the object returns the individual coordinates

class Point:
	def __init__(self, coords):
		self.x = coords[0]
		self.y = coords[1]


class Hexagon:
  # class methods
  random_point = None
  validate = False
  
  def __init__(self,triangle = None,radius = 10):
    self.triangle = triangle
    self.radius = radius

  def draw_hexagon(self):
    # draws an hexagon
    rect = RegularPolygon((0,0), 6, radius = self.radius, orientation = 0, fill= False)

    # obtains vertices of the triangle
    verts = rect.get_path().vertices
    trans = rect.get_patch_transform()
    points = trans.transform(verts)
    points_list = [ tuple(x) for x in points.tolist()]

    # round off the points
    points = np.around(points, decimals=4)

    return [points,rect,points_list]


    # Area of a tringle given coordinates
  def area_triangle(self,p,q,r):
    area = (1/2)*abs(p.x*(q.y-r.y)+q.x*(r.y-p.y)+r.x*(p.y-q.y))
    return area

  # Area of an hexagon:
  def hexagon_area(self,s):
    area = (1/2)*3*math.sqrt(3)*s**2

    return area

  # This function takes in a random coordinate, validate and returns coordinates of a random triangle
  def find_adjacent(self):

    points,rect,points_list = self.draw_hexagon()
    triangle_coords = []
    areas = []

    for i,point in enumerate(points_list):
      if(i+1 < len(points_list)):
        p = Point(self.random_point)
        q = Point(point)
        r = Point(points_list[i+1])
        area = self.area_triangle(p,q,r)
        areas.append(area)
        triangle_coords.append([self.random_point,point,points_list[i+1]])

    random_index = np.random.randint(len(triangle_coords)) #random index
    if(self.validate):
      area_hexagon = self.hexagon_area(self.radius)
      area_triangles = sum(areas)

      if(area_triangles < area_hexagon + 0.3 and area_triangles > area_hexagon - 0.3):
        return triangle_coords[random_index]
      else:
        raise Exception('Your Random Point not within the Hexagon. x should be between -9 and 9, and y should be between -10 and 10')
    if(not self.validate):
      return triangle_coords[random_index]



  # user input
  def inputNumber(self,message):
    while True:
      try:
        userInput = float(input(message))       
      except ValueError:
        print("Not an integer! Try again.")
        continue
      else:
        return userInput 
        break 

  # the function draws a triangle given coordinates of the vertices
  def draw_triangle(self):
    if(self.triangle):
      coordinates = np.asarray(self.triangle)
      triangle  = Polygon(coordinates,fill= False, closed =True)
      return triangle
    else:
      triangle = self.find_adjacent()
      coordinates = np.asarray(triangle)
      self.triangle = triangle
      triangle  = Polygon(coordinates,fill= False, closed =True)
      return triangle


  # the method computes centroid of a triangle
  def centroid_triangle(self):
    p, q, r = self.triangle

    p = Point(p)
    q = Point(q)
    r = Point(r)

    x = (p.x +q.x + r.x)/3
    y = (p.y +q.y + r.y)/3

    return (x,y)

  # The method returns matplotlib figure
  def show_figure(self,triangle = None,centroid = False):

    points,rect,points_list = self.draw_hexagon()

    fig = plt.figure(figsize=(6,4),dpi=150)
    if(centroid):
      centroid =  self.centroid_triangle()
      plt.scatter(centroid[0],centroid[1],alpha = 0.7, c = 'r')
      plt.text(centroid[0]+0.3,centroid[1],'Centroid',color='k', fontsize = 10)

    plt.scatter(points[:, 0], points[:, 1],alpha=0.7, c = 'k');
    plt.gca().add_patch(rect);
    if(triangle):
      plt.gca().add_patch(triangle)
      plt.scatter(self.random_point[0],self.random_point[1],alpha = 0.7, c = 'k')
      plt.text(self.random_point[0],self.random_point[1],'P',color='blue', fontsize = 14)
    plt.xlabel('X coordinates')
    plt.ylabel('y coordinates')
    plt.tick_params(axis='x',which='major',length=10,direction='out',width=1,top=True)
    plt.tick_params(axis='y',which='major',length=10,right=True)
    plt.yticks(fontsize=12)

    plt.show()

  @classmethod
  def random_tri(cls, random_point, validate = False):
    cls.random_point = random_point
    cls.validate = validate


if __name__ == '__main__':
    print('success')