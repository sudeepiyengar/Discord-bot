from bs4 import BeautifulSoup as BS
import requests
import discord

def find_job():
    #skill = input("Enter skills: ")
    #loc = input("Enter location: ")
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=india'
    html_file = requests.get(url)

    soup = BS(html_file.text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')


    for job in (jobs):
        #published_date = job.find('span', class_='sim-posted').span.text
        #if 'few' in published_date:
        company_name = job.find('h3', class_='joblist-comp-name').text
        skills = job.find('span', class_='srp-skills').text
        more_info = job.header.h2.a['href']

        print("Company Name:", company_name.strip())
        print("Required Skills:", skills.strip())
        print("More info:", more_info.strip())
        print("\n")

client = discord.Client()

@client.event

async def on_ready():
    print("Logged in as {0.user}".format(client))
    
@client.event

async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$job'):
        find_job()
        
client.run('<Insert token>')