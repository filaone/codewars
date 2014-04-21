#remove odd hashes
def remove_odd_hashes(array, key_1, key_2)
  array.delete_if{|x| (x[key_1] + x[key_2]).odd? }
end
#there is an interator delete_if!

def remove_odd_hashes(array, key_1, key_2)
  array.delete_if{|x| x.values.inject(:+).odd?}
end

def remove_odd_hashes(array, key_1, key_2)
  array.reject {|h| (h[key_1] + h[key_2]).odd? }
end

def remove_odd_hashes(array, key_1, key_2)
  array.select do |x|
    (x[key_1] + x[key_2]).even?
  end
end

# may be error
def remove_odd_hashes(array, key_1, key_2)
  #you can check for "%" operator
  array.map{ |hashes| ((hashes[key_1] + hashes[key_2])%2 != 0) ? array.delete(hashes) : {} }
  return array
end
#pay attention 1.9.2 cannot do an array with only one variable
#!!!!!expect [] but it return [ {a: 3, b: 4} ]!!!


def remove_odd_hashes_2(array, key_1, key_2)
  array2 = []
  array.map{ |hashes| ((hashes[key_1] + hashes[key_2]) % 2 != 0) ? array2.push(hashes) : {}}
  array2
end


p remove_odd_hashes( 
  [ {a: 3, b: 4} ],  :a, :b)