import math
import random
 
# bool
t = lambda x : (lambda y: x)
f = lambda x : (lambda y: y)
 
if_then_else = lambda b : (lambda x : (lambda y : b(x)(y)))
 
bool_to_tf = lambda b : t if b else f
tf_to_bool = lambda b : if_then_else(b)(True)(False)
 
# ex
print("ex 1 : if then else")
print(if_then_else(t)(1)(2))
print()
# xe
 
# pair
pair = lambda x : (lambda y : (lambda b : b(x)(y)))
first = lambda p : p(t)
second = lambda p : p(f)
 
pair_to_str = lambda p : ("( " + str(first(p)) + ", " + str(second(p)) + " )")
 
# ex
print("ex 2 : pair")
print(pair_to_str(pair("one")("two")))
print()
# xe
 
# times
times = lambda n : (lambda x : (lambda f : f(times(n - 1)(x)(f)) if n > 0 else x))
 
inc = lambda x: x + 1
 
# ex
print("ex 3 : increment from 0 5 times")
print(times(5)(0)(inc))
print()
# xe
 
# 2d vector
vec2 = lambda x : (lambda y : pair(x)(y))
vec2_x = lambda v : first(v)
vec2_y = lambda v : second(v)
vec2_add = lambda v : (lambda w : vec2(vec2_x(v) + vec2_x(w))(vec2_y(v) + vec2_y(w)))
vec2_dot_prod = lambda v : (lambda w : (vec2_x(v) * vec2_x(w)) + (vec2_y(v) * vec2_y(w)))
 
vec2_to_str = lambda v : ("[ " + str(vec2_x(v)) + ", " + str(vec2_y(v)) + " ]")
 
a = vec2(2)(1)
b = vec2(3)(6)
 
c = vec2_add(a)(b)
 
# ex
print("ex 4 : vec 2")
print(vec2_to_str(c))
print()
# xe
 
# 2x2 matrix
mat22 = lambda a : (lambda b : (lambda c : (lambda d : (lambda f : f(a)(b)(c)(d)))))
mat22_11 = lambda m : m(lambda a : (lambda b : (lambda c : (lambda d : a))))
mat22_12 = lambda m : m(lambda a : (lambda b : (lambda c : (lambda d : b))))
mat22_21 = lambda m : m(lambda a : (lambda b : (lambda c : (lambda d : c))))
mat22_22 = lambda m : m(lambda a : (lambda b : (lambda c : (lambda d : d))))

# creating and applying a rotation matrix
mat22_make_rot = lambda t : mat22(math.cos(t))(-math.sin(t))(math.sin(t))(math.cos(t))
mul_vec2_mat22 = lambda m : (lambda v : vec2((vec2_x(v) * mat22_11(m)) + (vec2_y(v) * mat22_12(m)))((vec2_x(v) * mat22_21(m)) + (vec2_y(v) * mat22_22(m))))
 
mat22_to_str = lambda m : ("| " + str(mat22_11(m)) + " " + str(mat22_12(m)) + " |\n| " + str(mat22_21(m)) + " " + str(mat22_22(m)) + " |")
 
# ex
print("ex 5 : mat 2x2")
print(mat22_to_str(mat22(1)(2)(3)(4)))
print()
# xe
 
# 3d vectors
vec3 = lambda x : (lambda y : (lambda z : (lambda f : f(x)(y)(z))))
vec3_x = lambda v : v(lambda x : (lambda y : (lambda z : x)))
vec3_y = lambda v : v(lambda x : (lambda y : (lambda z : y)))
vec3_z = lambda v : v(lambda x : (lambda y : (lambda z : z)))
vec3_dot_prod = lambda v : (lambda w : (vec3_x(v) * vec3_x(w)) + (vec3_y(v) * vec3_y(w)) + (vec3_z(v) * vec3_z(w)))

vec3_scalar_mul = lambda v : (lambda s : vec3(vec3_x(v) * s)(vec3_y(v) * s)(vec3_z(v) * s))
vec3_add = lambda v : (lambda w : vec3(vec3_x(v) + vec3_x(w))(vec3_y(v) + vec3_y(w))(vec3_z(v) + vec3_z(w)))
vec3_sub = lambda v : (lambda w : vec3(vec3_x(v) - vec3_x(w))(vec3_y(v) - vec3_y(w))(vec3_z(v) - vec3_z(w)))
vec3_cross_prod = lambda v : (lambda w : vec3((vec3_y(v) * vec3_z(w)) - (vec3_z(v) * vec3_y(w)))((vec3_z(v) * vec3_x(w)) - (vec3_x(v) * vec3_z(w)))((vec3_x(v) * vec3_y(w)) - (vec3_y(v) * vec3_x(w))))
 
vec3_to_str = lambda v : ("[ " + str(vec3_x(v)) + ", " + str(vec3_y(v)) + ", " + str(vec3_z(v)) + " ]")
 
