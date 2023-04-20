'''7.Write a shutting down program:
First, def a function, shut_down, that takes one argument s. Then, if the shut_down function receives
an s equal to "yes", it should return "Shutting down" Alternatively, elif s is equal to "no", then the
function should return "Shutdown aborted". Finally, if shut_down gets anything other than those inputs,
the function should return "Sorry".'''
string=input('Enter yes for shutdown, no for shutdown aborted and others for sorry:')
def shut_down(s):
        if string=='yes':
            print('shutdown')
        elif string=='no':
            print('shutdownaborted')
        elif string=='sorry':
            print('inavalid input')
        return string
shut_down(string)
