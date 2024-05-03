'''
Module 1: This module provides a reusable byline for the author's services
'''

# Import Dependencies
import math
import statistics

def main():
    

    # Define Variables
    company_name:str = "Anjana Pharmacy Company"
    company_description:str = "Best Pharmacy in the Town"
    company_city:str = 'Winter Springs'
    company_state:str = 'Florida'
    company_rating: float = 4.6
    open_position:list = ["Pharmacist", "Customer Sevice", "Nurse"]
    salary_per_position: list = [45000, 35000, 65000]
    has_employee_benefits:bool = True
    employee_satisfaction_scores:list = [4.8, 4.6, 4.9, 5.0, 4.7]

# Multiline string with byline using f-string formatting
    byline: str = f"""
       About Anjana Company
    Name: {company_name}
    Description: {company_description}
    City: {company_city}
    State: {company_state}
    Rating: {company_rating}
    Job Position: {open_position}
    Salary: {salary_per_position}
    Employee Benefits: {has_employee_benefits}
    Employee Satisfaction:{employee_satisfaction_scores}

      About the Job 
    Highest salary pay: {max(salary_per_position)}
    Lowest salary pay: {min(salary_per_position)}
    Number of open position: {len(open_position)}
    Mean of employee satisfaction scores: {statistics.mean(employee_satisfaction_scores)}
    """

    print(byline)
   

# Call the main function to execute the code
if __name__ == '__main__':
    main()
