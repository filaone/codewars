#sort for gift code
def sort_gift_code code
  #TODO
  ('a'..'z').map {|letter| code.include?(letter) ? letter : ''}.join
end


def sort_gift_code code
  code.chars.sort.join
  #code.split('').sort.join
end
# string#chars return an array of characters in str
# Array#sort can sort it then use the join to connect them
#you can use split('') to separte them

