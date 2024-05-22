# import library
from tabulate import tabulate

#insert dummy data
data = {"Shandy" : ["Basic Plan", 12, "shandy-2134"],
       "Cahya" : ["Standard Plan", 24, "cahya-abcd"],
       "Ana" : ["Premium Plan", 5, "ana-2f9g"],
       "Bagus" : ["Basic Plan", 11, "bagus-9f92"]}

class User:
    def __init__(self, username, duration_plan, current_plan):
        self.username = username
        self.duration_plan = duration_plan
        self.current_plan = current_plan
        
    def check_benefit(self):
        """
        Function to show all Pacflix Subsription Benefit Table.
        """
        headers = ['Basic Plan', 'Standard Plan', 'Premium Plan', 'Services']
        
        table = [[True, True, True, 'Bisa Stream'],
               [True, True, True, 'Bisa Download'],
               [True, True, True, 'Kualitas SD'],
               [False, True, True, 'Kualitas HD'],
               [False, False, True, 'Kualitas UHD'],
               [1, 2, 4, 'Number of Devices'],
               ['3rd party Movie only', 'Basic Plan Content + Sports', 'Basic Plan + Standard Plan + PacFlix Original Series', 'Content'],
               [120_000, 160_000, 200_000, 'Price']]
        
        print("All PacFlix Subs List\n")
        print(tabulate(table, headers=headers, tablefmt='fancy_grid'))
        
    #User Subscription check
    def check_plan(self, username):
        """
        Function to show user's current plan and duration plan along with the benefit.
        
        Parameters
        ----------
        username: string
            input username
        """
        for key, value in data.items():
            if self.username == key:
                print(f"Username: {key}")
                print(f"Plan: {value[0]}")
                print(f"Duration Plan: {value[1]}")
                
                try:
                    if value[0] == 'Basic Plan':
                        table = [[True, 'Bisa Stream'],
                                [True, 'Bisa Download'],
                                [True, 'Kualitas SD'],
                                [False, 'Kualitas HD'],
                                [False, 'Kualitas UHD'],
                                [1, 'Number of Devices'],
                                ['3rd party Movie only', 'Content'],
                                [120_000, 'Price']]
                        headers = ['Basic Plan', 'Services']
                        print(f"{value[0]} Subscription Benefits\n")
                        print(tabulate(table, headers=headers, tablefmt='fancy_grid'))
                    elif value[0] == 'Standard Plan':
                        table = [[True, 'Bisa Stream'],
                                [True, 'Bisa Download'],
                                [True, 'Kualitas SD'],
                                [True, 'Kualitas HD'],
                                [False, 'Kualitas UHD'],
                                [2, 'Number of Devices'],
                                ['Basic Plan Content + Sports', 'Content'],
                                [160_000, 'Price']]
                        headers = ['Standard Plan', 'Services']
                        print(f"{value[0]} Subscription Benefits\n")
                        print(tabulate(table, headers=headers, tablefmt='fancy_grid'))
                    elif value[0] == 'Premium Plan':
                        table = [[True, 'Bisa Stream'],
                                [True, 'Bisa Download'],
                                [True, 'Kualitas SD'],
                                [True, 'Kualitas HD'],
                                [True, 'Kualitas UHD'],
                                [4, 'Number of Devices'],
                                ['Basic Plan + Standard Plan + PacFlix Original Series', 'Content'],
                                [200_000, 'Price']]
                        headers = ['Premium Plan', 'Services']
                        print(f"{value[0]} Subscription Benefits\n")
                        print(tabulate(table, headers=headers, tablefmt='fancy_grid'))
                except:
                    raise Exception("Subscription Plan does not exist")
    def upgrade_plan(self, username, current_plan, upgrade_plan):
        """
        Function to calculate final price if the user upgrades plan. User who have subscribed for more than 12 months will be given a discount. 
            total price = normal price - (normal price*0.05)
        
        Parameters
        ----------
        username: string
            input username
        current_plan: string
            Plan currently owned by existing user
        upgrade plan: string
            New plan selected by existing user
        """
        #Current Plan tier list
        if current_plan == 'Basic Plan':
            current_plan = 1
        elif current_plan == 'Standard Plan':
            current_plan = 2
        elif current_plan == 'Premium Plan':
            current_plan = 3
        
        #Upgraded Plan tier list + Price
        if upgrade_plan == 'Basic Plan':
            upgrade_plan = 1
            price = 120_000
        elif upgrade_plan == 'Standard Plan':
            upgrade_plan = 2 
            price = 160_000
        elif upgrade_plan == 'Premium Plan':
            upgrade_plan = 3
            price = 200_000
        
        try:
            if current_plan < upgrade_plan:
                
                if self.duration_plan > 12:
                    total = price - (price * 0.05)
                    print(f"Username: {self.username}")
                    print(f"Total Price: Rp {total}")
                else:
                    print(f"Username: {self.username}")
                    print("Duration Plan is less than 12 months")
                    print(f"Total Price: Rp {price}")
            elif current_plan == upgrade_plan:
                raise Exception("Upgrade Plan failed")
            else:
                raise Exception("Upgrade Plan failed. Unable to downgrade Plan")
        except:
            raise Exception("Error: Plan is not available.")
            
class NewUser:
    existing_referral_code = []
    def __init__(self, username):
        self.username = username
        
    def get_referral_code(self, data):
        """
        Function to get referral code from existing user.
        
        Parameters
        ----------
        data: dictionary
            existing PacFlix database
        
        Returns
        -------
        existing_referral_code: list
            List of referral code from database
        """
        for value in data.values():
            ref_code = value[2]
            self.existing_referral_code.append(ref_code)
        return self.existing_referral_code
    
    def pick_plan(self, new_plan, referral_code):
        """
        Function to calculate final discounted price for new user if the referral code is valid.
            total price = normal price - (normal price*0.04)
            
        Parameters
        ----------
        new_plan: String
            Plan chosen by new user
        referral_code: String
            Referral code entered by new user
            
        Returns
        -------
        total: Float
            Final price to be paid by new user
        """
        DISCOUNT = 0.04
        if referral_code in self.existing_referral_code:
            if new_plan == 'Basic Plan':
                total = 120_000 - (120_000*DISCOUNT)
                return total
            elif new_plan == 'Standard Plan':
                total = 160_000 - (160_000*DISCOUNT)
                return total
            elif new_plan == 'Premium Plan':
                total = 200_000 - (200_000*DISCOUNT)
                return total
            else:
                raise Exception("Plan is unavailable.")
        else:
            raise Exception("Referral Code invalid.")