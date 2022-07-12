\ Model Car Problem
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  1.83237905436754 x_ij[1,1] + 1.83237905436754 x_ij[1,2]
   + 1.83237905436754 x_ij[1,3] + 1.83237905436754 x_ij[1,4]
   + 2.287351992485154 x_ij[2,1] + 2.287351992485154 x_ij[2,2]
   + 2.287351992485154 x_ij[2,3] + 2.287351992485154 x_ij[2,4]
   + 6.466028940713115 x_ij[3,1] + 6.466028940713115 x_ij[3,2]
   + 6.466028940713115 x_ij[3,3] + 6.466028940713115 x_ij[3,4]
   + 2.950871790445022 x_ij[4,1] + 2.950871790445022 x_ij[4,2]
   + 2.950871790445022 x_ij[4,3] + 2.950871790445022 x_ij[4,4]
   + 3.083239767110299 x_ij[5,1] + 3.083239767110299 x_ij[5,2]
   + 3.083239767110299 x_ij[5,3] + 3.083239767110299 x_ij[5,4]
   + 13.43958233398697 x_ij[6,1] + 13.43958233398697 x_ij[6,2]
   + 13.43958233398697 x_ij[6,3] + 13.43958233398697 x_ij[6,4]
   + 3.129421847004153 x_ij[7,1] + 3.129421847004153 x_ij[7,2]
   + 3.129421847004153 x_ij[7,3] + 3.129421847004153 x_ij[7,4]
   + 2.759790273092318 x_ij[8,1] + 2.759790273092318 x_ij[8,2]
   + 2.759790273092318 x_ij[8,3] + 2.759790273092318 x_ij[8,4]
   + 1.677077696185839 x_ij[9,1] + 1.677077696185839 x_ij[9,2]
   + 1.677077696185839 x_ij[9,3] + 1.677077696185839 x_ij[9,4]
   + 2.720948331142218 x_ij[10,1] + 2.720948331142218 x_ij[10,2]
   + 2.720948331142218 x_ij[10,3] + 2.720948331142218 x_ij[10,4]
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
