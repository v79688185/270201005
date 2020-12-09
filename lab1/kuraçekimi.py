import random
import time
second = 4
name_List = ["onurbaşıbüyük","oraz","emirsefer","deno","mevlüt","ahmet","ali","ege","burak","emrebeskan","rıfat","serhat"]
team_List = ["galatasaray","beşiktaş","fenerbahçe","trabzonspor","başakşehir","sivasspor","alanya","göztepe","kasımpaşa","antalyaspor","gençlerbirliği","konyaspor"]
while name_List >= [] and team_List >= []:
  name=random.choice(name_List)
  team=random.choice(team_List)
  name_List.remove(name)
  team_List.remove(team)
  time.sleep(second)
  print(name,"take")
  time.sleep(second)
  print(team)
  