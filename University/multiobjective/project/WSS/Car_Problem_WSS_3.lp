\ Model Car Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0.034032434940318 x_ij[1,1] + 0.034032434940318 x_ij[1,2]
   + 0.034032434940318 x_ij[1,3] + 0.034032434940318 x_ij[1,4]
   + 0.2684487082428114 x_ij[2,1] + 0.2684487082428114 x_ij[2,2]
   + 0.2684487082428114 x_ij[2,3] + 0.2684487082428114 x_ij[2,4]
   - 0.4143061390785114 x_ij[3,1] - 0.4143061390785114 x_ij[3,2]
   - 0.4143061390785114 x_ij[3,3] - 0.4143061390785114 x_ij[3,4]
   + 0.19207319361667 x_ij[4,1] + 0.19207319361667 x_ij[4,2]
   + 0.19207319361667 x_ij[4,3] + 0.19207319361667 x_ij[4,4]
   - 0.6508426917428434 x_ij[5,1] - 0.6508426917428434 x_ij[5,2]
   - 0.6508426917428434 x_ij[5,3] - 0.6508426917428434 x_ij[5,4]
   - 2.923430781964846 x_ij[6,1] - 2.923430781964846 x_ij[6,2]
   - 2.923430781964846 x_ij[6,3] - 2.923430781964846 x_ij[6,4]
   - 0.1866120412925746 x_ij[7,1] - 0.1866120412925746 x_ij[7,2]
   - 0.1866120412925746 x_ij[7,3] - 0.1866120412925746 x_ij[7,4]
   + 0.2411046706142487 x_ij[8,1] + 0.2411046706142487 x_ij[8,2]
   + 0.2411046706142487 x_ij[8,3] + 0.2411046706142487 x_ij[8,4]
   + 0.110006691897258 x_ij[9,1] + 0.110006691897258 x_ij[9,2]
   + 0.110006691897258 x_ij[9,3] + 0.110006691897258 x_ij[9,4]
   - 0.3108031813707303 x_ij[10,1] - 0.3108031813707303 x_ij[10,2]
   - 0.3108031813707303 x_ij[10,3] - 0.3108031813707303 x_ij[10,4]
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
