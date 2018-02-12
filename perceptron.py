import data_set as data
import numpy as np

def classify(weights, x):
    return np.sign(sum([a*b for a,b in zip(weights, x)]))

training_iterations = 1000
etha = 0.1

weights = [0.0 for x in range(0,5)]
weights_delta = [0.0 for x in range(0,5)]

for i in range(0, training_iterations):
    for j in range(0,len(data.data_set)):
        x = list(data.data_set[j].data)
        x.insert(0,-1)
        classified = classify(weights, x)
        t = 0
        if(data.data_set[j].good_day):
            t = 1
        else:
            t = -1
        if (classified != t):
            # was wrong
            w_t_x = sum([a*b for a,b in zip(weights, x)])
            for k in range(0,5):
                weights[k] += etha*(t-classified)*x[k]
                weights_delta[k] += etha*(t-w_t_x)*x[k]

print weights
print weights_delta
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

user_data.insert(0,-1)

predicted = classify(weights, user_data)
predicted_delta = classify(weights_delta, user_data)



print "The AI gods have predicted.....(using PERCEPTRON)"

if (predicted == 1):
    print "You are going to have a GOOD day!"
else:
    print "You are going to have a BAD day!"

print "The AI gods have predicted.....(using PERCEPTRON with DELTA)"

if (predicted_delta == 1):
    print "You are going to have a GOOD day!"
else:
    print "You are going to have a BAD day!"
