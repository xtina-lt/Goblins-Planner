#open store needs to make space for gamers to rent tables.
#favorit game is abruptly goblins

#list for gamers attending
gamers = []
#create a funciton to add gamer
def add_gamer(gamer):
    if gamer.get('name') and gamer.get('avail'):
        gamers.append(gamer)
    else:
        print('Gamer info missing')
        
#add kimberly
kimberly = {
    'name': 'Kimberly Warner',
    'avail': ['Monday', 'Tuesday', 'Friday']
}
add_gamer(kimberly)
add_gamer({'name':'Thomas Nelson','avail': ["Tuesday", "Thursday", "Saturday"]})
add_gamer({'name':'Joyce Sellers','avail': ["Monday", "Wednesday", "Friday", "Saturday"]})
add_gamer({'name':'Michelle Reyes','avail': ["Wednesday", "Thursday", "Sunday"]})
add_gamer({'name':'Stephen Adams','avail': ["Thursday", "Saturday"]})
add_gamer({'name': 'Joanne Lynn', 'avail': ["Monday", "Thursday"]})
add_gamer({'name':'Latasha Bryan','avail': ["Monday", "Sunday"]})
add_gamer({'name':'Crystal Brewer','avail': ["Thursday", "Friday", "Saturday"]})
add_gamer({'name':'James Barnes Jr.','avail': ["Tuesday", "Wednesday", "Thursday", "Sunday"]})
add_gamer({'name':'Michel Trujillo','avail': ["Monday", "Tuesday", "Wednesday"]})

'''Find the most available'''          
#create a table
def buidaily_table():
    return {
        "Monday":    0,
        "Tuesday":   0,
        "Wednesday": 0,
        "Thursday":  0,
        "Friday":    0,
        "Saturday":  0,
        "Sunday":    0,
    }
#name the table
count_availability = buidaily_table()

#create a function to update table
def get_avail(x):
    # for i in range(len(gamers)):
    #     for j in gamers[i].get('avail'):
            # count_availability[j] += 1
    for i in x:
        for j in i.get('avail'):
            count_availability[j] += 1


'''Get the day / find who is available on said day.'''
def find_best(x):
    most = 0;
    best_day = ""
    for k, v in x.items():
        if v > most:
            most = v
            best_day = k
    return best_day

def find_avail(x):
    list = []
    for i in gamers:
        for j in i.get('avail'):
            if j == x:
                list.append(i.get('name'))
    return list

'''Let's get printing'''
def play():
    #pass in a gamers list to build a table
    get_avail(gamers)
    best_day = find_best(count_availability)
    list_avail_on_day = find_avail(best_day)
    for i in list_avail_on_day:
        print(f'''Dear {i},
        Santa's Game House is planning to host a game day for Abrutly Goblibs.
        We would love for you to attend {best_day}
        Extra candy canes for Elves in pajamas!
        ''')
    return print('Happy Gaming and Merry Christmas')

play()


####################################
#        WHAT DO I PRINT?          #
####################################
# Dear Thomas Nelson,
#         Santa's Game House is planning to host a game day for Abrutly Goblibs.       
#         We would love for you to attend Thursday
#         Extra candy canes for Elves in pajamas!

# Dear Michelle Reyes,
#         Santa's Game House is planning to host a game day for Abrutly Goblibs.       
#         We would love for you to attend Thursday
#         Extra candy canes for Elves in pajamas!

# Dear Stephen Adams,
#         Santa's Game House is planning to host a game day for Abrutly Goblibs.       
#         We would love for you to attend Thursday
#         Extra candy canes for Elves in pajamas!

# Dear Joanne Lynn,
#         Santa's Game House is planning to host a game day for Abrutly Goblibs.       
#         We would love for you to attend Thursday
#         Extra candy canes for Elves in pajamas!

# Dear Crystal Brewer,
#         Santa's Game House is planning to host a game day for Abrutly Goblibs.       
#         We would love for you to attend Thursday
#         Extra candy canes for Elves in pajamas!

# Dear James Barnes Jr.,
#         Santa's Game House is planning to host a game day for Abrutly Goblibs.       
#         We would love for you to attend Thursday
#         Extra candy canes for Elves in pajamas!

# Happy Gaming and Merry Christmas