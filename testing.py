import database as db;

print(db.get_job_application_status_by_recruiter(12))

db.update_job_application_status(3, 'accepted')
print('Updated status')

print(db.get_job_application_status_by_recruiter(12))