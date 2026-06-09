def classify_email(subject, body):
    """Classify email based on keywords — 100% free."""
    text = (subject + " " + body).lower()
    
    support_words = ['help', 'error', 'broken', 'bug', 'issue', 'problem', 'not working', 'fix', 'wrong', 'failed']
    sales_words = ['price', 'cost', 'buy', 'purchase', 'plan', 'demo', 'trial', 'subscription', 'package']
    complaint_words = ['refund', 'complaint', 'angry', 'disappointed', 'bad', 'terrible', 'unhappy', 'cancel', 'poor']
    
    if any(w in text for w in support_words):
        return "SUPPORT"
    if any(w in text for w in complaint_words):
        return "COMPLAINT"
    if any(w in text for w in sales_words):
        return "SALES"
    
    return "INQUIRY"

def generate_reply(subject, body, category):
    """Generate professional reply based on category."""
    replies = {
        "SUPPORT": "Thank you for reaching out! I understand you're experiencing an issue and I want to help resolve this as quickly as possible. Could you please provide a few more details about what's happening?\n\nIn the meantime, here are some steps that might help:\n- Clear your cache and restart\n- Check our help center at help.company.com\n- Update to the latest version\n\nI'll keep an eye out for your reply and make this a priority.\n\nBest regards,\nSupport Team",

        "SALES": "Thank you for your interest! I'm excited to help you explore how our solution can meet your needs.\n\nHere's what I can do:\n- Send you detailed pricing information\n- Schedule a personalized demo\n- Connect you with a product specialist\n\nWhat would be most helpful for you?\n\nLooking forward to hearing from you!\n\nBest regards,\nSales Team",

        "COMPLAINT": "I want to sincerely thank you for bringing this to our attention. I completely understand your frustration, and I take full responsibility for making this right.\n\nI have already flagged this issue with our team and I'm personally going to follow up to ensure it gets resolved within the next 24 hours.\n\nIn the meantime, if there's anything else I can do immediately, please don't hesitate to let me know.\n\nThank you for your patience.\n\nBest regards,\nCustomer Success Team",

        "INQUIRY": "Thank you for your message! That's a great question.\n\nHere's the information you requested. If you need any clarification or have additional questions, please feel free to ask — I'm happy to help.\n\nYou can also find more resources at help.company.com or reach us by phone at 1-800-555-0123.\n\nBest regards,\nSupport Team"
    }
    
    return replies.get(category, replies["INQUIRY"])