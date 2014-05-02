def is_santa_clausable(obj)
  obj.respond_to?('say_ho_ho_ho')&& obj.respond_to?('distribute_gifts')&& obj.respond_to?('go_down_the_chimney')
end