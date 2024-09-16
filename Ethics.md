## Purpose of Data Collection

The purpose of this data collection is to gather publicly available information about therapists in Cumming, GA, for educational and research purposes. The data will help us apply web scraping techniques and analyze therapist information in a structured format.

## Why We Are Collecting This Data

We are collecting this data to:

- **Learn**: Understand and practice web scraping techniques.
- **Analyze**: Examine therapist information to gain insights into available services in a specific region.
- **Demonstrate**: Showcase practical applications of data collection and processing.

## Data Sources and `robots.txt`

- **Data Source**: The data is collected from https://www.goodtherapy.org/therapists/ga/cumming?p=1 , which provides a directory of therapists.
- **Compliance**: The robots.txt file for GoodTherapy does not disallow scraping of the therapist directory pages. We have verified compliance by reviewing the robots.txt file located at [https://www.goodtherapy.org/robots.txt](https://www.goodtherapy.org/robots.txt).

## Collection Practices

- **Limit Scraping**: We limit our scraping to avoid disrupting the website’s normal operations. This is achieved by implementing rate limiting (e.g., delaying between requests).
- **Password Protection**: We do not attempt to bypass any password protection or access restricted areas of the site.

## Data Handling and Privacy

- **No PII Collection**: We do not collect personally identifiable information (PII). The data collected includes public information such as names, qualifications, specialties, addresses, and phone numbers.
- **Secure Storage**:  Currently, the script does not store any data. The data is only printed to the console.
- **If Data Storage Is Implemented**: Should data storage be introduced in the future, sensitive files should be added to .gitignore to prevent accidental exposure.
  
## Data Usage

- **Educational and Research Purposes**: The data collected is used solely for educational and research purposes. It is intended to demonstrate web scraping techniques and analyze public information in a structured way.
