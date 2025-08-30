import os
import requests
import csv

def main():
    # Let user provide url of table to scrape
    url = input("URL: ")
    path = input("Path (optional): ")

    if not check_url(url):
        raise ValueError("Provided URL does not have correct form. " \
                         "URL should look similar to: " \
                         "https://www.statistik-bw.de/BevoelkGebiet/GebietFlaeche/01515020.tab?R=GS335043")

    urls = construct_urls(url)

    for url in urls:
        # TODO: Add terminal progress bar.
        if path != "":
            get_csv(url, path)
        else:
            get_csv(url)

def check_url(url):
    '''
    Checks if url resembles 'https://www.statistik-bw.de/BevoelkGebiet/GebietFlaeche/01515020.tab?R=GS335043'.
    '''
    # Check if base url is correct
    if 'https://www.statistik-bw.de/' not in url:
        return False
    
    # Check if table is selected and level selected
    if '.tab?R=' not in url:
        return False
    
    return True

def construct_urls(example_url):
    '''
    Takes str as input. example_url is the url of a specific table to be
    downloaded with one town or so being selected. Function recognises level of
    information and parses for all available data on this level.

    e.g. choose table for 'Konstanz, Universitätsstadt' -> returns same table 
    for all Gemeinden in BW.
    '''
    try:
        table_url, query = example_url.split("?")
    except Exception as e:
        raise ValueError("URL not supported or no city or town selected.")

    gemeinden = get_gemeinden()

    url_list = []
    if query[:4] == "R=GS":         # So far, only this case is supported.
        for gemeinde in gemeinden:
            key = gemeinde["AGS"]
            new_url = table_url + "?" + query[:4] + key[2:]
            url_list.append(new_url)

    return url_list

def get_gemeinden():
    '''
    Reads csv and returns data as Python dict.
    '''
    with open('gemeinden.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        gemeinden = []
        for row in reader:
            gemeinden.append(row)

    # If you want to filter values, this would be a good place to add a filter
    # function for `gemeinden`. You could also filter them while reading from
    # the csv file.

    return gemeinden

def get_csv(table_url, path="data"):
    # Define path to save to
    key = table_url.split("?")[1][4:]
    path = os.path.join(path, "08" + key + ".csv")

    # Build url to download from
    url = table_url + "&form=csv"
    r = requests.get(url)

    # Check if request worked
    if r.status_code != 200:
        raise ValueError(f"Website not responding as expected with key: {key}")

    # Save to file
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(r.text)

if __name__ == "__main__":
    main()