import numpy as np
import math


def project_point(P, u=None, v=None, n=None):
    if n is None:
        n = np.cross(u, v)
    projection = P - (np.dot(P, n) / (np.linalg.norm(n)**2)) * n
    return projection


vector_u = np.array([1, 1, 0])
vector_V = np.array([0, -1, 0])
P = np.array([math.pi, math.e, 1])


# Resultaten blir identiska då den negativa vektorn av v fortfarande spänner upp samma plan
# skillnaden blir då att punkter och vektorer förändras, men i vårt fall använder vi normalvektorn 
# därmerd kommer projektionen vara likadan
print(project_point(P, vector_u, vector_V))
print(project_point(P, vector_u, -vector_V))


n = np.array([1, 1, 1])
m = np.array([3, 3, 3])
# Resultaten blir identiska då båda vektorerna är linjärt beroende och därmed är normalvektorer för samma plan
print(project_point(P, n=n))
print(project_point(P, n=m))
