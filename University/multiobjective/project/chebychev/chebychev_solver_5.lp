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
 chebychev2: 94400 x_ij[1,1] + 94400 x_ij[1,2] + 94400 x_ij[1,3]
   + 94400 x_ij[1,4] + 116600 x_ij[2,1] + 116600 x_ij[2,2]
   + 116600 x_ij[2,3] + 116600 x_ij[2,4] + 370800 x_ij[3,1]
   + 370800 x_ij[3,2] + 370800 x_ij[3,3] + 370800 x_ij[3,4]
   + 162400 x_ij[4,1] + 162400 x_ij[4,2] + 162400 x_ij[4,3]
   + 162400 x_ij[4,4] + 193040 x_ij[5,1] + 193040 x_ij[5,2]
   + 193040 x_ij[5,3] + 193040 x_ij[5,4] + 860000 x_ij[6,1]
   + 860000 x_ij[6,2] + 860000 x_ij[6,3] + 860000 x_ij[6,4]
   + 190000 x_ij[7,1] + 190000 x_ij[7,2] + 190000 x_ij[7,3]
   + 190000 x_ij[7,4] + 145400 x_ij[8,1] + 145400 x_ij[8,2]
   + 145400 x_ij[8,3] + 145400 x_ij[8,4] + 89000 x_ij[9,1]
   + 89000 x_ij[9,2] + 89000 x_ij[9,3] + 89000 x_ij[9,4]
   + 166800 x_ij[10,1] + 166800 x_ij[10,2] + 166800 x_ij[10,3]
   + 166800 x_ij[10,4] - t <= 494000
 chebychev3: 600 x_ij[1,1] + 600 x_ij[1,2] + 600 x_ij[1,3] + 600 x_ij[1,4]
   + 480 x_ij[2,1] + 480 x_ij[2,2] + 480 x_ij[2,3] + 480 x_ij[2,4]
   + 2120 x_ij[3,1] + 2120 x_ij[3,2] + 2120 x_ij[3,3] + 2120 x_ij[3,4]
   + 600 x_ij[4,1] + 600 x_ij[4,2] + 600 x_ij[4,3] + 600 x_ij[4,4]
   + 1300 x_ij[5,1] + 1300 x_ij[5,2] + 1300 x_ij[5,3] + 1300 x_ij[5,4]
   + 5440 x_ij[6,1] + 5440 x_ij[6,2] + 5440 x_ij[6,3] + 5440 x_ij[6,4]
   + 816 x_ij[7,1] + 816 x_ij[7,2] + 816 x_ij[7,3] + 816 x_ij[7,4]
   + 600 x_ij[8,1] + 600 x_ij[8,2] + 600 x_ij[8,3] + 600 x_ij[8,4]
   + 400 x_ij[9,1] + 400 x_ij[9,2] + 400 x_ij[9,3] + 400 x_ij[9,4]
   + 872 x_ij[10,1] + 872 x_ij[10,2] + 872 x_ij[10,3] + 872 x_ij[10,4] - t
   <= 8400
Bounds
Binaries
 x_ij[1,1] x_ij[1,2] x_ij[1,3] x_ij[1,4] x_ij[2,1] x_ij[2,2] x_ij[2,3]
 x_ij[2,4] x_ij[3,1] x_ij[3,2] x_ij[3,3] x_ij[3,4] x_ij[4,1] x_ij[4,2]
 x_ij[4,3] x_ij[4,4] x_ij[5,1] x_ij[5,2] x_ij[5,3] x_ij[5,4] x_ij[6,1]
 x_ij[6,2] x_ij[6,3] x_ij[6,4] x_ij[7,1] x_ij[7,2] x_ij[7,3] x_ij[7,4]
 x_ij[8,1] x_ij[8,2] x_ij[8,3] x_ij[8,4] x_ij[9,1] x_ij[9,2] x_ij[9,3]
 x_ij[9,4] x_ij[10,1] x_ij[10,2] x_ij[10,3] x_ij[10,4]
End
