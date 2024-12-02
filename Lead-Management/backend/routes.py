from flask import request, jsonify
from app import app, db, mail
from flask_mail import Message
from models import Lead

@app.route('/leads', methods=['POST'])
def add_lead():
    data = request.json
    new_lead = Lead(
        name=data['name'],
        contact_info=data['contact_info'],
        platform=data['platform'],
        status=data.get('status', 'New')
    )
    db.session.add(new_lead)
    db.session.commit()
    
    # Send email notification
    try:
        msg = Message(
            "New Lead Added",
            sender="your-email@gmail.com",  # Change to your email
            recipients=["recipient@example.com"],  # Change to recipient's email
        )
        msg.body = f"A new lead '{new_lead.name}' has been added."
        mail.send(msg)
    except Exception as e:
        return jsonify({'message': 'Failed to send email', 'error': str(e)}), 500
    
    return jsonify({'message': 'Lead added successfully!'}), 201

@app.route('/leads', methods=['GET'])
def get_leads():
    leads = Lead.query.all()
    lead_list = [
        {
            'id': lead.id,
            'name': lead.name,
            'contact_info': lead.contact_info,
            'platform': lead.platform,
            'status': lead.status,
            'date_added': lead.date_added,
            'last_updated': lead.last_updated,
        }
        for lead in leads
    ]
    return jsonify(lead_list), 200

@app.route('/leads/<int:id>', methods=['PUT'])
def update_lead(id):
    data = request.json
    lead = Lead.query.get_or_404(id)
    old_status = lead.status
    lead.status = data.get('status', lead.status)
    db.session.commit()

    if old_status != lead.status:
        try:
            msg = Message(
                "Lead Status Updated",
                sender="your-email@gmail.com",  # Change to your email
                recipients=["recipient@example.com"],  # Change to recipient's email
            )
            msg.body = f"The status of lead '{lead.name}' has been updated from '{old_status}' to '{lead.status}'."
            mail.send(msg)
        except Exception as e:
            return jsonify({'message': 'Lead updated but failed to send email', 'error': str(e)}), 200

    return jsonify({'message': 'Lead updated successfully!'})

@app.route('/leads/<int:id>', methods=['DELETE'])
def delete_lead(id):
    lead = Lead.query.get_or_404(id)
    db.session.delete(lead)
    db.session.commit()
    
    # Send email notification
    try:
        msg = Message(
            "Lead Deleted",
            sender="your-email@gmail.com",  # Change to your email
            recipients=["recipient@example.com"],  # Change to recipient's email
        )
        msg.body = f"The lead '{lead.name}' has been deleted."
        mail.send(msg)
    except Exception as e:
        return jsonify({'message': 'Failed to send email', 'error': str(e)}), 500

    return jsonify({'message': 'Lead deleted successfully!'})
