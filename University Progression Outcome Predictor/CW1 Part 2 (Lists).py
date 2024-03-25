progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0
progress = []
excluded = []
trailer = []
retriever = []
a_list = []
b_list = []
c_list = []
d_list = []


def loop(input_message, error_message):  # loop to get the input(result) and print error messages
    while True:
        try:
            result = int(input(input_message))
        except ValueError:
            print(error_message)
            continue
        if result not in range(0, 121, 20):
            print('Out of range.')
            continue
        else:
            return result

def star_print(message, count):
    print(message, count, ' : ', count * '*')

def remove_brackets(result, str_result):
    for elements in result:
        print(str_result, str(elements).replace('[', '').replace(']', ''))

while True:
    passs = loop('\nPlease enter your credits at pass : ', 'Integer required.')

    defer = loop('Please enter your credits at defer : ', 'Integer required.')

    fail = loop('Please enter your credits at fail : ', 'Integer required.')

    total = passs + defer + fail
    if total != 120:  # to check the total
        print('Total incorrect.')
        continue

    if passs == 120:
        progress_count += 1
        a_list.append(passs)
        a_list.append(defer)
        a_list.append(fail)
        progress.append(a_list)
        a_list = []
        print('Progress')
    elif fail >= 80:
        excluded_count += 1
        b_list.append(passs)
        b_list.append(defer)
        b_list.append(fail)
        excluded.append(b_list)
        b_list = []
        print('Exclude')
    elif passs == 100:
        trailer_count += 1
        c_list.append(passs)
        c_list.append(defer)
        c_list.append(fail)
        trailer.append(c_list)
        c_list = []
        print('Progress(module trailer)')
    elif fail <= 60:
        retriever_count += 1
        d_list.append(passs)
        d_list.append(defer)
        d_list.append(fail)
        retriever.append(d_list)
        d_list = []
        print('Do  not Progress-module retriever')

    conti = str(input(
        '\nWould you like to enter another set of data? \nEnter "y" for yes or "q" to quit and view results : '))  # asking to continue or quit
    if conti.lower() == "y":  # to convert capital letters to simple letters and check the condition
        continue
    elif conti.lower() == "q":
        break

print('\n-------------------------------------------------------------\nHistogram')  # Histogram and printing stars

star_print('Progress ', progress_count)
star_print('Trailer ', trailer_count)
star_print('Retriever ', retriever_count)
star_print('Excluded ', excluded_count)
print()

total = progress_count + trailer_count + retriever_count + excluded_count  # addition of total outcomes
print(total, 'outcomes in total.\n-------------------------------------------------------------\n')

print('Part 2:')
remove_brackets(progress, 'Progress -')
remove_brackets(trailer, 'Progress (module trailer) - ')
remove_brackets(retriever, 'Module Retriever -')
remove_brackets(excluded, 'Excluded -')