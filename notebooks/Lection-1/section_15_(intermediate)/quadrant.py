def quadrant(address):
    """
    Повертає квадрант постійного струму для вказаної адреси.
    """
    return [_quadrant for _quadrant in address.split(' ') if _quadrant in ['NW', 'NE', 'SW', 'SE']] or None

