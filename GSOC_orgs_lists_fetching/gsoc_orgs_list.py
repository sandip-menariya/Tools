import requests
import csv

def fetch_gsoc_orgs(year):
    url=f"https://api.gsocorganizations.dev/{year}.json"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        if isinstance(data, dict) and "organizations" in data:
            csv_lines=[]
            filename=f"gsoc_orgs_{year}.csv"
            with open(filename,mode="w",newline="",encoding="utf-8") as f:
                writer=csv.writer(f)
                writer.writerow(["Organization Name","Website","Category","Technologies","Topics","Project Name","Project Url"])
                for org in data.get("organizations",[]):
                    name=org.get("name","N/A")
                    website=org.get("url","N/A")
                    category=org.get("category","N/A")
                    technologies=",".join(org.get("technologies",[]))
                    topics=",".join(org.get("topics",[]))
                    projects=org.get("projects",[])
                    if projects:
                        for project in projects:
                            project_name=project.get("title","N/A")
                            project_url=project.get("project_url","N/A")
                            writer.writerow([name,website,category,technologies,topics,project_name,project_url])
                    else:
                        writer.writerow([name,website,category,technologies,topics,"N/A","N/A"])

for year in range(2016,2026):
    fetch_gsoc_orgs(year)