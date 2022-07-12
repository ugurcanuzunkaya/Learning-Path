\ Model Car Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  3.124045721034207 x_ij[1,1] + 3.124045721034207 x_ij[1,2]
   + 3.124045721034207 x_ij[1,3] + 3.124045721034207 x_ij[1,4]
   + 3.848792670451255 x_ij[2,1] + 3.848792670451255 x_ij[2,2]
   + 3.848792670451255 x_ij[2,3] + 3.848792670451255 x_ij[2,4]
   + 6.23568524956434 x_ij[3,1] + 6.23568524956434 x_ij[3,2]
   + 6.23568524956434 x_ij[3,3] + 6.23568524956434 x_ij[3,4]
   + 3.427919813043892 x_ij[4,1] + 3.427919813043892 x_ij[4,2]
   + 3.427919813043892 x_ij[4,3] + 3.427919813043892 x_ij[4,4]
   + 1.134463872571692 x_ij[5,1] + 1.134463872571692 x_ij[5,2]
   + 1.134463872571692 x_ij[5,3] + 1.134463872571692 x_ij[5,4]
   + 2.410745234175298 x_ij[6,1] + 2.410745234175298 x_ij[6,2]
   + 2.410745234175298 x_ij[6,3] + 2.410745234175298 x_ij[6,4]
   + 1.515250472239558 x_ij[7,1] + 1.515250472239558 x_ij[7,2]
   + 1.515250472239558 x_ij[7,3] + 1.515250472239558 x_ij[7,4]
   + 4.060284623374804 x_ij[8,1] + 4.060284623374804 x_ij[8,2]
   + 4.060284623374804 x_ij[8,3] + 4.060284623374804 x_ij[8,4]
   + 2.413071104848739 x_ij[9,1] + 2.413071104848739 x_ij[9,2]
   + 2.413071104848739 x_ij[9,3] + 2.413071104848739 x_ij[9,4]
   + 1.240016127752388 x_ij[10,1] + 1.240016127752388 x_ij[10,2]
   + 1.240016127752388 x_ij[10,3] + 1.240016127752388 x_ij[10,4]
   - 10 Constant
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
Bounds
 Constant = 1
Binaries
 x_ij[1,1] x_ij[1,2] x_ij[1,3] x_ij[1,4] x_ij[2,1] x_ij[2,2] x_ij[2,3]
 x_ij[2,4] x_ij[3,1] x_ij[3,2] x_ij[3,3] x_ij[3,4] x_ij[4,1] x_ij[4,2]
 x_ij[4,3] x_ij[4,4] x_ij[5,1] x_ij[5,2] x_ij[5,3] x_ij[5,4] x_ij[6,1]
 x_ij[6,2] x_ij[6,3] x_ij[6,4] x_ij[7,1] x_ij[7,2] x_ij[7,3] x_ij[7,4]
 x_ij[8,1] x_ij[8,2] x_ij[8,3] x_ij[8,4] x_ij[9,1] x_ij[9,2] x_ij[9,3]
 x_ij[9,4] x_ij[10,1] x_ij[10,2] x_ij[10,3] x_ij[10,4]
End
