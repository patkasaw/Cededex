class Restaurant:
  name = ''
  description = ''
  rating = 0.0
  deliver = False
  
bobs_burgers = Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.description = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.deliver = False

print(vars(bobs_burgers))
