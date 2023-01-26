def add_time(start, duration, day = ""):
  #get data from input adn cleanup
  startfix = start.replace(":"," ")
  h, m, oldap = startfix.split(" ")
  oldap = oldap.rstrip("M")
  addh, addm = duration.split(":")
  newap = oldap
  time = ""
  new_time = ""
  dayinfo = ""
  newday = ""

  #convert input strings into float, and then int
  h = int(float(h))
  m = int(float(m))
  addh = int(float(addh))
  addm = int(float(addm))

  newh = h
  newm = m
  #to count changes from PM to AM = day changes
  dtchng = 0
  #add duration to h and m, and count day changes
  for i in range(addh+1):
    if i == 0:
      newm += addm
      if newm >= 60:
        newh += 1
        newm -= 60
      if newh == 12:
        if oldap == 'A':
          newap = 'P'
          oldap = 'P'
        elif oldap == 'P':
          newap = 'A'
          oldap = 'A'
          dtchng += 1
      if newh > 12:
        newh -= 12           
      next
    else:
      newh += 1
      if newh == 12:
        if oldap == 'A':
          newap = 'P'
          oldap = 'P'
        elif oldap == 'P':
          newap = 'A'
          oldap = 'A'
          dtchng += 1
      if newh > 12:
        newh -= 12

  #get date (if applicable) and assign index per list below
  if day != "":
    userday = str(day).title()
    userday = userday.lstrip("('")
    userday = userday.rstrip("',)")
    wkdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    wkdayi = wkdays.index(userday)
    
    #if day included, and datechanged >1, change newday
    if dtchng > 0:
      wkdayi += dtchng
      if wkdayi > 6:
        wkdayi %= 7
    newday = ", " + wkdays[wkdayi]

  #default line that is printed in each usecase
  time = "{}:{:02d} {}M".format(newh, newm, newap)

  #format "days later" field if necessary
  if dtchng > 0:
    if dtchng == 1:
      dayinfo = " (next day)"
    else:
      dayinfo = " (" + str(dtchng) + " days later)"

  #new_time constructed from all 3 strings
  new_time = time + newday + dayinfo
  
  return new_time