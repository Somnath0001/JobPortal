from database import applied_jobs;
from user_session import get_id;

def generate_check_application_status_html():
    user_account_id = get_id()

    html_head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Application Status</title>
</head>
<body>
    <table>
        <tr>
            <th>Job Description</th>
            <th>Company</th>
            <th>Status</th>
            <th>Application Date</th>
        </tr>"""
    
    html_end = """
    </table>
</body>
</html>"""

    complete_html_code = html_head
    result = applied_jobs(user_account_id)
    for data in result:
        row_code = f"""<tr>
        <td>{data[0]}</td>
        <td>{data[2]}</td>
        <td>{data[3]}</td>
        <td>{data[4]}</td>
</tr>"""
        complete_html_code += row_code

    complete_html_code += html_end

    return complete_html_code