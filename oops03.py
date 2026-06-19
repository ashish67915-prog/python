class Point:
    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
    
    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    def distance_from_origin(self):
        return self.euclidean_distance(Point(0,0))
        # or return ((self.x_cod)**2 + (self.y_cod)**2)**0.5   

class Line:
    def __init__(self,a,b,c):
        self.A = a
        self.B = b
        self.C = c

    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)
    
    def point_on_line(line,point):   #here line act as self
        if line.A*point.x_cod + line.B*point.y_cod + line.C == 0 :
            print("lies on the line")
        else:
            print("does not lies on the line")

    def shortest_dist(line,point):
        return abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/(line.A**2 + line.B**2)**0.5
    
        

p1 = Point(0,0)
p2 = Point(-2,-1)
distance_01 = p1.euclidean_distance(p2)
distance_02 = p1.distance_from_origin()

print(p1)
print(p2)
print(distance_01)
print(distance_02)



L1 = Line(1,2,3)
print(L1)



L2 = Line(1,1,-2)
P3 = Point(1,1)
L2.point_on_line(P3)
distance03 = L2.shortest_dist(P3)
print(distance03)

