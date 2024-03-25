progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0

def loop(input_message, error_message): #loop to get the input(result) and print error messages
    while True:
        try:#handle the Value Error using try
            result = int(input(input_message))
        except ValueError:
            print(error_message)
            continue
        if result not in range(0, 121, 20):#to check the marks are in range
            print('Out of range.')
            continue
        else:
            return result#return the result value

while True:
    try:
        category = int(input('If you are a student press 1 or\nIf you are a Staff member press 2 to continue\n>>>>: '))
    except ValueError:
        print('Invalid input')
        continue
    if category == 1:
        while True:
            passs = loop('\nPlease enter your credits at pass : ',
                         'Integer required.')  # user define loop function to get input and print error message

            defer = loop('Please enter your credits at defer : ', 'Integer required.')

            fail = loop('Please enter your credits at fail : ', 'Integer required.')

            total = passs + defer + fail
            if total != 120:  # to check the total
                print('Total incorrect.')
                continue

            if passs == 120:
                progress_count += 1
                print('Progress')
                break
            elif fail >= 80:
                excluded_count += 1
                print('Exclude')
                break
            elif passs == 100:
                trailer_count += 1
                print('Progress(module trailer)')
                break
            elif fail <= 60:
                retriever_count += 1
                print('Do  not Progress-module retriever')
                break


    elif category == 2:
        while True:
            passs = loop('\nPlease enter your credits at pass : ',
                         'Integer required.')  # user define loop function to get input and print error message

            defer = loop('Please enter your credits at defer : ', 'Integer required.')

            fail = loop('Please enter your credits at fail : ', 'Integer required.')

            total = passs + defer + fail
            if total != 120:  # to check the total
                print('Total incorrect.')
                continue

            if passs == 120:
                progress_count += 1
                print('Progress')
            elif fail >= 80:
                excluded_count += 1
                print('Exclude')
            elif passs == 100:
                trailer_count += 1
                print('Progress(module trailer)')
            elif fail <= 60:
                retriever_count += 1
                print('Do  not Progress-module retriever')

            conti = str(input(
                '\nWould you like to enter another set of data? \nEnter "y" for yes or "q" to quit and view results : '))  # asking to continue or quit
            if conti.lower() == "y":  # to convert capital letters to simple letters and check the condition
                continue
            elif conti.lower() == "q":
                break

        print('\n-------------------------------------------------------------\nHistogram')  # Histogram and printing stars
        print('Progress ', progress_count, '  : ', progress_count * '*')
        print('Trailer ', trailer_count, '   : ', trailer_count * '*')
        print('Retriever ', retriever_count, ' : ', retriever_count * '*')
        print('Excluded ', excluded_count, '  : ', excluded_count * '*', '\n')

        total = progress_count + trailer_count + retriever_count + excluded_count  # addition of total outcomes
        print(total, 'outcomes in total.\n-------------------------------------------------------------')
    else:
        continue
    break