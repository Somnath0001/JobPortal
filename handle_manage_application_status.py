from database import get_job_application_status_by_recruiter;
from user_session import get_id;
import base64;

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
            <th>Resume</th>
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
        job_application_status_id = data[11]
        color = "black"
        if (data[7] == "pending"):
            color = "orange"
        elif (data[7] == "accepted"):
            color = "limegreen"
        elif (data[7] == "rejected"):
            color = "red"
        elif (data[7] == "interviewScheduled"):
            color = "blue"

        # Base64 encode the file data
        resume_base64 = base64.b64encode(data[10]).decode('utf-8')
        # Prepend "data:application/pdf;base64," to the encoded string to ensure the browser interprets it as a PDF file.
        resume_link = f"data:application/pdf;base64,{resume_base64}"

        row_code = f"""<tr>
        <td>{data[0]}</td>
        <td>{data[2]}</td>
        <td>{data[3]}</td>
        <td>{data[4]}</td>
        <td>{data[5]}</td>
        <td style="color:{color}">{data[7]}</td>
        <td>{data[8]}</td>
        <td><a href="{resume_link}" download="{data[9]}" target="_blank">{data[9]}</a></td>
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