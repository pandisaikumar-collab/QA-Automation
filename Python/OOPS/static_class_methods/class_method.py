"""
> A class method works with class level data,
> uses cls
> works on class variables
> called using class name
"""
class Company:
    company_name = "RR"
    @classmethod
    def show_company(cls):
        print(cls.company_name)

Company.show_company()
