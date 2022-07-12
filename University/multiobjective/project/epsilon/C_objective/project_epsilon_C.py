import gurobipy as gp
from gurobipy import GRB

C = [None, 5.4, 6.6, 10.3, 5.7, 1.6, 2.3, 2.2, 6.9, 4.1, 1.8]
P = [None, 150, 120, 530, 150, 325, 1360, 204, 150, 100, 218]
PR = [None, 23600, 29150, 92700, 40600, 48260, 215000, 47500, 36350, 22250, 41700]
F = [None, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
T = [None, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]
DI = [None, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]
G = [None, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
E = [None, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1]

Set_I = range(1, 11)
Set_J = range(1, 5)
for i in range(6):

    m1 = gp.Model("Car Problem")
    x_ij = m1.addVars(Set_I, Set_J, vtype=GRB.BINARY, name="x_ij")
    m1.setParam(GRB.Param.IntegralityFocus, 1)
    m1.update()

    m1.addConstrs((gp.quicksum(x_ij[i, j] for i in Set_I) == 1 for j in Set_J), name="everyone buy one car")
    m1.addConstr(gp.quicksum(x_ij[i, 3] * P[i] for i in Set_I) >= 100, name="Power constraints for 3rd person")
    m1.addConstr(gp.quicksum(x_ij[i, 4] * P[i] for i in Set_I) >= 125, name="Power constraint for 4th person")
    m1.addConstr(gp.quicksum(x_ij[i, 1] * F[i] for i in Set_I) == 1, name="Four door for 1st person")
    m1.addConstr(gp.quicksum(x_ij[i, 2] * T[i] for i in Set_I) == 1, name="Two door for 2nd person")
    m1.addConstr(gp.quicksum(x_ij[i, 1] * DI[i] for i in Set_I) == 1, name="Diesel type for 1st person")
    m1.addConstr(gp.quicksum(x_ij[i, 2] * G[i] for i in Set_I) == 1, name="Gasoline type for 2nd person")
    m1.addConstr(gp.quicksum(x_ij[i, 3] * E[i] for i in Set_I) == 1, name="Electric type for 3rd person")
    m1.addConstr(x_ij[1, 4] + x_ij[2, 4] + x_ij[9, 4] + x_ij[10, 4] == 1, name="Brand constraint")

    epsilon1 = 2600 - i * 100
    epsilon2 = 124300 - i * 100

    m1.addConstr(gp.quicksum(x_ij[i, j] * P[i] for i in Set_I for j in Set_J) <= epsilon1, name="Cost constraint")
    m1.addConstr(gp.quicksum(x_ij[i, j] * PR[i] for i in Set_I for j in Set_J) <= epsilon2, name="Power constraint")
    m1.update()
    
    m1.setObjective(gp.quicksum(x_ij[i, j] * C[i] for i in Set_I for j in Set_J), GRB.MINIMIZE)
    m1.update()
    m1.write(f"Car_Problem_epsilon_C_{str(i+1)}.lp")
    m1.optimize()
    if m1.status != GRB.Status.INFEASIBLE:
        print("\nCar Problem Solution: (C Obj)", i + 1, m1.objVal)
        for v in m1.getVars():
            if v.x != 0:
                print(v.varName, v.x)
    else:
        print("\nCar Problem Solution: (C Obj)", i + 1, "INFEASIBLE")

    print()
