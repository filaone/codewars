class Student
  attr_reader :name
  attr_reader :fives
  attr_reader :tens
  attr_reader :twenties
  
  def initialize(name, fives, tens, twenties)
    @name = name
    @fives = fives
    @tens = tens
    @twenties = twenties
  end
end

def most_money(students)
  students.sort! do |a, b|
    (a.fives + a.tens * 2 + a.twenties * 4) <=> (b.fives + b.tens * 2 + b.twenties * 4)
  end
  if (students[0].fives + students[0].tens * 2 +students[0].twenties * 4) == (students[-1].fives + students[-1].tens * 2 + students[-1].twenties * 4)
     'all'
  else
    students[-1].name
  end
end


student_1 = Student.new('wang', 0, 0, 45)
student_2 = Student.new('hou', 0, 1, 300)
student_3 = Student.new('liu', 1, 0, 0)
students = [student_1, student_2, student_3]

#students.sort! do |a, b|
#  (b.fives + b.tens * 2 + b.twenties * 4) <=> (a.fives + a.tens * 2 + a.twenties * 4)
#end


#students[1].name
p most_money(students)