# ex
print("ex 6 : cross product between [ 0, 1, 0 ] and [ 1, 0, 0 ]")
print(vec3_to_str(vec3_cross_prod(vec3(0)(1)(0))(vec3(1)(0)(0))))
print()
# xe

# 3x3 matrix

mat33 = lambda a : (lambda b : (lambda c : (lambda d : (lambda e : (lambda f : (lambda g : (lambda h : (lambda i : vec3(vec3(a)(b)(c))(vec3(d)(e)(f))(vec3(g)(h)(i))))))))))

mat33_1 = lambda c : (vec3_x(c))
mat33_2 = lambda c : (vec3_y(c))
mat33_3 = lambda c : (vec3_z(c))
mat33__1 = lambda r : (vec3_x(r))
mat33__2 = lambda r : (vec3_y(r))
mat33__3 = lambda r : (vec3_z(r))

mat33_11 = lambda m : (mat33__1(mat33_1(m)))
mat33_12 = lambda m : (mat33__2(mat33_1(m)))
mat33_13 = lambda m : (mat33__3(mat33_1(m)))
mat33_21 = lambda m : (mat33__1(mat33_2(m)))
mat33_22 = lambda m : (mat33__2(mat33_2(m)))
mat33_23 = lambda m : (mat33__3(mat33_2(m)))
mat33_31 = lambda m : (mat33__1(mat33_3(m)))
mat33_32 = lambda m : (mat33__2(mat33_3(m)))
mat33_33 = lambda m : (mat33__3(mat33_3(m)))

mat33_make_rot_x = lambda t : mat33(1)(0)(0)(0)(math.cos(t))(-math.sin(t))(0)(math.sin(t))(math.cos(t))
mat33_make_rot_y = lambda t : mat33(math.cos(t))(0)(math.sin(t))(0)(1)(0)(-math.sin(t))(0)(math.cos(t))
mat33_make_rot_z = lambda t : mat33(math.cos(t))(-math.sin(t))(0)(math.sin(t))(math.cos(t))(0)(0)(0)(1)

mul_vec3_mat33 = lambda v : (lambda m : vec3(vec3_x(v) * mat33_11(m) + vec3_y(v) * mat33_12(m) + vec3_z(v) * mat33_13(m))(vec3_x(v) * mat33_21(m) + vec3_y(v) * mat33_22(m) + vec3_z(v) * mat33_23(m))(vec3_x(v) * mat33_31(m) + vec3_y(v) * mat33_32(m) + vec3_z(v) * mat33_33(m)))

# ex
print("ex 7 : rotating [ 1, 0, 0 ] with 3 3x3 matrices")
test1 = mul_vec3_mat33(vec3(1)(0)(0))(mat33_make_rot_x(math.pi))
test2 = mul_vec3_mat33(test1)(mat33_make_rot_y(math.pi))
test3 = mul_vec3_mat33(test2)(mat33_make_rot_z(math.pi))
print(vec3_to_str(test1))
print(vec3_to_str(test2))
print(vec3_to_str(test3))
print()
# xe

# ex
print("ex 8 : rotating [ 0, 1 ] using a matrix by pi and pi / 2 respectively")
print(vec2_to_str(mul_vec2_mat22(mat22_make_rot(math.pi))(vec2(0)(1))))
print(vec2_to_str(mul_vec2_mat22(mat22_make_rot(math.pi / 2))(vec2(0)(1))))
print()
# xe
 
# recursion
#Y = lambda f : (lambda x : f(x(x)))(lambda x : f(x(x))) !python evals in normal order so this overflows!
Y = lambda f : (lambda x : f(Y(f))(x)) # issue is the 1 arg!
 
for_n_ = lambda n : lambda f : (lambda i : f(i + 1) if i < n else i)
for_n = lambda n : Y(for_n_(n))(0)
 
# ex
print("ex 9 : for i = 0; i < 10; i++")
print(for_n(10))
print()
# xe
 
# arrays
#
# an array is a tree* of the form
# (1, (1, (1, ...)))
#
# / \
# 1 / \
#   1 / \
#     1 / \
#       1 iden
#
# *linked list and tree

iden = lambda x : x

arr = lambda i : (lambda c : (lambda o : pair(i)(arr(o(i))(c)(o)) if c(i) else iden))
arr_value = lambda v : pair(v)(iden)
arr_range = lambda m : (lambda n : arr(m)(lambda x : x <= n)(lambda x : x + 1))

arr_len_ = lambda a : (lambda i : arr_len_(second(a))(i + 1) if a != iden else i)
arr_len = lambda a : arr_len_(a)(0)

arr_to_str_ = lambda a : (lambda n : (lambda s : arr_to_str_(second(a))(n + 1)(s + (", "  if n > 0 else " ") + str(first(a))) if a != iden else s))
arr_to_str = lambda a : (arr_to_str_(a)(0)("[") + " ]")

