# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a 
# system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

service_tickets = {
     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
 }

# Dictionary to store the tickets
tickets = {}

def create_ticket(ticket_id, customer_name, issue_description):
    """ Create a new ticket """
    if ticket_id in tickets:
        print(f"Error: Ticket ID '{ticket_id}' already exists.")
    else:
        tickets[ticket_id] = {
            'customer_name': customer_name,
            'issue_description': issue_description,
            'status': 'Open'
        }
        print(f"Ticket '{ticket_id}' created successfully.")

def update_ticket(ticket_id, status):
    """ Update the status of a ticket """
    if ticket_id in tickets:
        tickets[ticket_id]['status'] = status
        print(f"Ticket '{ticket_id}' status updated to '{status}'.")
    else:
        print(f"Error: Ticket ID '{ticket_id}' not found.")

def view_ticket(ticket_id):
    """ View details of a ticket """
    if ticket_id in tickets:
        ticket_details = tickets[ticket_id]
        print(f"Ticket ID: {ticket_id}")
        print(f"Customer Name: {ticket_details['customer_name']}")
        print(f"Issue Description: {ticket_details['issue_description']}")
        print(f"Status: {ticket_details['status']}")
    else:
        print(f"Error: Ticket ID '{ticket_id}' not found.")

def list_tickets():
    """ List all tickets """
    if tickets:
        print("Current Tickets:")
        for ticket_id, details in tickets.items():
            print(f"Ticket ID: {ticket_id}, Customer: {details['customer_name']}, Status: {details['status']}")
    else:
        print("No tickets found.")


