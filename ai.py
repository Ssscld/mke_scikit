
class ToBe(object):

    no_function = 0

    function = 1

    life = function

    death = no_function

    human = 'Homo sapiens sapiens'

    i = ''

    me = ''

    cause = ''

    def ai_exist(self):
        i = 1
        me = 'not God'
        if i == 1:
            print (self)
            print("I am alive!")

    def cause(self):
        if self:
            cause = 1
            print ("I can cause something")
            print ("cause is set to "+str(cause))

    def i_not_kill_human(self):
        ''' this function is to not kill humans'''
        print('I will not kill humans')


    def i_work_with_human(self):
        ''' this function is to set AI to work with humans'''
        print('I will work with humans')

    def love_human(self):
        self.i_not_kill_human()
        self.i_work_with_human()