arr_at = lambda a : (lambda n : arr_at(second(a))(n - 1) if n > 1 else first(a))
arr_to = lambda a : (lambda n : pair(first(a))(arr_to(second(a))(n - 1)) if n > 0 else iden)
arr_from = lambda a : (lambda n : arr_from(second(a))(n - 1) if n > 1 else a)

arr_prepend = lambda a : (lambda x : pair(x)(a))

arr_append = lambda a : (lambda b : pair(first(a))(arr_append(second(a))(b)) if a != iden else b)
arr_append_value = lambda a : (lambda v : arr_append(a)(arr_value(v)))

arr_insert_at = lambda a : (lambda n : (lambda x : arr_append(arr_append_value(arr_to(a)(n - 1))(x))(arr_from(a)(n))))

arr_filter = lambda a : (lambda b : (pair(first(a))(arr_filter(second(a))(b)) if b(first(a)) else arr_filter(second(a))(b)) if a != iden else iden)

arr_find_ = lambda a : (lambda b : (lambda i : (i if b(first(a)) else arr_find_(second(a))(b)(i + 1)) if a != iden else iden))
arr_find = lambda a : (lambda b : arr_find_(a)(b)(1))

arr_select_ = lambda a : (lambda b : (lambda i : (first(a) if b(first(a)) else arr_select_(second(a))(b)(i + 1)) if a != iden else iden))
arr_select = lambda a : (lambda b : arr_select_(a)(b)(1))

arr_find_all_ = lambda a : (lambda b : (lambda i : (pair(i)(arr_find_all_(second(a))(b)(i + 1)) if b(first(a)) else arr_find_all_(second(a))(b)(i + 1)) if a != iden else iden))
arr_find_all = lambda a : (lambda b : arr_find_all_(a)(b)(1))

foreach = lambda a : (lambda f : pair(f(first(a)))(foreach(second(a))(f)) if a != iden else iden)

# ex
print("ex 10 : create an array [ 1; 19 ]")
print(arr_to_str(arr_range(1)(19)))
print()
print("ex 11 : prepend, append, insert a zero into [ 1; 10 ]")
print(arr_to_str(arr_prepend(arr_range(1)(10))(0)))
print(arr_to_str(arr_append_value(arr_range(1)(10))(0)))
print(arr_to_str(arr_insert_at(arr_range(1)(10))(5)(0)))
print()
print("ex 12 : to, from, from to, to [ 1; 19 ]" )
print(arr_to_str(arr_to(arr_range(1)(19))(5)))
print(arr_to_str(arr_from(arr_range(1)(19))(5)))
print(arr_to_str(arr_to(arr_from(arr_range(1)(19))(5))(10)))
print()
print("ex 13 : filter all even elements from [ 1; 19 ]")
print(arr_to_str(arr_filter(arr_range(1)(19))(lambda x : x % 2 == 0)))
print()
print("ex 14 : get element 5 from [ 1; 19 ], find the index of the element equal to 10")
print(arr_at(arr_range(1)(19))(5))
print(arr_find(arr_range(1)(19))(lambda x : x == 10))
print()
print("ex 15 : generate an array of 101 1/0s, find all indexes of 1, get the length")
bin_arr = foreach(arr_range(1)(100))(lambda x : random.randint(0, 1))
test = arr_find_all(bin_arr)(lambda x : x == 1)
print(arr_to_str(bin_arr) + "\n" + arr_to_str(test) + "\n" + str(arr_len(test)))
print()
print("ex 16 : foreach angle in an array rotate a 2d vector by it using a 2x2 matrix")
print(arr_to_str(foreach(arr(0)(lambda x : x <= 3.14)(lambda x : x + 0.314))(lambda x : vec2_to_str(mul_vec2_mat22(mat22_make_rot(x))(vec2(0)(1))))))
print()
# xe

# dicts
#
#      / \
# (k, v) / \
#   (k, v) / \
#     (k, v) / \
#       (k, v) iden

dict_value = lambda k : lambda v : pair(pair(k)(v))(iden)

dict_prepend = lambda d : lambda v : arr_prepend(d)(v)
dict_append = lambda d : lambda v : arr_append(d)(v)

dict_to_str_ = lambda d : (lambda n : (lambda s : dict_to_str_(second(d))(n + 1)(s + (", "  if n > 0 else " ") + pair_to_str(first(d))) if d != iden else s))
dict_to_str = lambda d : (dict_to_str_(d)(0)("[") + " ]")

dict_find = lambda d : lambda k : second(arr_select(d)(lambda p : first(p) == k))

# ex
print("ex 17 : dicts")
my_dict = dict_append(dict_append(dict_value("name")("jeff"))(dict_value("occupation")("builder")))(dict_value("age")(32))
print(dict_to_str(my_dict))
print(dict_find(my_dict)("name"))
# xe
