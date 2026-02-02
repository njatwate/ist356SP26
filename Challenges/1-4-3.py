from datetime import datetime

def parsedate_mdy(text: str) -> datetime:
    """
    Takes a string in "MM/DD/YYYY" format and returns a datetime object.
    """
    return datetime.strptime(text, "%m/%d/%Y")

def formatdate_ymd(date: datetime) -> str:
    """
    Takes a datetime object and returns a formatted string in "YYYY-MM-DD" format.
    """
    return date.strftime("%Y-%m-%d")

if __name__ == "__main__":
    test = "12/30/2000"
    date = parsedate_mdy(test)
    print(date)         # datetime object
    date_str = formatdate_ymd(date)
    print(date_str)     # formatted string "2000-12-30"


