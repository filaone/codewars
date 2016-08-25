# ipv4 to int32
# it has some massive information,it is unnecessary to calculate 128.32.10.1 == 10000000.00100000.00001010.00000001

def ip_to_int32(ip)
  ("%02x%02x%02x%02x" % ip.split('.')).to_i(16)
# ("%08b%08b%08b%08b" % ip.split('.')).to_i(2)
end
# N进制转化为10进制的方法为：to_i(N)
# 2X进制可以很方便的转化，但是2X转化为其他进制比较难
# also can use map + join


def ip_to_int32(ip)
  ip.split('.').inject(0){|total, val|
    (total << 8) + val.to_i
  }
end
#<<移位

def ip_to_int32(ip)
  ip.split(".").map{ |octet| ("%08b" % octet.to_i) }.join.to_i(2)
end
 

def convert(ipv4)
  string = ipv4.split(/\./)
  sum = 0
  (0..3).map{|nu|
    sum = (string[nu].to_i * (2 ** (8*(3 - nu)))) + sum 
    
  }
 sum
end
