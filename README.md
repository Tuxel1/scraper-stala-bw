# scraper-stala-bw

A Python-based scraper to download data from [Statistisches Landesamt Baden-Württemberg](https://www.statistik-bw.de/).

## Usage

Run `scraper.py`. When prompted, provide the program with a full URL from the website of Statistisches Landesamt Baden-Württemberg.
You should have selected a table and a municipality. The scraper will automatically scrape the data for all municipalities in Baden-Württemberg.

Example URL: `https://www.statistik-bw.de/BevoelkGebiet/GebietFlaeche/01515020.tab?R=GS335043`

If you want to get data for specific municipalities, please (for now) edit `get_gemeinden()` in `scraper.py` where specified and write your own filter function.

## Roadmap

So far, the scraper only supports scraping data for municipalities. In the future, support for other levels of data will be provided.

## For future reference

`gemeinden.csv` was sourced from [this PDF file](https://www.statistik-bw.de/Service/LIS/Gemeindetabellen/RV_UEG_RegioSTab_GS_VWE.pdf) using [Tabula](https://tabula.technology/).