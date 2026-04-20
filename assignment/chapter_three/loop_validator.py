for i in range(2):
        value = int(input('enter an integer (-1 to break):   '))
        print('you entered: ', value)

        if value == -1:
                break
        else:
                print('the loop terminated without executing the break')
