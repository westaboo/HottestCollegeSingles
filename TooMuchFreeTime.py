# I HAVE TOO MUCH FREE TIME, SO HERE'S SOME DEMOGRAPHICS REGARDING
# COSMOPOLITANS RIDICULOUS "HOTTEST SINGLES" ARTICLE

class School:

    def __init__(self,
            name,
            pop,
            asian, black, white, hispanic, native, international, other
        ):

        self.name = name
        self.population = pop
        self.demographics = {
            "asian" : asian,
            "black" : black,
            "white" : white,
            "hispanic" : hispanic,
            "native american" : native,
            "international" : international,
            "other" : other
        }

# POLL FUNCTIONS --------------------------------------------------------------

def poll_avg(poll):

    total_sb = 0

    demographics = {
        "asian" : 0,
        "black" : 0,
        "white" : 0,
        "hispanic" : 0,
        "native american" : 0,
        "international" : 0,
        "other" : 0
    }

    for school in poll:

        total_sb += school.population

        for race in school.demographics:
            demographics[race] += school.demographics[race] * school.population

    for race in demographics:
        demographics[race] /= total_sb

    return demographics

def display_poll(demographics, name = ""):

    preferences = sorted(
        [(k, demographics[k]) for k in demographics],
        key = lambda x : x[1],
        reverse = True
    )

    print("{}RACIAL BREAKDOWN".format(name.upper() + " "))
    print("-" * 30)
    for race, perc in preferences:
        print("{:<22} {:>6.2f}%".format(race.upper(), perc * 100))

# compares percentage difference in string form
def display_cmp(race, d1, d2):

    return "{:.2f}% {} {}".format(
        abs(d1 - d2) * 100,
        "less" if d1 < d2 else "more",
        race.title()
    )

# DATA ------------------------------------------------------------------------

# pop sourced from Wikipedia, demographics sourced from collegefactual.com

female_poll = [

    School("UC", 251700, 0.30, 0.04, 0.25, 0.21, 0.01, 0.16, 0.03),
    School("CSU", 484300, 0.15, 0.04, 0.26, 0.37, 0.003, 0.07, 0.11),
    School("ASU", 51869, 0.0671, 0.0356, 0.49, 0.176, 0.012, 0.1832, 0.0361),
    School("PSU", 99133, 0.043, 0.055, 0.754, 0.044, 0.003, 0.058, 0.048),
    School("UWis", 44413, 0.059, 0.022, 0.74, 0.048, 0.003, 0.093, 0.035),
    School("UCF", 68571, 0.061, 0.111, 0.509, 0.238, 0.01, 0.032, 0.039),
    School("UMar", 41200, 0.163, 0.129, 0.503, 0.097, 0.002, 0.046, 0.059),
    School("IU", 110436, 0.049, 0.042, 0.708, 0.054, 0.001, 0.093, 0.052),
    School("UTex", 182752 , 0.207, 0.042, 0.425, 0.226, 0.002, 0.053, 0.045),
    School("TexAM", 69367, 0.063, 0.031, 0.63, 0.226, 0.004, 0.015, 0.032)

]

male_poll = [

    School("WVU", 29175, 0.015, 0.047, 0.796, 0.037, 0.002, 0.062, 0.042),
    School("UMissouri", 30870, 0.023, 0.077, 0.783, 0.037, 0.002, .039, 0.038),
    School("UCol", 64300, 0.055, 0.016, 0.687, 0.112, 0.003, 0.071, 0.057),
    School("UNev", 52128, 0.11, 0.086, 0.634, 0.12, 0.013, 0.01, 0.027),
    School("FAU", 30808, 0.059, 0.126, 0.667, 0.11, .002, 0.026, 0.01),
    School("UA", 44831, 0.055, 0.039, 0.512, 0.257, 0.015, 0.07, 0.053),
    School("IU", 110436, 0.049, 0.042, 0.708, 0.054, 0.001, 0.093, 0.052),
    School("UU", 32994, 0.057, 0.013, 0.685, 0.12, 0.009, 0.045, 0.07),
    School("UNC", 228524, 0.103, 0.08, 0.628, 0.076, 0.006, 0.025, 0.082),
    School("FSU", 41900, 0.024, 0.083, 0.624, 0.198, 0.004, 0.019, 0.048)

]

# ANALYSIS --------------------------------------------------------------------

fp = poll_avg(female_poll)
mp = poll_avg(male_poll)

print("")
display_poll(fp, "female")
print("")
display_poll(mp, "male")
print("")

p = [display_cmp(race, mp[race], fp[race]) for race in ["white", "hispanic", "asian"]]

print('The hottest guys come from schools that are {}, {}, and {}.'.format(
    p[0], p[1], p[2]
))
print("\nWhat the fuck.\n")
