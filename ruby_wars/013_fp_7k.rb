def solution(value)
  formatted = "%.2f" % value
  formatted.class #string! not number!
  formatted.to_f
end

# pay attention!!!! just
# "%.2f" % value return string not number!

def solution(value)
  value.round(2)
end

def solution(value)
  ("%0.2f" % value).to_f
end


p solution(2.333333)