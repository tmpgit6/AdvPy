import greetings

greetings.greeting_de("Thomas")
greetings.greeting_fr("Thomas")
print(greetings.LOCATION)

#############################
# Alias (nickname)
import greetings as gt
gt.greeting_cn("Sven")
gt.LOCATION
#############################

from greetings import greeting_en, greeting_sp, LOCATION

greeting_en("Frank")
greeting_sp("Frank")

# ############



#############################
# With Alias
from greetings import greeting_en as gen, greeting_sp as gsp

gen("Julia")
gsp("Julia")


############################
from greetings import * 

greeting_fr("Lena")


print(LOCATION)