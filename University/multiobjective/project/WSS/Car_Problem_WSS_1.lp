\ Model Car Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0.4990457210342064 x_ij[1,1] + 0.4990457210342064 x_ij[1,2]
   + 0.4990457210342064 x_ij[1,3] + 0.4990457210342064 x_ij[1,4]
   + 0.6404593371179221 x_ij[2,1] + 0.6404593371179221 x_ij[2,2]
   + 0.6404593371179221 x_ij[2,3] + 0.6404593371179221 x_ij[2,4]
   + 1.228740805119894 x_ij[3,1] + 1.228740805119894 x_ij[3,2]
   + 1.228740805119894 x_ij[3,3] + 1.228740805119894 x_ij[3,4]
   + 0.6570864797105583 x_ij[4,1] + 0.6570864797105583 x_ij[4,2]
   + 0.6570864797105583 x_ij[4,3] + 0.6570864797105583 x_ij[4,4]
   + 0.3566860947939149 x_ij[5,1] + 0.3566860947939149 x_ij[5,2]
   + 0.3566860947939149 x_ij[5,3] + 0.3566860947939149 x_ij[5,4]
   + 1.292689678619743 x_ij[6,1] + 1.292689678619743 x_ij[6,2]
   + 1.292689678619743 x_ij[6,3] + 1.292689678619743 x_ij[6,4]
   + 0.4458060277951137 x_ij[7,1] + 0.4458060277951137 x_ij[7,2]
   + 0.4458060277951137 x_ij[7,3] + 0.4458060277951137 x_ij[7,4]
   + 0.706117956708137 x_ij[8,1] + 0.706117956708137 x_ij[8,2]
   + 0.706117956708137 x_ij[8,3] + 0.706117956708137 x_ij[8,4]
   + 0.4200155492931836 x_ij[9,1] + 0.4200155492931836 x_ij[9,2]
   + 0.4200155492931836 x_ij[9,3] + 0.4200155492931836 x_ij[9,4]
   + 0.3650161277523876 x_ij[10,1] + 0.3650161277523876 x_ij[10,2]
   + 0.3650161277523876 x_ij[10,3] + 0.3650161277523876 x_ij[10,4]
   - 3 Constant
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
