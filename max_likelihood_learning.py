import data_set as data

def calc_priors():
    good_days = 0;
    total = 0;
    for sample in data.data_set:
        if (sample.good_day):
            good_days += 1
        if (sample.good_day != None):
            total += 1
    prior_yes = float(good_days)/total
    prior_no = float(total-good_days)/total
    return (prior_yes, prior_no)

def calc_likelihoods():
    yes_cases = [x for x in data.data_set if x.good_day]
    no_cases = [x for x in data.data_set if (x.good_day == 0)]
    yes_count = len(yes_cases)
    no_count = len(no_cases)
    # add pseudocounts to avoid 0
    yes_count += 6
    no_count += 6
    yes_likelihoods = dict()
    no_likelihoods = dict()
    for field in data.field_names:
        yes_likelihoods[field] = [1.0 for x in range(0,6)] # one for pseudocount
        no_likelihoods[field] = [1.0 for x in range(0,6)] # one for pseudocount
    for x in yes_cases:
        index = 0
        for field in data.field_names:
            yes_likelihoods[field][x.data[index]-1] += 1
            index += 1
    for x in no_cases:
        index = 0
        for field in data.field_names:
            no_likelihoods[field][x.data[index]-1] += 1
            index += 1
    for field in data.field_names:
        for i in range(0,6):
            yes_likelihoods[field][i] = yes_likelihoods[field][i] / yes_count
            no_likelihoods[field][i] = no_likelihoods[field][i] / no_count
    return (yes_likelihoods, no_likelihoods)


(P_yes, P_no) = calc_priors() #P(yes) and P(no)

(P_x_given_yes, P_x_given_no) = calc_likelihoods() # [P(x_i | y=yes), P(x_i | y=no)]

print "Prior probabilities:\n yes: %.2f    no: %.2f" % (P_yes, P_no)
print "\n"
print "Likelihood:\n"
for field in data.field_names:
    print field
    print "1: %.2f(%.2f)    2: %.2f(%.2f)   3: %.2f(%.2f)   4: %.2f(%.2f)   5: %.2f(%.2f)   6: %.2f(%.2f)" % (P_x_given_yes[field][0],P_x_given_no[field][0],
    P_x_given_yes[field][1],P_x_given_no[field][1],
    P_x_given_yes[field][2],P_x_given_no[field][2],
    P_x_given_yes[field][3],P_x_given_no[field][3],
    P_x_given_yes[field][4],P_x_given_no[field][4],
    P_x_given_yes[field][5],P_x_given_no[field][5])


# Get user data
user_data = []
print "Rate the following from a scale 1 to 6, 1 being the worst and 6 the best!"
for field in data.field_names:
    print "Rate your %s\n" % field
    rating_input = raw_input("> ")
    try:
        rating = int(rating_input)
        if rating < 1 or rating > 6:
            raise ValueError("Wrong input")
        user_data.append(rating)
    except:
        print "Not a valid input!"
        exit(1)

print "\n"

y_map_yes = P_yes
y_map_no = P_no

data_index = 0
for field in data.field_names:
    y_map_yes *= P_x_given_yes[field][user_data[data_index]-1]
    y_map_no *= P_x_given_no[field][user_data[data_index]-1]
    data_index += 1

print "The AI gods have predicted.....(using MAP estimate on ML learning)"

if (y_map_yes > y_map_no):
    print "You are going to have a GOOD day!"
else:
    print "You are going to have a BAD day!"
