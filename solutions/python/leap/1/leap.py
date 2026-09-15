def leap_year(year):
    """Verify that the year currently we are in is a leap year or not
    
    Parameters:
        year (int)
    
    Returns:
        bool: Is the year a leap year?"""
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
