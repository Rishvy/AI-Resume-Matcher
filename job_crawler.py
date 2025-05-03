import requests

def fetch_linkedin_jobs(query, location, limit=10):
    """Use JSearch API from RapidAPI (free tier available)"""
    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "X-RapidAPI-Key": "e91092bb54mshd93de809b247cd3p1d05a6jsn70e9b6207a9d",
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    params = {
        "query": f"{query} in {location}",
        "num_pages": 2  # Change this if you want more results
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    return data.get("data", [])[:limit]

def fetch_indeed_jobs(query, location, limit=10):
    """Scrape Indeed jobs via unofficial API endpoint"""
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    params = {
        "q": query,
        "l": location,
        "limit": limit
    }

    url = "https://www.indeed.com/jobs"
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        # Parse with BeautifulSoup (simple title scrape example)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = []
        for div in soup.find_all("div", attrs={"class": "job_seen_beacon"}):
            title_tag = div.find("h2", class_="jobTitle")
            company_tag = div.find("span", class_="companyName")
            if title_tag and company_tag:
                jobs.append({
                    "title": title_tag.text.strip(),
                    "company": company_tag.text.strip()
                })
                if len(jobs) >= limit:
                    break
        return jobs
    return []

def fetch_remoteok_jobs(keyword, limit=10):
    """Use RemoteOK public API"""
    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        jobs = response.json()
        # Remove the metadata at index 0
        if isinstance(jobs, list):
            jobs = jobs[1:]
        filtered = [job for job in jobs if keyword.lower() in job.get("position", "").lower()]
        return filtered[:limit]
    return []