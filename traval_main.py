#import travel.thailand
#trip_to = travel.thailand.ThailandPackage()
#trip_to.detail()

#from travel.thailand import ThailandPackage as TP
#trip_to = TP()
#trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel import *
# try:
#     trip_to = vietnam.VietnamPackage()
#     trip_to.detail()
#     trip_to = thailand.ThailandPackage()
#     trip_to.detail()
# except NameError:
#     print("__init__.py 파일을 확인해보세요")

import inspect
import random
from travel import *
#print(inspect.getfile(vietnam))
#print(inspect.getfile(thailand))
