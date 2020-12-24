from sample_madlibs import hp,code,hungergames,zombie
import random

if __name__ == "__main__":
    madlib_obj = random.choice([hp,code,hungergames,zombie])
    madlib_obj.madlib()