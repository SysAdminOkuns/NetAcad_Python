from ast import literal_eval
# Let's create a variable named var = 1
# The following conditions are pairwise equivalent:
# understand priority hierarchy
# Unary operator not has higher priority than and,or
# and, or operator are binary operators where
# and operator higher priority than the or operator.

# Example 1:
var = 1
# print(var > 0)
# print(not (var > 0))

# Example 2:
# print(var != 0)
# print(not (var == 0))

# Example 3: De Morgan's laws
# The negation of a conjunction is the disjuction of the negations.
# The negation of a disjunction is the conjunction of the negations.

# p1, p2 = True, False
# q1, q2 = True, False
# 
# print(not (p1 and q1) == (not p1) or (not q2))
# print(not (p1 or q1) == (not p1) and (not q2))
#

# Example 4
# i = 1
# j = not not i
# print(j)

# j = "0X1234"
# scale = 16
# num_of_bits = 32
# # Expected output 00000000000000000001001000110100
# #print(bin(int(j, scale))[2:].zfill(num_of_bits))
# flag_register = bin(int(j, scale))[2:].zfill(num_of_bits)
# # print(flag_register)
# # bit masking meaning grabbing value or to change the selected bits called bit mask
# # 2 ^ 3 = 8
# the_mask = literal_eval("0x8")
# # flag_register &= the_mask
# print(flag_register, type(the_mask))

# Binary left shift and binary right shift.
# 17 >> 1 -> 17 // 2 (17 floor divided by 2 to the power of 1) -> 8
# (Shifting to the right by one bit is the same as integer division by two)
# 17 << 2 -> 17 * 4 ( 17 multiplied by 2 to the power of 2) -> 68
# (Shifting to the left by two bits is the same as integer multiplication by 4)
num = 17
right_shift_result = num >> 1
left_shift_result = num << 2
print(num, left_shift_result, right_shift_result)




