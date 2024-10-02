from flask import Flask, render_template, request;
from database import get_job_card_data;
import base64;

html_top = """<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Job Card</title>
                    <link rel="stylesheet" type="text/css" href="/static/css/job_card.css">
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css">
                </head>
                <body>"""

html_bottom = """</body>
                </html>"""


def generate_job_card_html():
    data = get_job_card_data()

    complete_html_code = html_top

    for row in data:
        job_role = row[0]
        company_name = row[1]
        company_image = row[2]
        # Convert the blob data to a base64-encoded string
        logo_base64 = base64.b64encode(company_image).decode('utf-8')
        experience_years = row[3]
        salary = row[4]
        street = row[5]
        city = row[6]
        state = row[7]
        country = row[8]
        zip_code = row[9]
        job_listing_date = row[10]
        print(job_role, company_name, experience_years, salary, street, city, state, country, zip_code, job_listing_date)

        job_card = f"""<div class="job-card">
            <div class="section">
                <label class="job-role">{job_role}</label>
            </div>
            <div class="section">
                <div class="company-info">
                    <h3 class="company-name">{company_name}</h3>
                    <img class="company-logo" src="data:image/png;base64,{logo_base64}" alt="Company Logo">
                </div>
            </div>
            <div class="section">
                <div class="job-details">
                    <p class="experience-required">
                        <i class="fa-solid fa-clock"></i><span>  {experience_years} Yrs</span>
                    </p>
                    <p class="salary">
                        <i class="fa-solid fa-inr"></i><span>  {salary}</span>
                    </p>
                    <p class="job-location">
                        <i class="fa-solid fas fa-map-marker-alt"></i><span>  {city}, {country}</span>
                    </p>
                </div>
            </div>
            <div class="section">
                <p class="qualification-skills">
                    <i class="fa-solid fa-graduation-cap"></i><span>  Bachelor's Degree, Java, Python, JavaScript</span>
                </p>
            </div>
            <div class="section">
                <p class="publish-date">
                    <i class="far fa-calendar-alt"></i><span>   {job_listing_date}</span>
                </p>
            </div>
        </div>"""

        complete_html_code += job_card

    complete_html_code += html_bottom

    return complete_html_code


