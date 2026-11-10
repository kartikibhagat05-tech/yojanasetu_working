from django.core.management.base import BaseCommand
from vacancy.scraper import scrape_site

# List of URLs for scraping each category
CATEGORY_URLS = [
    "https://ibps.in",  # banking
    "https://ssc.nic.in",  # SSC
    "https://upsc.gov.in",  # UPSC
    # Add all other category URLs here
     "https://freejobalert.com/search-jobs/page/1",
    "https://freejobalert.com/search-jobs/page/2",
    "https://indiangovtjobs.co.in/",
]

class Command(BaseCommand):
    help = "Scrape all vacancies from predefined sites"

    def handle(self, *args, **kwargs):
        for url in CATEGORY_URLS:
            print(f"Scraping {url} ...")
            scrape_site(url)
        self.stdout.write(self.style.SUCCESS("All vacancies scraped successfully!"))
