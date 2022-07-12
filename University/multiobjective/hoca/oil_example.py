import gurobipy as gp
from gurobipy import GRB

Set_I = range(1, 5)
Set_J = range(1, 4)
Capacity = [5000, 2400, 4000, 1500]
Blending = [[-0.3, -0.3, 0.7, -0.3], [0.4, 0.4, -0.6, 0.4], [-0.5, 0.5, -0.5, -0.5]]
Blending1 = [0.2, -0.8, 0.2, 0.2]
Price = [12, 18, 10]
Cost = [-9, -7, -12, -6]

m1 = gp.Model("Oil_Example")
x_ij = m1.addVars(Set_I, Set_J, vtype=GRB.INTEGER, lb=0.0, name="x_ij")

m1.addConstrs((x_ij.sum(i, '*') <= Capacity[i - 1] for i in Set_I), "Capacity")
m1.update()
m1.addConstr(gp.quicksum(Blending1[i - 1] * x_ij[i, 1] for i in Set_I) <= 0, "Blending1")
m1.addConstrs((gp.quicksum(Blending[j - 1][i - 1] * x_ij[i, j] for i in Set_I) <= 0 for j in Set_J), "Blending")
m1.update()
m1.setObjective(gp.quicksum(Price[j - 1] * x_ij[i, j] for i in Set_I for j in Set_J) +
                gp.quicksum(Cost[i - 1] * x_ij[i, j] for j in Set_J for i in Set_I) +
                gp.quicksum(x_ij[i, 1] for i in Set_I), GRB.MAXIMIZE)
m1.update()
m1.optimize()
m1.write("oil_example.lp")

print("\nOptimal Solution:")
for i in Set_I:
    for j in Set_J:
        if x_ij[i, j].x > 0:
            print(f"x_ij[{i},{j}] = {x_ij[i, j].x}")

print("\nObjective Value: {}".format(m1.objVal))
