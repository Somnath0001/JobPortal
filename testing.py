import database as db;
from werkzeug.security import generate_password_hash, check_password_hash

print("som@pass: ", generate_password_hash("som@pass"))
print("santanu@pass: ", generate_password_hash("santanu@pass"))
print("sayan@pass: ", generate_password_hash("sayan@pass"))
print("susanta@pass: ", generate_password_hash("susanta@pass"))
print("sukhendu@pass: ", generate_password_hash("sukhendu@pass"))
print("subhajit@pass: ", generate_password_hash("subhajit@pass"))
print("sujoy@pass: ", generate_password_hash("sujoy@pass"))
print("rakesh@pass: ", generate_password_hash("rakesh@pass"))
print("sujit@pass: ", generate_password_hash("sujit@pass"))