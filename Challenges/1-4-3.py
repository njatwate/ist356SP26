from datetime import datetime #Imports datetime module to be used in the functions

def parsedate_mdy(text: str) -> datetime: #Tests paresedate_mdy function and returns it in the correct format
    """
    Takes a string in "MM/DD/YYYY" format and returns a datetime object.
    """
    return datetime.strptime(text, "%m/%d/%Y")

def formatdate_ymd(date: datetime) -> str: #Tests formatdate_ymd function and returns it in the yyyy-mm-dd format
    """
    Takes a datetime object and returns a formatted string in "YYYY-MM-DD" format.
    """
    return date.strftime("%Y-%m-%d")

if __name__ == "__main__": #Main program that tests the functions and prints the results
    test = "12/30/2000"
    date = parsedate_mdy(test)
    print(date)         # datetime object
    date_str = formatdate_ymd(date)
    print(date_str)     # formatted string "2000-12-30"


