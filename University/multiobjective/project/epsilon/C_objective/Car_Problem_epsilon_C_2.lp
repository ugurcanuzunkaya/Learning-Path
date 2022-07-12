\ Model Car Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  5.4 x_ij[1,1] + 5.4 x_ij[1,2] + 5.4 x_ij[1,3] + 5.4 x_ij[1,4]
   + 6.6 x_ij[2,1] + 6.6 x_ij[2,2] + 6.6 x_ij[2,3] + 6.6 x_ij[2,4]
   + 10.3 x_ij[3,1] + 10.3 x_ij[3,2] + 10.3 x_ij[3,3] + 10.3 x_ij[3,4]
   + 5.7 x_ij[4,1] + 5.7 x_ij[4,2] + 5.7 x_ij[4,3] + 5.7 x_ij[4,4]
   + 1.6 x_ij[5,1] + 1.6 x_ij[5,2] + 1.6 x_ij[5,3] + 1.6 x_ij[5,4]
   + 2.3 x_ij[6,1] + 2.3 x_ij[6,2] + 2.3 x_ij[6,3] + 2.3 x_ij[6,4]
   + 2.2 x_ij[7,1] + 2.2 x_ij[7,2] + 2.2 x_ij[7,3] + 2.2 x_ij[7,4]
   + 6.9 x_ij[8,1] + 6.9 x_ij[8,2] + 6.9 x_ij[8,3] + 6.9 x_ij[8,4]
   + 4.1 x_ij[9,1] + 4.1 x_ij[9,2] + 4.1 x_ij[9,3] + 4.1 x_ij[9,4]
   + 1.8 x_ij[10,1] + 1.8 x_ij[10,2] + 1.8 x_ij[10,3] + 1.8 x_ij[10,4]
