#padded numbers
def solution(value)
  "Value is %.5d" % value
  # "Value is %05d" % [value]
  sprintf "Value is %05d", value
  # we should use sprintf to get the 00005
end