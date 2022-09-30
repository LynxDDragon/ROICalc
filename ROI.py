class User_info:
    def __init__(self,curr_user, name,property,income,investment,users_dict = {}):
        self.users_dict = users_dict
        self.name = name
        self.property = property
        self.income = income
        self.investment = investment
        self.curr_user = curr_user

        

    def get_user_info(self): ## get our information from user 

        self.name = input(str('Enter UserName: '))
        
        self.users_dict[self.name] = {}

        self.property = input(str('Enter your property: '))

        self.users_dict[self.name]['Properties'] = {}
        
        self.income = int(input('Enter your income: '))
            
        while True:
            ans = input(str('Do you have any other form of income? (y/n): '))
            if ans[0].lower() == 'y':
                self.income += int(input('What is your income: '))
            else:
                break
                 
        self.users_dict[self.name]['Income'] = self.income

        self.investment = int(input(f'What is your total investment on {self.property}?: '))
                    
        self.users_dict[self.name]['Properties'][self.property] = {'Total Investment': self.investment}

        self.curr_user =  self.users_dict[self.name]



    def calc(self):

        coc_roi = (self.income / self.investment) * 100

        print(f'The Cash on Cash ROI for {self.property} is: %{coc_roi}')
        
        self.users_dict[self.name]['Properties'][self.property]['ROI'] = coc_roi

    def create_property(self):
        print('Create your new property here!')
        new_prop = input(str('Enter your property name: '))
        new_prop_inv = int(input(f'What is your total investment on {new_prop}?: '))
        print(self.curr_user)
        coc1_roi = (self.curr_user['Income'] / new_prop_inv) * 100
        print(f'The Cash on Cash ROI for {new_prop} is: %{coc1_roi}')

        self.curr_user['Properties'][new_prop] = {'Total Investment': new_prop_inv}
        self.curr_user['Properties'][new_prop]['ROI'] = coc1_roi

    def show_portfolio(self):
        print('This is your current portfolio!')
        print(self.curr_user)

    def del_property(self):
        print(self.curr_user['Properties'])
        answe = input('which property would you like to delete?: ')
        del self.curr_user['Properties'][answe]
        print('Your current properties:')
        print(self.curr_user['Properties'])


    def show_curr(self):
        print(f'You are currently: {self.users_dict[self.name]}')

        

    def create_user(self):
        
        new_user = input(str('What is your name?: ')) 
    
        self.users_dict[new_user] = {}

        new_property = input(str('Enter your property name: '))

        self.users_dict[new_user]['Properties'] = {}
    
        new_income = int(input('What is your income: '))
        

        while True:
            ans = input(str('Do you have any other income? (y/n): '))
            if ans[0].lower() == 'y':
                new_income += int(input('What is your income: '))
                print(f'Your total income is: {new_income}')
            else:
                break
        
    
        self.users_dict[new_user]['Income'] = new_income

        new_investment = int(input(f'What is your total investment on {new_property}?: '))
        
        
        self.users_dict[new_user]['Properties'][new_property] = {'Total Investment': new_investment}


    def ch_user(self):
        print(self.users_dict)

        answer = input('Which user would you like to choose?: ')
        self.curr_user = self.users_dict[answer]
        self.name = answer

        







        
        


user_info = User_info(' ',' ',' ',' ',' ')




print('Welcome to our ROI')
user_info.get_user_info()
user_info.calc()







while True:

    print('What would you like to do?')
    user_info.show_curr()
    print('[1] Create Property - create a new property and see its ROI')
    print('[2] Delete Property ')
    print('[3] Portfolio')
    print('[4] Create User')
    print('[5] Switch Users')
    print('[0] Quit')

    user_ans = int(input('Enter your next move here: '))

    if user_ans == 0:
        print('Thank you for using our calculator today!')
        break

    elif user_ans == 1:
        user_info.create_property()

    elif user_ans == 2:
        user_info.del_property()
        

    elif user_ans == 3:
        user_info.show_portfolio()

    elif user_ans == 4:
        user_info.create_user()
        

    elif user_ans == 5:
        user_info.ch_user()