Subject To
 everyone_buy_one_car[1]: x_ij[1,1] + x_ij[2,1] + x_ij[3,1] + x_ij[4,1]
   + x_ij[5,1] + x_ij[6,1] + x_ij[7,1] + x_ij[8,1] + x_ij[9,1] + x_ij[10,1]
   = 1
 everyone_buy_one_car[2]: x_ij[1,2] + x_ij[2,2] + x_ij[3,2] + x_ij[4,2]
   + x_ij[5,2] + x_ij[6,2] + x_ij[7,2] + x_ij[8,2] + x_ij[9,2] + x_ij[10,2]
   = 1
 everyone_buy_one_car[3]: x_ij[1,3] + x_ij[2,3] + x_ij[3,3] + x_ij[4,3]
   + x_ij[5,3] + x_ij[6,3] + x_ij[7,3] + x_ij[8,3] + x_ij[9,3] + x_ij[10,3]
   = 1
 everyone_buy_one_car[4]: x_ij[1,4] + x_ij[2,4] + x_ij[3,4] + x_ij[4,4]
   + x_ij[5,4] + x_ij[6,4] + x_ij[7,4] + x_ij[8,4] + x_ij[9,4] + x_ij[10,4]
   = 1
 Power_constraints_for_3rd_person: 150 x_ij[1,3] + 120 x_ij[2,3]
   + 530 x_ij[3,3] + 150 x_ij[4,3] + 325 x_ij[5,3] + 1360 x_ij[6,3]
   + 204 x_ij[7,3] + 150 x_ij[8,3] + 100 x_ij[9,3] + 218 x_ij[10,3] >= 100
 Power_constraint_for_4th_person: 150 x_ij[1,4] + 120 x_ij[2,4]
   + 530 x_ij[3,4] + 150 x_ij[4,4] + 325 x_ij[5,4] + 1360 x_ij[6,4]
   + 204 x_ij[7,4] + 150 x_ij[8,4] + 100 x_ij[9,4] + 218 x_ij[10,4] >= 125
 Four_door_for_1st_person: x_ij[1,1] + x_ij[2,1] + x_ij[3,1] + x_ij[5,1]
   + x_ij[7,1] + x_ij[9,1] = 1
 Two_door_for_2nd_person: x_ij[4,2] + x_ij[6,2] + x_ij[8,2] + x_ij[10,2]
   = 1
 Diesel_type_for_1st_person: x_ij[1,1] + x_ij[3,1] + x_ij[4,1] + x_ij[9,1]
   = 1
 Gasoline_type_for_2nd_person: x_ij[2,2] + x_ij[8,2] = 1
 Electric_type_for_3rd_person: x_ij[5,3] + x_ij[6,3] + x_ij[7,3]
   + x_ij[10,3] = 1
 Brand_constraint: x_ij[1,4] + x_ij[2,4] + x_ij[9,4] + x_ij[10,4] = 1
 Cost_constraint: 150 x_ij[1,1] + 150 x_ij[1,2] + 150 x_ij[1,3]
   + 150 x_ij[1,4] + 120 x_ij[2,1] + 120 x_ij[2,2] + 120 x_ij[2,3]
   + 120 x_ij[2,4] + 530 x_ij[3,1] + 530 x_ij[3,2] + 530 x_ij[3,3]
   + 530 x_ij[3,4] + 150 x_ij[4,1] + 150 x_ij[4,2] + 150 x_ij[4,3]
   + 150 x_ij[4,4] + 325 x_ij[5,1] + 325 x_ij[5,2] + 325 x_ij[5,3]
   + 325 x_ij[5,4] + 1360 x_ij[6,1] + 1360 x_ij[6,2] + 1360 x_ij[6,3]
   + 1360 x_ij[6,4] + 204 x_ij[7,1] + 204 x_ij[7,2] + 204 x_ij[7,3]
   + 204 x_ij[7,4] + 150 x_ij[8,1] + 150 x_ij[8,2] + 150 x_ij[8,3]
   + 150 x_ij[8,4] + 100 x_ij[9,1] + 100 x_ij[9,2] + 100 x_ij[9,3]
   + 100 x_ij[9,4] + 218 x_ij[10,1] + 218 x_ij[10,2] + 218 x_ij[10,3]
   + 218 x_ij[10,4] <= 2500
 Power_constraint: 23600 x_ij[1,1] + 23600 x_ij[1,2] + 23600 x_ij[1,3]
   + 23600 x_ij[1,4] + 29150 x_ij[2,1] + 29150 x_ij[2,2] + 29150 x_ij[2,3]
   + 29150 x_ij[2,4] + 92700 x_ij[3,1] + 92700 x_ij[3,2] + 92700 x_ij[3,3]
   + 92700 x_ij[3,4] + 40600 x_ij[4,1] + 40600 x_ij[4,2] + 40600 x_ij[4,3]
   + 40600 x_ij[4,4] + 48260 x_ij[5,1] + 48260 x_ij[5,2] + 48260 x_ij[5,3]
   + 48260 x_ij[5,4] + 215000 x_ij[6,1] + 215000 x_ij[6,2]
   + 215000 x_ij[6,3] + 215000 x_ij[6,4] + 47500 x_ij[7,1]
   + 47500 x_ij[7,2] + 47500 x_ij[7,3] + 47500 x_ij[7,4] + 36350 x_ij[8,1]
   + 36350 x_ij[8,2] + 36350 x_ij[8,3] + 36350 x_ij[8,4] + 22250 x_ij[9,1]
   + 22250 x_ij[9,2] + 22250 x_ij[9,3] + 22250 x_ij[9,4] + 41700 x_ij[10,1]
   + 41700 x_ij[10,2] + 41700 x_ij[10,3] + 41700 x_ij[10,4] <= 124200
Bounds
Binaries
 x_ij[1,1] x_ij[1,2] x_ij[1,3] x_ij[1,4] x_ij[2,1] x_ij[2,2] x_ij[2,3]
 x_ij[2,4] x_ij[3,1] x_ij[3,2] x_ij[3,3] x_ij[3,4] x_ij[4,1] x_ij[4,2]
 x_ij[4,3] x_ij[4,4] x_ij[5,1] x_ij[5,2] x_ij[5,3] x_ij[5,4] x_ij[6,1]
 x_ij[6,2] x_ij[6,3] x_ij[6,4] x_ij[7,1] x_ij[7,2] x_ij[7,3] x_ij[7,4]
 x_ij[8,1] x_ij[8,2] x_ij[8,3] x_ij[8,4] x_ij[9,1] x_ij[9,2] x_ij[9,3]
 x_ij[9,4] x_ij[10,1] x_ij[10,2] x_ij[10,3] x_ij[10,4]
End
