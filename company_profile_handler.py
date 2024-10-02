from database import get_company_id, add_company_profile, add_company_image;

def handle_company_profile(company_name, profile_description, business_stream_id, establishment_date, website_url, company_image):
    # insert company data to DB
    add_company_profile(company_name, profile_description, business_stream_id, establishment_date, website_url)

    # get company_id for the company
    company_id = get_company_id(company_name)
    print(f"company_id: {company_id}")

    company_image_data = company_image.read()

    # insert company_image to DB
    add_company_image(company_id, company_image_data)


