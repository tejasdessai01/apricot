from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phonebook.db'
db = SQLAlchemy(app)

# Define the model for storing name and phone number
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

# Endpoint to add a new contact
@app.route('/api/contact', methods=['POST'])
def add_contact():
    data = request.get_json()
    fname = data.get('fname')
    lname = data.get('lname')
    phone_number = data.get('phone_number')

    # Ensure first name, last name, and phone_number are provided
    if not lname or not fname or not phone_number:
        return jsonify({'message': 'First name, last name, and phone number are required.'}), 400

    # Ensure phone number is in US format (xxx) xxx-xxxx
    if not re.match(r'^\(\d{3}\) \d{3}-\d{4}$', phone_number):
        return jsonify({'message': 'Phone number must be in (xxx) xxx-xxxx format.'}), 400

    # Create a new contact object
    new_contact = Contact(fname=fname, lname=lname, phone_number=phone_number)

    # Add the new contact to the database
    db.session.add(new_contact)
    db.session.commit()

    return jsonify({'message': 'Contact added successfully.'}), 201

# Endpoint to retrieve all contacts
@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    contact_list = []
    for contact in contacts:
        contact_data = {
            'id': contact.id,
            'fname': contact.fname,
            'lname': contact.lname,
            'phone_number': contact.phone_number
        }
        contact_list.append(contact_data)

    return jsonify(contact_list)

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run(debug=True)
