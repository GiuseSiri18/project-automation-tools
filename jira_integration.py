import os
from jira import JIRA
from dotenv import load_dotenv

# Load environment variables from the .env file.
# This ensures that sensitive credentials (API Tokens) are not hardcoded.
load_dotenv()

# Retrieve Jira configuration from environment variables
JIRA_URL = os.getenv("JIRA_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")
PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")

def create_jira_task(summary, description):
    """
    Connects to the Jira Cloud instance and creates a new Task.

    Args:
        summary (str): The title of the Jira ticket.
        description (str): The detailed body of the ticket.
    """
    print("🔄 Connecting to Jira Cloud...")

    # Check if credentials are present to avoid runtime errors
    if not all([JIRA_URL, JIRA_EMAIL, JIRA_TOKEN, PROJECT_KEY]):
        print("❌ Error: Missing Jira credentials in .env file.")
        return

    try:
        # Establish connection using Basic Authentication
        # Note: Jira Cloud requires an API Token, not a password.
        jira = JIRA(server=JIRA_URL, basic_auth=(JIRA_EMAIL, JIRA_TOKEN))

        # Define the payload for the new issue
        issue_dict = {
            'project': {'key': PROJECT_KEY},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Task'}, # Can be customized (e.g., 'Story', 'Epic')
        }

        # Send request to Jira API
        new_issue = jira.create_issue(fields=issue_dict)

        print(f"✅ Jira Ticket Created Successfully: {new_issue.key}")
        print(f"🔗 Link: {JIRA_URL}/browse/{new_issue.key}")

    except Exception as e:
        print(f"❌ Failed to create Jira ticket. Error details: {e}")

if __name__ == "__main__":
    # Test execution block (only runs if the file is executed directly)
    print("--- Testing Jira Integration ---")
    create_jira_task("Test Ticket", "This is a test from the integration module.")