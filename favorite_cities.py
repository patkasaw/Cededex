class City: 
  def __init__(self, name ,country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

london = City('London', 'UK', 9748000, 'Tower of London') 
gdynia = City('Gdynia', 'Poland', 100000, 'bulwar')

print(vars(london))
print(vars(gdynia))