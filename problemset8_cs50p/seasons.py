from datetime import date
import re
import sys
import inflect

class Date:
    def __init__(self,birth,d):
        self.birthdate=birth
        self.today=d

    @classmethod
    def get_birth(cls,birth):
        if matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})$",birth):
            d=date.today()
            year=int(matches.group(1))
            month=int(matches.group(2))
            day=int(matches.group(3))
            try:
                birth=date(year,month,day)
                return cls(birth,d)
            except ValueError:
                sys.exit("Invalid Date")
        else:
            sys.exit("Invalid Date")

    def __sub__(self, other):
        difference = self.today - other.birthdate
        minutes=difference.days*24*60
        return minutes

def main():
    p=inflect.engine()
    b=input("Date of Birth:")
    dt=Date.get_birth(b)
    d3=dt-dt
    print(p.number_to_words(d3,andword=" "))

if __name__ == "__main__":
    main()