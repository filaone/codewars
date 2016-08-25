def search_substr( fullText, searchText, allowOverlap = true)
	if searchText == ''
		0
	else
		fullText.scan(allowOverlap ? Regexp.new("(?=(#{searchText}))") : searchText).size
	end
end

def search_substr(fullText, searchText, allowOverlap)
	return 0 if searchText.empty?
	count, offset = 0, 0
	while idx = fullText.index(searchText, offset)
		count += 1
		offset = idx + (allowOverlap ? 1 : searchText.length)
	end
	count
end


def search_substr(fullText, searchText, allowOverlap = true)
	searchText.empty? || fullText.empty? ? 0: fullText.scan(/#{searchText}#{'?' if allowOverlap}/).size
end








def search_substr(fullText,searchText, allowOverlap = true)
  total = 0
  if(!allowOverlap)
  total =  fullText.scan(/#{searchText}/).size
  else
#  (0..fullText.length).inject(0) { |total, i|
#    total +((fullText[i..-1]).index(/#{searchText}/).include(0))}
  all = (0..fullText.length).map{|i|
     (fullText[i..-1]).index(searchText)
   }
  total = all.count(0)
  if((total == fullText.length + 1) && (searchText == ''))
    total = 0
  else
    total
  end
 end
end
p search_substr('aa_bb_cc_dd_bb_e', 'bb', true)
p search_substr('aaabbbcccc', 'bbb') # should return 1
p search_substr( 'aaa', 'aa' ) # should return 2
p search_substr( 'aaa', '' ) # should return 0
p search_substr( 'aaa', 'aa', false) # should return 1






=begin
class String
  def all_subs substr, overlap = false
    return scan(substr) unless overlap
    (0...size).inject([]){ |r, i|
      p self
      r <<
        ( substr.match(self[i..-1])[0]  rescue nil )
    }.compact
  end
end


p "aaaaaaaa".all_subs( /aaa/ )
p "aaaabaaaa".all_subs( /aaa/, true )
=end