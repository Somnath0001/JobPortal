from database import get_job_application_status_by_recruiter;
from user_session import get_id;

def generate_manage_application_status_html():
    user_account_id = get_id()

    html_head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manage Job Application Status</title>
    <style>table, th, td {border: 1px solid black; border-collapse: collapse; padding: 10px;}</style>
</head>
<body>
    <table>
        <caption><b>Manage Status of Job Applications</b></caption>
        <tr>
            <th>Job Description</th>
            <th>Company</th>
            <th>Applied by</th>
            <th>Email</th>
            <th>Contact Number</th>
            <th>Status</th>
            <th>Application Date</th>
            <th>Accept</th>
            <th>Reject</th>
            <th>Schedule for Interview</th>
        </tr>"""
    
    html_end = """
    </table>
</body>
</html>"""

    complete_html_code = html_head
    result = get_job_application_status_by_recruiter(user_account_id)
    for data in result:
        job_application_status_id = data[9]
        color = "black"
        if (data[7] == "pending"):
            color = "orange"
        elif (data[7] == "accepted"):
            color = "limegreen"
        elif (data[7] == "rejected"):
            color = "red"
        elif (data[7] == "interviewScheduled"):
            color = "blue"

        row_code = f"""<tr>
        <td>{data[0]}</td>
        <td>{data[2]}</td>
        <td>{data[3]}</td>
        <td>{data[4]}</td>
        <td>{data[5]}</td>
        <td style="color:{color}">{data[7]}</td>
        <td>{data[8]}</td>
        <td><form action="/apply_job_application_status" method="POST">
                <input type="hidden" id="job_application_status_id" name="job_application_status_id" value="{job_application_status_id}">
                <input type="hidden" id="job_application_status" name="job_application_status" value="accepted">
                <input type="submit" value="Accept">
            </form>
        </td>
        <td><form action="/apply_job_application_status" method="POST">
                <input type="hidden" id="job_application_status_id" name="job_application_status_id" value="{job_application_status_id}">
                <input type="hidden" id="job_application_status" name="job_application_status" value="rejected">
                <input type="submit" value="Reject">
            </form>
        </td>
        <td><form action="/apply_job_application_status" method="POST">
                <input type="hidden" id="job_application_status_id" name="job_application_status_id" value="{job_application_status_id}">
                <input type="hidden" id="job_application_status" name="job_application_status" value="interviewScheduled">
                <input type="submit" value="Schedule for Interview">
            </form>
        </td>
</tr>"""
        complete_html_code += row_code

    complete_html_code += html_end

    return complete_html_code