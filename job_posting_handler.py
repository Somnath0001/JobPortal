import database as db;

all_skill_set = db.get_all_skill_set()
#print(all_skill_set)

all_location = db.get_all_location()
#print(all_location)

all_company = db.get_all_company()
#print(all_company)

all_job_type = db.get_all_job_type()
#print(all_job_type)

"""
for i in range(len(all_job_type)):
    print(f"<option value=\"{all_job_type[i][0]}\">{all_job_type[i][1]}</option>")

for i in range(len(all_company)):
    print(f"<option value=\"{all_company[i][0]}\">{all_company[i][1]}</option>")

for i in range(len(all_location)):
    print(f"<option value=\"{all_location[i][0]}\">{all_location[i][1]}, {all_location[i][2]}, {all_location[i][3]}, {all_location[i][4]}, {all_location[i][5]}</option>")

for i in range(len(all_skill_set)):
    print(f"<option value=\"{all_skill_set[i][0]}\">{all_skill_set[i][1]}</option>")
"""

def generate_job_type_code():
    job_type_html_code = ""
    for i in range(len(all_job_type)):
        job_type_html_code += "\n"
        job_type_html_code += f"<option value=\"{all_job_type[i][0]}\">{all_job_type[i][1]}</option>"
    return job_type_html_code

def generate_company_code():
    company_code = ""
    for i in range(len(all_company)):
        company_code += "\n"
        company_code += (f"<option value=\"{all_company[i][0]}\">{all_company[i][1]}</option>")
    return company_code

def generate_location_code():
    location_code = ""
    for i in range(len(all_location)):
        location_code += "\n"
        location_code += (f"<option value=\"{all_location[i][0]}\">{all_location[i][1]}, {all_location[i][2]}, {all_location[i][3]}, {all_location[i][4]}, {all_location[i][5]}</option>")
    return location_code

def generate_skill_set_code():
    skill_set_code = ""
    for i in range(len(all_skill_set)):
        skill_set_code += "\n"
        skill_set_code += (f"<option value=\"{all_skill_set[i][0]}\">{all_skill_set[i][1]}</option>")
    return skill_set_code

# print(generate_skill_set_code())

