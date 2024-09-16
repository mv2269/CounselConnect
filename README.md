# CounselConnect
## Description

This Python script scrapes data on therapists from the GoodTherapy website for therapists located in Cumming, GA. The script helps users find therapists based on their specialty by extracting and displaying detailed information such as the therapist's name, qualifications, specialty, address, and phone number. We scraped data from pages 1 through 5 of the GoodTherapy website, providing a list of available therapists in Cumming, GA.

The GoodTherapy website also includes therapist information for other states, which could be included in future scraping efforts.


## Website Used

The scraper targets the GoodTherapy website (`https://www.goodtherapy.org/therapists/ga/cumming?p=1`) due to its comprehensive directory of licensed therapists. The website was chosen for its extensive listing of therapists, which allows users to filter and find professionals based on their needs. It provides a centralized source for relevant therapist information in the specified geographic location.

**Note:** Data has currently been scrapped from pages 1 through 5. 

## How to Run

1. **Clone the Repository**

   - To get started, clone this repository to your local machine:

       git clone https://github.com/Marian-CA/CounselConnect.git

       cd CounselConnect

3. **Install Dependencies**

    - Install the required Python libraries using pip. Create a requirements.txt file if you don't have one, with the following content:

        requests

        beautifulsoup4

    - Then, install the dependencies:

        pip install -r requirements.txt

4. **Run the Script**

    - Execute the script using Python:

        python main.py

    - When prompted, enter the specialty you want to search for (e.g., "marriage").

## Benefits
This script provides a streamlined way to gather detailed information about therapists, which can save users significant time and effort compared to manual searches. By automating the data collection process, users can quickly access a curated list of therapists that meet their specific needs. The tool delivers unique insights into available therapy services and helps users make informed decisions based on comprehensive, up-to-date information.
