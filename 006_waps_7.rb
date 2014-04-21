#Given an array of number, which are perfect squares?
#this means you choose square numbers from the array

=begin
pay attention the range is not array! so the array = 1..16 cannot use array[1]
the array can do map select dircetirly and it can do some other things just like array can
=end

def gets_squares(array)
  array.select{ |i| Math.sqrt(i) % 1 == 0}.uniq.sort
end
# Math.sqrt() = i**0.5

#my solution :the answer is right but it is totally mass
#understand wrong not one by one but select
def get_squares(array)
  #Enter code here!
  arr = array.to_a.sort
  p array
  number = arr[-1]
  str = Array.new
  (1..number).map {|n| (arr.include?(n*n))&&(n*n <= number) ? str<<n*n :{}}
  str
end


p get_squares(1..2)
