def sendmail(toemail, pbk):
    """
    Simulated email function for deployment.
    In production, replace this with real email service (SendGrid, AWS SES, etc.)
    """

    try:
        print("\n----- EMAIL SIMULATION -----")
        print(f"To: {toemail}")
        print(f"Subject: Decryption Key")
        print(f"Message: publickey: {pbk}")
        print("----------------------------\n")

        return True

    except Exception as e:
        print("Error in email simulation:", str(e))
        return False