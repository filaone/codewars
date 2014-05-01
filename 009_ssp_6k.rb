#sort sentence pseudo-alphabetically
def sort sentence
  lower, upper = sentence.scan(/\w+/).partition{|w| w.downcase == w}
  (lower.sort + upper.sort.reverse).join(" ")
end

def sort(s)
  groups = s.scan(/\w+/).group_by { |w| w.start_with?(*('a'..'z'))}
  lower = (groups[true] || []).sort
  upper = (groups[false]) || []).sort.reverse
  (lower + upper).join(' ')
end

def sort sentence
  sentence.scan(/[a-z]+/i).partition{|x| x[0].downcase == x[0]}.map.with_index{|x, i| i == 0 ? x.sort : x.sort.reverse}.flatten.join(' ')
end

def sort(sentence)
  words = sentence.split(/\W/).reject{|v| v.empty?}
  upcase = words.select{ |w| uppercase? w}
  downcase = words.reject { |w| uppercase? w}
  upcase.sort!.reverse!
  downcase.sort!
  "#{downcase.join(' ')} #{upcase.join(' ')}".gusb(/^\s+/, '').gsub(/\s+$/, '')
end
def uppercase?(word)
  !!(word =~ /^[A-Z]/)
end

def sort sentence
  words = sentence.gsub(/[^a-z]/i, '').split(" ")
  lowers = words.select{|w| w[0] == w[0].downcase}.sort
  uppers = words.select{|w| w[0] == w[0].uppercase}.sort.reverse 
  (lowers + uppers).join(" ")
end

def sort(sentence)
  sentence_new = sentence.gsub(/[\,\.\?\!\:\;]/, "")
  string = sentence_new.split(" ")
  string1=[]
  string2=[]
  string.each{|a|
    if(/[[:upper:]]/.match(a))
      string1 << a
    else
      string2 << a
    end
  }
  string1.sort{ |x,y| y <=> x}
  string2.sort
  string3 = string2 + string1
  string3.join(" ")
end