code_1 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Posting</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    <link rel="stylesheet" type="text/css" href="/static/css/job_posting.css">
</head>
<body>
    <div class="container">
        <div class="card">
            <h2>Job Posting</h2>
            <form action="/job_posting_handler" method="POST">
                <div class="input-box">
                    <label for="job-type">Select Job Type:</label>
                    <select id="job-type" name="job-type" required>
                        <option value="">Select Job Type</option>"""

code_2 = """</select>
                </div>
                <div class="input-box">
                    <label for="company-name">Select Company:</label>
                    <select id="company-name" name="company-name" required>
                        <option value="">Select Company</option>"""

code_3 = """</select>
                </div>
                <div class="input-box">
                    <label for="hide-company-name">Hide Company Name?</label>
                    <div>
                        <input type="radio" id="hide-company-name-yes" name="hide-company-name" value="Y">
                        <label for="hide-company-name-yes">Yes</label>
                        <input type="radio" id="hide-company-name-no" name="hide-company-name" value="N" checked>
                        <label for="hide-company-name-no">No</label>
                    </div>
                </div>
                <div class="input-box">
                    <label for="job-description">Job Description:</label>
                    <textarea id="job-description" name="job-description" required></textarea>
                </div>
                <div class="input-box">
                    <label for="existing-or-new-location">Select location or add new location</label>
                    <div>
                        <input type="radio" id="existing-location" name="existing-or-new-location" value="existing" checked>
                        <label for="existing-location">Existing location</label>
                        <input type="radio" id="new-location" name="existing-or-new-location" value="new">
                        <label for="new-location">New location</label>
                    </div>
                </div>
                <div class="input-box">
                    <label for="job-location">Select Job Location:</label>
                    <select id="job-location" name="job-location">
                        <option value="">Select Job Location</option>"""

code_4 = """</select>
                </div>
                <div class="input-box new-address" style="display: none;">
                    <label for="street-address">Street Address:</label>
                    <input type="text" id="street-address" name="street-address">
                    <label for="city">City:</label>
                    <input type="text" id="city" name="city">
                    <label for="state">State:</label>
                    <input type="text" id="state" name="state">
                    <label for="country">Country:</label>
                    <input type="text" id="country" name="country">
                    <label for="zip-code">Zip Code:</label>
                    <input type="text" id="zip-code" name="zip-code">
                </div>
                <div class="input-box">
                    <label for="no-of-skill-set-required">How many skill set required?</label>
                    <select id="no-of-skill-set-required" name="no-of-skill-set-required" required>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                    </select>
                </div>
                <!--
                <div class="input-box skill-box">
                    <label>Skills Required:</label>
                    <div class="skill-fields">
                        <select id="required-skills" required>
                            <option value="0">Java</option>
                            <option value="1">Python</option>
                            <option value="3">JavaScript</option>
                        </select>
                        <select id="required-skill-level" required>
                            <option value="1">Beginner</option>
                            <option value="2">Intermediate</option>
                            <option value="3">Advanced</option>
                            <option value="4">Expert</option>
                        </select>
                    </div>
                </div>
                -->
                <div class="skill-box-container"></div>
                <div class="input-box">
                    <label for="experience-required">Experience Required (in Years):</label>
                    <input type="number" id="experience-required" name="experience-required" required>
                </div>
                <div class="input-box">
                    <label for="salary-offered">Salary Offered:</label>
                    <input type="number" id="salary-offered" name="salary-offered" required>
                </div>
                <div class="input-box">
                    <label for="apply-date">Apply Date:</label>
                    <input type="date" id="apply-date" name="apply-date" required>
                </div>
                <button type="submit" class="save-button">Save</button>
            </form>
        </div>
    </div>

    <script>"""

code_5 = """</script>
</body>
</html>"""

javascript_code_1 = """document.addEventListener('DOMContentLoaded', function() {
    // Location toggle logic
    const existingLocationRadio = document.getElementById('existing-location');
    const newLocationRadio = document.getElementById('new-location');
    const jobLocationSelect = document.getElementById('job-location');
    const newAddressDiv = document.querySelector('.new-address');

    existingLocationRadio.addEventListener('change', function() {
        if (this.checked) {
            jobLocationSelect.style.display = 'block';
            newAddressDiv.style.display = 'none';
        }
    });

    newLocationRadio.addEventListener('change', function() {
        if (this.checked) {
            jobLocationSelect.style.display = 'none';
            newAddressDiv.style.display = 'block';
        }
    });

    // Initialize default state
    if (existingLocationRadio.checked) {
        jobLocationSelect.style.display = 'block';
        newAddressDiv.style.display = 'none';
    }

    // Dynamic skill box logic
    const skillSetCountSelect = document.getElementById('no-of-skill-set-required');
    const skillBoxContainer = document.querySelector('.skill-box-container');

    // Initialize skill box container
    skillBoxContainer.innerHTML = '';

    skillSetCountSelect.addEventListener('change', function() {
        const skillSetCount = parseInt(this.value);
        skillBoxContainer.innerHTML = '';

        for (let i = 0; i < skillSetCount; i++) {
            const skillBox = document.createElement('div');
            skillBox.className = 'input-box skill-box';

            skillBox.innerHTML = `
                <label for="required-skills-${i}">Skills Required ${i + 1}:</label>
                <div class="skill-fields">
                    <select id="required-skills-${i}" name="required-skills-${i}" required>"""

javascript_code_2 = """</select>
                    <label for="required-skill-level-${i}">Skill Level:</label>
                    <select id="required-skill-level-${i}" name="required-skill-level-${i}" required>
                        <option value="1">Beginner</option>
                        <option value="2">Intermediate</option>
                        <option value="3">Advanced</option>
                        <option value="4">Expert</option>
                    </select>
                </div>
            `;

            skillBoxContainer.appendChild(skillBox);
        }
    });

    // Initialize default skill box
    skillSetCountSelect.dispatchEvent(new Event('change'));
});"""


def generate_job_posting_html_code():
    job_posting_html_code = code_1 + generate_job_type_code() + code_2 + generate_company_code() + code_3 + generate_location_code() + code_4 + javascript_code_1 + generate_skill_set_code() + javascript_code_2 + code_5 
    return job_posting_html_code

# print(generate_job_posting_html_code())
