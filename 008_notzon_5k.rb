#Number of trailing zeros of N!
def zeros(n, pow = 5)
  pow <= n ? zero (n, pow*5) + (n/pow).floor : 0
end


def zeros(n)
  (1..Math.log(n,5)).reduce(0){|result, power| result + (n/5**power).to_i}
end
# fastest one

def zeros(n)
  zero = 0
  zeros += n /= 5 while n >= 1
  zeros
end


def zeros(n)
  (n/4.00000003).floor
end


def zero(n)
  i = 1
  result = 0
  while (n <= i ) do
    i *= 5
    result += n/i
  end
  result
end