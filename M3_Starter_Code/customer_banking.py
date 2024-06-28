# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("How much ya got? "))
    savings_interest_rate = float(input("Waas the interest? "))
    savings_months = int(input("How many moons has it been sittin? "))


    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your starting Savings Account balance was -> {savings_balance:.2f}.")
    print(f"After {savings_months} months at {savings_interest_rate} percent. ")
    print(f"Your intrest Will have Earned you -> {interest_earned:.2f}.")
    print(f"Your new Savings balance is -> {updated_savings_balance:.2f}.")
    
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Ya, got a CD and ya don't know what it is worth now? Let me help. How much did ya put in? "))
    cd_interest_rate = float(input("Do you remember the CD's interest rate? "))
    cd_months = int(input("How many months did you say it was in there? "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"CD Account -> {cd_balance:.2f}")
    print(f"Holding for {savings_months} months at {cd_interest_rate} percent. ")
    print(f"Your interest Earned will be -> {interest_earned:.2f}.")
    print(f"Well look at that you now have -> {updated_cd_balance:.2f}.")
if __name__ == "__main__":
    # Call the main function.
    main()