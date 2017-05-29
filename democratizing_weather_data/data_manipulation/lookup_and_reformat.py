"""
This module contains code that transforms station data from
WBAN QLCD surface weather station data to a more consumable
CSV format.

(c) Data for Democracy
"""

import os
import googlemaps as gm


def lookup_wban_zip_and_tz(lat_long):
    """
    Get both the zip code and time zone of a lat and lon point via
    the Google Maps API. Used for when no such info is available
    in the WBAN data.
    
    Arguments: 
        lat_long (tuple): Tuple repsentation of a lat/lon point 
    Returns: 
        (tuple): Tuple of zipcode and timezone for the lat/lon
        point
    """

    proxies = {
        "http": os.getenv("HTTP"),
        "https": os.getenv("HTTPS")
    }

    #Instantiate a Google maps client so that the timezone and
    #zip code can be gathered
    gmaps = gm.Client(
        key=google_maps_key,
        requests_kwargs={proxies = proxies})

    zipcode = ''
    timezone = 0

    # call gmaps for reverse looking up
    reverse_zip = gmaps.reverse_geocode(lat_long)
    reverse_tz = gmaps.timezone(lat_long)

    # verify results and then return the needed data
    if reverse_zip[0]['address_components'][5]['types'][0] == 'country' and reverse_zip[0]['address_components'][5][
        'short_name'] == 'US':
        zipcode = reverse_zip[0]['address_components'][6]['short_name']
    if reverse_tz['status'] == 'OK':
        timezone = (result['rawOffset'] / 60) / 60

    return zipcode, timezone


def get_iso_dttz_format(date, time, timezone):
    # TZ Format  "1969-12-31T16:00-08:00"
    #            "YYYY-MM-DDTHH:MM-TZ"
    local_tz_formatted = get_iso_tz_format(timezone)

    file_dt = date + '-' + time
    file_dt = (dt.datetime.strptime(file_dt, "%Y%m%d-%H%M"))
    final_form_dt = file_dt.strftime("%Y-%m-%dT%H:%M") + local_tz_formatted

    return final_form_dt


def get_iso_tz_format(local_tz_int):
    """
    Function that returns a formatted ISO timezone
    local_tz_int = the timezone as an int
    """
    local_tz = ""
    if local_tz_int <= -10 or local_tz_int >= 10:
        local_tz = str(local_tz_int) +":00"
    elif local_tz_int <= 10 or local_tz_int >=-10:
        #If TZ is negative/positive, format string appropriately
        if local_tz_int < 0:
            local_tz = "-0" + str(abs(local_tz_int)) +":00"
        else:
            local_tz = "+0" + str(abs(local_tz_int)) +":00"
    return(local_tz)