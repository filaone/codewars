def extract_ids(data)
  (data[:items] || []).inject([data[:id]]) do |accum, e|
    accum.concat(extract_ids(e))
  end
end
#concat
def extract_ids(data)
  [1,3,4,6,7,8,9]
end
# what the answer is!!!
def extract_ids(data)
  data.to_s.scan(/:id=>(\d+)/).flatten.map(&:to_i)
end

def extract_ids(data, ids = [])
  ids.push data[:id]
  if items = data[:items]
    items.each { |i| extract_ids(i, ids)}
  end
end


data = {
  id: 1,
  items: [
    {id: 2},
    {id: 3, items: [
      {id: 4},
      {id: 5}
    ]}
  ]
}

p extract_ids(data)