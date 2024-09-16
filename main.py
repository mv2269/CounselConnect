import requests
from bs4 import BeautifulSoup

# Base URL of the page to scrape (without the page number)
base_url = 'https://www.goodtherapy.org/therapists/ga/cumming?p='

# Function to fetch and parse a page
def scrape_page(page_num, search_specialty):
    # Full URL with the current page number
    url = base_url + str(page_num)
    
    # Send a GET request to fetch the page content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page {page_num}, status code: {response.status_code}")
        return
    
    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting data
    therapist_lists = soup.find_all('ul', class_='therapist-list')

    for therapist_list in therapist_lists:
        # Find all individual therapist items (li elements)
        therapists = therapist_list.find_all('li')
        
        for therapist in therapists:
            # Drill down to find the div with the class 'therapist_middle_section'
            middle_section = therapist.find('div', class_='therapist_middle_section')
            
            if middle_section:
                # Find the 'a' tag with class 'profile-url-link' and then the 'h2' tag for the name
                profile_link = middle_section.find('a', class_='profile-url-link')
                
                if profile_link:
                    # Extract the name, qualification, and specialty
                    name = profile_link.find('h2').text.strip() if profile_link.find('h2') else 'N/A'
                    qualification = profile_link.find('h3').text.strip() if profile_link.find('h3') else 'N/A'
                    speciality = profile_link.find('h4').text.strip() if profile_link.find('h4') else 'N/A'
                    
                    # Check if the specialty matches the user's search input
                    if search_specialty.lower() in speciality.lower():
                        print(f"Therapist Name: {name}")
                        print(f"Qualification: {qualification}")
                        print(f"Speciality: {speciality}")

                        contact_section = therapist.find('div', class_='therapist_contact_list')
            
                        if contact_section:
                            # Extract the address from all <p> tags with class 'lprofile-address'
                            addresses = contact_section.find_all('p', class_='lprofile-address')
                            for address in addresses:
                                print(f"Address: {address.text.strip()}")
                                break
                            
                            # Extract the phone number from the <span> tag with the class 'thrapist_phone_show'
                            phone_number = contact_section.find('span', class_='thrapist_phone_show')
                            if phone_number:
                                phone_number = phone_number.find('span').text.strip()
                                print(f"Phone Number: {phone_number}")
                        
                        print("-" * 50)  # Separator between therapists

# Get user input for specialty search
print("This program helps you find the right therapist based on your specific needs and specialties.")
print("")
search_specialty = input("Enter the therapist specialty you want to search for: ")
print("")

import time

# Scrape multiple pages (e.g., first 5 pages) with a delay between requests
print("Here are the therapists that match the ",search_specialty,"speciality")
print("")
for page in range(1, 6):
    scrape_page(page, search_specialty)
    time.sleep(2)  # Sleep for 2 seconds between requests