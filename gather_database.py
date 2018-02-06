import MySQLdb
import time

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","GoodDay" )
# prepare a cursor object using cursor() method
cursor = db.cursor()

# Login as user
user_input = raw_input("Whos this?\n> ")
user_input_char = '?'

if len(user_input) == 1:
    user_input_char = user_input[0]

get_user_sql = "SELECT user_id, current_data FROM user WHERE  " \
    "lower_char = \'%c\' OR upper_char = \'%c\'" \
    "OR first_name = \"%s\" OR last_name = \"%s\"" % (user_input_char, user_input_char, user_input, user_input)

#Find user_id in database
user_id = 0
user_current_data = 0
try:
    # Execute the SQL command
    cursor.execute(get_user_sql)
    (user_id, user_current_data) = cursor.fetchone()
except:
    print "no such user"
    # Rollback in case there is any error
    db.rollback()
    db.close()
    exit(0)

# if user_current_data != null the user has to put in info about their day.
# Else a new day was started
if user_current_data:
    # Find the date of the day.
    which_day = ""
    try:
        which_day_sql = "SELECT which_day FROM DATA WHERE data_id = %d" % user_current_data
        cursor.execute(which_day_sql)
        which_day = cursor.fetchone()[0]
    except:
        print "could not find day"
        db.rollback()
        db.close()
        exit(0)

    #prompt user
    good_day_input = raw_input("Did you have a good day on "+ str(which_day) + "? y/n\n> ")
    good_day_input = good_day_input[0].lower()
    if good_day_input[0] != 'y' and good_day_input[0] != 'n':
        print "Not a valid input for good day... type y or n!"
        good_day_input = raw_input("Did you have a good day? y/n\n> ")
        if good_day_input[0] != 'y' and good_day_input[0] != 'n':
            print "Comon dude..."
            exit(0)

    #Update database
    update_data_sql = ""
    update_user_sql = "UPDATE user SET current_data = NULL WHERE user_id = %d" % user_id
    if (good_day_input == 'y'):
        update_data_sql = "UPDATE data SET good_day = TRUE WHERE data_id = %d" % user_current_data
    else:
        update_data_sql = "UPDATE data SET good_day = FALSE WHERE data_id = %d" % user_current_data

    try:
        cursor.execute(update_data_sql)
        cursor.execute(update_user_sql)
        db.commit()
    except:
        print "something went wrong trying to update data"
        db.rollback()
        db.close()
        exit(1)

    print "Thank you for adding info about how your day was!"

else:
    # Get date
    which_day = time.strftime("%Y-%m-%d")
    # Get data field names
    field_names_sql = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME=\'data\'"
    cursor.execute(field_names_sql)
    field_names_unformated = cursor.fetchall()
    field_names = []
    for i in field_names_unformated:
        field_names.append(i[0])
    field_names = field_names[2:len(field_names)-1]

    #Get user data
    data = []
    print "Rate the following from a scale 1 to 5, 1 being the worst and 5 the best!"
    for field in field_names:
        print "Rate your %s\n" % field
        rating_input = raw_input("> ")
        try:
            rating = int(rating_input)
            if rating < 1 or rating > 5:
                raise ValueError("Wrong input")
            data.append(rating)
        except:
            print "Not a valid input!"
            db.close()
            exit(1)

    #build sql put string
    insert_sql = "INSERT INTO data(which_day, "
    for i in field_names:
        insert_sql += i + ", "
    insert_sql = insert_sql[:len(insert_sql)-2] + ") VALUES (\'" + which_day + "\', "
    for i in data:
        insert_sql += str(i) + ", "
    insert_sql = insert_sql[:len(insert_sql)-2] + ")"

    try:
        cursor.execute(insert_sql)
        user_current_data = cursor.lastrowid
        update_user_sql = "UPDATE USER SET current_data = %d WHERE user_id = %d" % (user_current_data, user_id)
        cursor.execute(update_user_sql)
        db.commit()
    except:
        print "Something went wrong tyring to add new data"
        db.rollback()
        db.close()
        exit(1)
    print "Thank you for adding info about your day!"

print "DONE"
db.close()
