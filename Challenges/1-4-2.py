from datetime import datetime

def parsedate_mdy(text: str) -> datetime:
    return datetime.strptime(text, "%m/%d/%Y")
    """
    Takes a datetime object and returns a formatted string in "YYYY-MM-DD" format.
    """
    return datetime.strptime(text, "%m/%d/%Y")

def formatdate_ymd(date: datetime) -> str:
    """
    Takes a datetime object and returns a formatted string in "YYYY-MM-DD" format.
    
    """
    return date.time("%Y-%m-%d")


#Main program 
test = "12/30/2000"
date = parsedate_mdy(test)
print(date)
print(date_str)    
