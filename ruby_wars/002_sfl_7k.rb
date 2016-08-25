#search for letters
def change(word)
  # put your code here!
  arr = Array.new(26, '0')
  #arr = [0] * 26
  str = word.downcase
  str.each_byte{|byte|   #this byte can be replace by |c| or other variable
    if ((byte<=122)&&(byte>=97))
      arr[byte-97] = 1
    end
    #if can not have {} here!!
   }
  return arr.join
  #doesn't need to use return it can be automatically
  # it is shortcut of  arr.join("") because there is no separte code in "" 
end


def change_2(word)
  (”a”..“z“).map {|v| word.downcase.include?(v) ? '1' : '0'}.join
end


def change_3(word)
  0.upto(25).map { |v| word.index(('a'.ord + i).chr).nil? ? 0 : 1}.join
  #'a'.ord can get its ascii value
end

def change_4(word)
  '%026b' % (a.each_byte.reduce(0)) { |m, c| m | (1 << 122 - (c | 32))} & ~(-1 << 26)
end
#这种印出方式参见
#puts "He's %d inches tall." % my_height    has 'sapce' between '%' and my_height