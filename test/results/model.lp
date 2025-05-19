\ Model model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  y1
Subject To
 constraint_1: a_A >= 0.8
 constraint_2: - a_A + a_(some_S_A) >= 0
 constraint_3: - a_A + a_(some_R_A) >= 0
 constraint_4: - a_(some_S_A) - a_(all_S_(not_A)) = -1
 constraint_5: - a_(some_R_A) - a_(all_R_(not_A)) = -1
 constraint_7: - (a,i1)_S + i1_{_i1_} >= 0
 constraint_8: a_(some_S_A) - i1_A <= 0
 constraint_9: a_(some_S_A) - (a,i1)_S <= 0
 constraint_10: - i1_A + i1_(some_S_A) >= 0
 constraint_11: - i1_A + i1_(some_R_A) >= 0
 constraint_12: - i1_(some_S_A) - i1_(all_S_(not_A)) = -1
 constraint_13: - i1_(some_R_A) - i1_(all_R_(not_A)) = -1
 constraint_15: - (a,i2)_R + i2_{_i2_} >= 0
 constraint_16: a_(some_R_A) - i2_A <= 0
 constraint_17: a_(some_R_A) - (a,i2)_R <= 0
 constraint_18: - i2_A + i2_(some_S_A) >= 0
 constraint_19: - i2_A + i2_(some_R_A) >= 0
 constraint_20: - i2_(some_S_A) - i2_(all_S_(not_A)) = -1
 constraint_21: - i2_(some_R_A) - i2_(all_R_(not_A)) = -1
 constraint_23: - (i1,i3)_S + i3_{_i3_} >= 0
 constraint_24: i1_(some_S_A) - i3_A <= 0
 constraint_25: i1_(some_S_A) - (i1,i3)_S <= 0
 constraint_26: - i3_A + i3_(some_S_A) >= 0
 constraint_27: - i3_A + i3_(some_R_A) >= 0
 constraint_28: - i3_(some_S_A) - i3_(all_S_(not_A)) = -1
 constraint_29: - i3_(some_R_A) - i3_(all_R_(not_A)) = -1
 constraint_31: - (i1,i4)_R + i4_{_i4_} >= 0
 constraint_32: i1_(some_R_A) - i4_A <= 0
 constraint_33: i1_(some_R_A) - (i1,i4)_R <= 0
 constraint_34: - i4_A + i4_(some_S_A) >= 0
 constraint_35: - i4_A + i4_(some_R_A) >= 0
 constraint_36: - i4_(some_S_A) - i4_(all_S_(not_A)) = -1
 constraint_37: - i4_(some_R_A) - i4_(all_R_(not_A)) = -1
 constraint_38: y1 + a_(all_R_(all_R_(not_A))) >= 1
 constraint_39: - a_(all_R_(all_R_(not_A))) - a_(some_R_(some_R_A)) = -1
 constraint_40: i2_(all_R_(not_A)) - a_(all_R_(all_R_(not_A))) + y2 >= 0
 constraint_41: - (a,i2)_R - a_(all_R_(all_R_(not_A))) - y2 >= -2
 constraint_42: - i2_(some_R_A) - i2_(all_R_(not_A)) = -1
Bounds
 a_A <= 1
 a_(some_S_A) <= 1
 a_(some_R_A) <= 1
 a_(all_S_(not_A)) <= 1
 a_(all_R_(not_A)) <= 1
 (a,i1)_S <= 1
 i1_A <= 1
 i1_(some_S_A) <= 1
 i1_(some_R_A) <= 1
 i1_(all_S_(not_A)) <= 1
 i1_(all_R_(not_A)) <= 1
 (a,i2)_R <= 1
 i2_A <= 1
 i2_(some_S_A) <= 1
 i2_(some_R_A) <= 1
 i2_(all_S_(not_A)) <= 1
 i2_(all_R_(not_A)) <= 1
 (i1,i3)_S <= 1
 i3_A <= 1
 i3_(some_S_A) <= 1
 i3_(some_R_A) <= 1
 i3_(all_S_(not_A)) <= 1
 i3_(all_R_(not_A)) <= 1
 (i1,i4)_R <= 1
 i4_A <= 1
 i4_(some_S_A) <= 1
 i4_(some_R_A) <= 1
 i4_(all_S_(not_A)) <= 1
 i4_(all_R_(not_A)) <= 1
 y1 <= 1
 a_(all_R_(all_R_(not_A))) <= 1
 a_(some_R_(some_R_A)) <= 1
Binaries
 i1_{_i1_} i2_{_i2_} i3_{_i3_} i4_{_i4_} y2
Semi-continuous
 a_A a_(some_S_A) a_(some_R_A) a_(all_S_(not_A)) a_(all_R_(not_A)) (a,i1)_S
 i1_A i1_(some_S_A) i1_(some_R_A) i1_(all_S_(not_A)) i1_(all_R_(not_A))
 (a,i2)_R i2_A i2_(some_S_A) i2_(some_R_A) i2_(all_S_(not_A))
 i2_(all_R_(not_A)) (i1,i3)_S i3_A i3_(some_S_A) i3_(some_R_A)
 i3_(all_S_(not_A)) i3_(all_R_(not_A)) (i1,i4)_R i4_A i4_(some_S_A)
 i4_(some_R_A) i4_(all_S_(not_A)) i4_(all_R_(not_A)) y1
 a_(all_R_(all_R_(not_A))) a_(some_R_(some_R_A))
End
