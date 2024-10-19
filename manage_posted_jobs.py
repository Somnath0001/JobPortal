from database import get_posted_jobs;
from user_session import get_id;

def generate_manage_posted_jobs():
    html_code = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manage Posted Jobs</title>
    <style>table, th, td {{border: 1px solid black;border-collapse: collapse;padding: 5px;}}</style>
</head>
<body>
    <table>
        <caption><b>Manage Posted Jobs</b></caption>
        <tr>
            <th>Job Post Id</th>
            <th>Job Type</th>
            <th>Company</th>
            <th>Hide Company</th>
            <th>Created Date</th>
            <th>Job Description</th>
            <th>Location</th>
            <th>Active</th>
            <th>Salary</th>
            <th>Experience</th>
            <th>Change Status</th>
        </tr>
        {}
    </table>
</body>
</html>"""

    user_account_id = 15 # get_id()
    result = get_posted_jobs(user_account_id)
    all_row_code = ""
    for row in result:
        job_post_id = row[0]
        is_active = row[11]
        change_to = "Close"
        change_status_to = "N"

        if is_active == "Y":
            change_to = "Close"
            change_status_to = "N"
        elif is_active == "N":
            change_to = "Open"
            change_status_to = "Y"

        row_code = f"""<tr>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>{row[2]}</td>
            <td>{row[3]}</td>
            <td>{row[4]}</td>
            <td>{row[5]}</td>
            <td>{row[9]}, {row[7]}, {row[8]}</td>
            <td>{row[11]}</td>
            <td>{row[12]}</td>
            <td>{row[13]} yrs</td>
            <td>
                <form action="/manage_posted_jobs" method="POST">
                <input type="hidden" id="job_post_id" name="job_post_id" value="{job_post_id}">
                <input type="hidden" id="job_post_status" name="job_post_status" value="{change_status_to}">
                <input type="submit" value="{change_to}">
            </form>
            </td>
        </tr>
        """
        all_row_code += row_code

    complete_html_code = html_code.format(all_row_code)
    return complete_html_code