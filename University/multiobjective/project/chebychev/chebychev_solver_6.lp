\ Model Car Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  t
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
 chebychev1: 10.8 x_ij[1,1] + 10.8 x_ij[1,2] + 10.8 x_ij[1,3]
   + 10.8 x_ij[1,4] + 13.2 x_ij[2,1] + 13.2 x_ij[2,2] + 13.2 x_ij[2,3]
   + 13.2 x_ij[2,4] + 20.6 x_ij[3,1] + 20.6 x_ij[3,2] + 20.6 x_ij[3,3]
   + 20.6 x_ij[3,4] + 11.4 x_ij[4,1] + 11.4 x_ij[4,2] + 11.4 x_ij[4,3]
   + 11.4 x_ij[4,4] + 3.2 x_ij[5,1] + 3.2 x_ij[5,2] + 3.2 x_ij[5,3]
   + 3.2 x_ij[5,4] + 4.6 x_ij[6,1] + 4.6 x_ij[6,2] + 4.6 x_ij[6,3]
   + 4.6 x_ij[6,4] + 4.4 x_ij[7,1] + 4.4 x_ij[7,2] + 4.4 x_ij[7,3]
   + 4.4 x_ij[7,4] + 13.8 x_ij[8,1] + 13.8 x_ij[8,2] + 13.8 x_ij[8,3]
   + 13.8 x_ij[8,4] + 8.2 x_ij[9,1] + 8.2 x_ij[9,2] + 8.2 x_ij[9,3]
   + 8.2 x_ij[9,4] + 3.6 x_ij[10,1] + 3.6 x_ij[10,2] + 3.6 x_ij[10,3]
   + 3.6 x_ij[10,4] - t <= 24
 chebychev2: 47200 x_ij[1,1] + 47200 x_ij[1,2] + 47200 x_ij[1,3]
   + 47200 x_ij[1,4] + 58300 x_ij[2,1] + 58300 x_ij[2,2] + 58300 x_ij[2,3]
   + 58300 x_ij[2,4] + 185400 x_ij[3,1] + 185400 x_ij[3,2]
   + 185400 x_ij[3,3] + 185400 x_ij[3,4] + 81200 x_ij[4,1]
   + 81200 x_ij[4,2] + 81200 x_ij[4,3] + 81200 x_ij[4,4] + 96520 x_ij[5,1]
   + 96520 x_ij[5,2] + 96520 x_ij[5,3] + 96520 x_ij[5,4] + 430000 x_ij[6,1]
   + 430000 x_ij[6,2] + 430000 x_ij[6,3] + 430000 x_ij[6,4]
   + 95000 x_ij[7,1] + 95000 x_ij[7,2] + 95000 x_ij[7,3] + 95000 x_ij[7,4]
   + 72700 x_ij[8,1] + 72700 x_ij[8,2] + 72700 x_ij[8,3] + 72700 x_ij[8,4]
   + 44500 x_ij[9,1] + 44500 x_ij[9,2] + 44500 x_ij[9,3] + 44500 x_ij[9,4]
   + 83400 x_ij[10,1] + 83400 x_ij[10,2] + 83400 x_ij[10,3]
   + 83400 x_ij[10,4] - t <= 247000
 chebychev3: 900 x_ij[1,1] + 900 x_ij[1,2] + 900 x_ij[1,3] + 900 x_ij[1,4]
   + 720 x_ij[2,1] + 720 x_ij[2,2] + 720 x_ij[2,3] + 720 x_ij[2,4]
   + 3180 x_ij[3,1] + 3180 x_ij[3,2] + 3180 x_ij[3,3] + 3180 x_ij[3,4]
   + 900 x_ij[4,1] + 900 x_ij[4,2] + 900 x_ij[4,3] + 900 x_ij[4,4]
   + 1950 x_ij[5,1] + 1950 x_ij[5,2] + 1950 x_ij[5,3] + 1950 x_ij[5,4]
   + 8160 x_ij[6,1] + 8160 x_ij[6,2] + 8160 x_ij[6,3] + 8160 x_ij[6,4]
   + 1224 x_ij[7,1] + 1224 x_ij[7,2] + 1224 x_ij[7,3] + 1224 x_ij[7,4]
   + 900 x_ij[8,1] + 900 x_ij[8,2] + 900 x_ij[8,3] + 900 x_ij[8,4]
   + 600 x_ij[9,1] + 600 x_ij[9,2] + 600 x_ij[9,3] + 600 x_ij[9,4]
   + 1308 x_ij[10,1] + 1308 x_ij[10,2] + 1308 x_ij[10,3] + 1308 x_ij[10,4]
   - t <= 12600
Bounds
Binaries
 x_ij[1,1] x_ij[1,2] x_ij[1,3] x_ij[1,4] x_ij[2,1] x_ij[2,2] x_ij[2,3]
 x_ij[2,4] x_ij[3,1] x_ij[3,2] x_ij[3,3] x_ij[3,4] x_ij[4,1] x_ij[4,2]
 x_ij[4,3] x_ij[4,4] x_ij[5,1] x_ij[5,2] x_ij[5,3] x_ij[5,4] x_ij[6,1]
 x_ij[6,2] x_ij[6,3] x_ij[6,4] x_ij[7,1] x_ij[7,2] x_ij[7,3] x_ij[7,4]
 x_ij[8,1] x_ij[8,2] x_ij[8,3] x_ij[8,4] x_ij[9,1] x_ij[9,2] x_ij[9,3]
 x_ij[9,4] x_ij[10,1] x_ij[10,2] x_ij[10,3] x_ij[10,4]
End
