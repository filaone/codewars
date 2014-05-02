def solution(pairs)
  p
 # pairs.map{|name, value| '#{name} = #{value}'}.join(",")
 pairs.map{|a| a.join(" = ")}.join(",")
end
p solution({:a=>1, :b=>'2'})