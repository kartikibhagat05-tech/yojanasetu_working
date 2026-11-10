import requests
import certifi
from bs4 import BeautifulSoup
from datetime import datetime
from .models import Vacancy, VacancyCategory

CATEGORY_MAPPING = {
    "ssc": "SSC",
    "bank": "Banking",
    "railway": "Railway",
    "upsc": "UPSC",
    "defence": "Defence",
    "police": "Police",
    "teaching": "Teaching",
    "nursing": "Nursing",
    "engineering": "Engineering",
    "it": "IT / Technical",
    "psu": "PSU",
    "insurance": "Insurance",
    "judiciary": "Judiciary",
    "agriculture": "Agriculture",
    "research": "Research",
    "state": "State Government",
    "municipal": "Municipal",
}

def map_category(title):
    title_lower = title.lower()
    for keyword, category_name in CATEGORY_MAPPING.items():
        try:
            return VacancyCategory.objects.get(name=category_name)
        except VacancyCategory.DoesNotExist:
            continue
    return VacancyCategory.objects.get_or_create(name="Others")[0]

def get_text_or_default(tag, default=""):
    return tag.text.strip() if tag else default

def scrape_site(url):
    try:
        response = requests.get(url, verify=certifi.where(), timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not fetch {url}: {e}")
        return

    soup = BeautifulSoup(response.text, "lxml")

    job_elements = soup.select("article.job") or soup.select("div.job") or soup.select("div.post-content")

    for job in job_elements:
        title = get_text_or_default(job.find("h2") or job.find("h3"))
        if not title:
            continue

        description = get_text_or_default(job.find("p"))
        source = url.split("//")[-1].split("/")[0]

        location = ""
        if job.find("span", class_="location"):
            location = job.find("span", class_="location").text.strip()

        last_date = None
        # try to find last date text next to deadline / last date keywords
        deadline_tag = job.find(string=lambda t: "last date" in t.lower())
        if deadline_tag:
            try:
                date_str = deadline_tag.strip().split(":")[-1].strip()
                last_date = datetime.strptime(date_str, "%d %B %Y").date()
            except:
                last_date = None

        link_tag = job.find("a", href=True)
        apply_link = link_tag["href"] if link_tag else ""

        category = map_category(title)

        Vacancy.objects.update_or_create(
            title=title,
            defaults={
                "category": category,
                "department": description[:200],
                "source": source,
                "job_location": location,
                "last_date": last_date,
                "apply_link": apply_link,
                "is_active": True,
            }
        )
