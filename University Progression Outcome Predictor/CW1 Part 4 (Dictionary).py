students = dict()

def loop(input_message, error_message):  # loop to get the input(result) and print error messages
    while True:
        try:
            mark = int(input(input_message))
        except ValueError:
            print(error_message)
            continue
        if mark not in range(0, 121, 20):
            print('Out of range.')
            continue
        else:
            return mark


while True:
    id = str(input('\nEnter the ID : '))
    if len(id) != 8:
        print('Invalid ID')
        continue
    else:
        passs = loop('\nPlease enter your credits at pass : ', 'Integer required.')

        defer = loop('Please enter your credits at defer : ', 'Integer required.')

        fail = loop('Please enter your credits at fail : ', 'Integer required.')

        total = passs + defer + fail
        if total != 120:  # to check the total
            print('Total incorrect.')
            continue
        elif passs == 120:
            result = ('progress -', (passs, defer, fail))
            print('Progress')
        elif fail >= 80:
            result = ('Exclude - ', (passs, defer, fail))
            print('Exclude')
        elif passs == 100:
            result = ('Progress(module trailer) - ', (passs, defer, fail))
            print('Progress(module trailer)')
        elif fail <= 60:
            result = ('Do  not Progress-module retriever - ', (passs, defer, fail))
            print('Do  not Progress-module retriever')

        students[id] = result

        conti = str(input('\nWould you like to enter another set of data? \nEnter "y" for yes or "q" to quit and view '
                          'results : '))  # asking to continue or quit
        if conti.lower() == "y":  # to convert capital letters to simple letters and check the condition
            continue
        elif conti.lower() == "q":
            break
print('Part 4:')
for id in students:
    print(f'{id} : {students[id][0]} {students[id][1][0]}, {students[id][1][1]}, {students[id][1][2]}', end=' ')