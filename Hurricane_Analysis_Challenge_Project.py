# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
#print(damages)
updated_damages = []
def update_damages(some_input2): 

  for i in some_input2:
    if i == 'Damages not recorded':
      updated_damages.append(i)
    elif 'M' in i:
      updated_damages.append(float(i[:-1])*1000000)
    elif 'B' in i:
      updated_damages.append(float(i[:-1])*1000000000)
  return updated_damages

print(update_damages(damages))


# write your construct hurricane dictionary function here:
dictionary1 = {}
dictionary2 = {}

def construct_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):

  for i in range(len(names)):
    dictionary2 = {'Name': names[i], 
                   'Month': months[i], 
                   'Year': years[i], 
                   'Max Sustained Wind': max_sustained_winds[i], 
                   'Areas Affected': areas_affected[i], 
                   'Damage': updated_damages[i], 
                   'Deaths': deaths[i]}
    dictionary1[names[i]] = dictionary2

  return dictionary1

print(construct_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths))

# write your construct hurricane by year dictionary function here:

def hurricane_by_year(old_dictionary):
  hurricane_dictionary_year = {}
  current_year = []
  current_hurricane = {}
  for i in old_dictionary:
    current_hurricane = old_dictionary.get(i)
    current_year = current_hurricane.get('Year')
    if current_year not in hurricane_dictionary_year:
      hurricane_dictionary_year[current_year] = current_hurricane
  return hurricane_dictionary_year
print(hurricane_by_year(dictionary1))


# write your count affected areas function here:
dictionary3 = {}
def count_affected_areas(input_dictionary):
  for i in input_dictionary:
    current_hurricane = input_dictionary.get(i)
    current_area = current_hurricane.get('Areas Affected')
    for j in current_area:
     # print(j)
      if j not in dictionary3: 
        dictionary3[j] = 1
      elif j in dictionary3:
        dictionary3[j] += 1
  return dictionary3
print(count_affected_areas(dictionary1))

# write your find most affected area function here:
def most_affected_area(inputdict):
  count = 0
  mostaffected = ""
  for i in inputdict:
    if inputdict[i] > count:
      count = inputdict[i]
      mostaffected = i
  print("The most affected area is: " + mostaffected)
  print("This area was affected " + str(count) + " times.")
most_affected_area(dictionary3)

# write your greatest number of deaths function here:

def greatest_deaths(inputdict2):
  death_counter = 0 
  hurricane_most_deaths = ""
  for i in inputdict2:
    current_hurricane = inputdict2.get(i)
    current_deaths = current_hurricane.get('Deaths')
    if current_deaths > death_counter:
      death_counter = current_deaths
      hurricane_most_deaths = i
  print("The most deaths by hurricane was: " + str(death_counter))
  print("The hurricane thas caused the mosts deaths was: " + hurricane_most_deaths)
greatest_deaths(dictionary1)

# write your catgeorize by mortality function here:

def mortality_rating(inputdict3):
  mortality_dictionary = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for i in inputdict3:
    current_hurricane = inputdict3.get(i)
    current_deaths = current_hurricane.get('Deaths')
    if current_deaths == 0:
      mortality_dictionary[0].append(current_hurricane)
    elif current_deaths < 100:
      mortality_dictionary[1].append(current_hurricane)
    elif current_deaths < 500:
      mortality_dictionary[2].append(current_hurricane)
    elif current_deaths < 1000:
      mortality_dictionary[3].append(current_hurricane)
    elif current_deaths < 10000:
      mortality_dictionary[4].append(current_hurricane)
    elif current_deaths >= 10000:
      mortality_dictionary[5].append(current_hurricane)
  return mortality_dictionary
print(mortality_rating(dictionary1))

# write your greatest damage function here:

def greatest_damage(inputdict5):
  damage_counter = 0 
  hurricane_most_damage = ""
  for i in inputdict5:
    current_hurricane = inputdict5.get(i)
    current_damage = current_hurricane.get('Damage')
    if current_damage == "Damages not recorded":
      next
    elif current_damage > damage_counter:
      damage_counter = current_damage
      hurricane_most_damage = i
  print("The most damage by hurricane was: " + str(damage_counter))
  print("The hurricane thas caused the most damage was: " + hurricane_most_damage)
greatest_damage(dictionary1)

# write your catgeorize by damage function here:

def damages_rating(inputdict6):
  damages_dictionary = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for i in inputdict6:
    current_hurricane = inputdict6.get(i)
    current_damages = current_hurricane.get('Damage')
    if current_damages == 'Damages not recorded':
      next
    elif current_damages == 0:
      damages_dictionary[0].append(current_hurricane)
    elif current_damages < 100000000:
      damages_dictionary[1].append(current_hurricane)
    elif current_damages < 1000000000:
      damages_dictionary[2].append(current_hurricane)
    elif current_damages < 10000000000:
      damages_dictionary[3].append(current_hurricane)
    elif current_damages < 50000000000:
      damages_dictionary[4].append(current_hurricane)
    elif current_damages >= 50000000000:
      damages_dictionary[5].append(current_hurricane)
  return damages_dictionary
print(damages_rating(dictionary1))


