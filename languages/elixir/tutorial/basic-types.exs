# Basic arithmetic
1 + 2
10 / 2
div(10, 2)
div 10, 2
rem 10, 3
0b1010
0o777
0x1F
1.0
1.0e-10
round(3.58)
trunc(3.58)

# Identifying functions and documentation
# iex> h round/1

# Booleans
true
true == false
is_boolean(true)
is_boolean(1)

# Atoms
:apple
:apple == :apple    # true
:apple == :orange   # false
true == :true       # true
is_atom(false)      # true
is_boolean(:false)  # true
is_atom(Hello)      # alias

# Strings
"hellö"
"hellö #{:world}"   # interpolation
"hello
...> world"
"hello\nworld"
IO.puts "hello\nworld"
is_binary("hellö")
byte_size("hellö")
String.length("hellö")
String.upcase("hellö")

# Anonymus functions
add = fn a, b -> a + b end
add.(1, 2)
is_function(add)
is_function(add, 2)
is_function(add, 1)
double = fn a -> add.(a, a) end
double.(2)
x = 42
(fn -> x = 0 end).()
x

# Lists (linked)
[1, 2, true, 3]
length [1, 2, 3]
[1, 2, 3] ++ [4, 5, 6]  # concat
[1, true, 2, false, 3, true] -- [true, false]   # subtract
list = [1, 2, 3]
hd(list)
tl(list)
# iex> i 'hello'        --> information
'hello' == "hello"  # false

# Tuples (stored contiguously)
{:ok, "hello"}
tuple_size {:ok, "hello"}
tuple = {:ok, "hello"}
elem(tuple, 1)      # "hello"
tuple_size(tuple)   # 2
put_elem(tuple, 1, "world")     # {:ok, "world"}, returns new, immutable

File.read("path/to/existing/file")      # {:ok, "... contents ..."}
File.read("path/to/unknown/file")       # {:error, :enoent}
