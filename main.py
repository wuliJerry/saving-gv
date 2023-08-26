import smtplib
import random
import os

def send_email(recipient_email, subject, body):
    OUTLOOK_USER = os.environ.get('OUTLOOK_USER')
    OUTLOOK_PASSWORD = os.environ.get('OUTLOOK_PASSWORD')

    headers = [
        "From: " + OUTLOOK_USER,
        "Subject: " + subject,
        "To: " + recipient_email,
        "MIME-Version: 1.0",
        "Content-Type: text/html"
    ]
    headers = "\r\n".join(headers)

    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.ehlo()
        server.starttls()
        server.login(OUTLOOK_USER, OUTLOOK_PASSWORD)
        server.sendmail(OUTLOOK_USER, recipient_email, headers + "\r\n\r\n" + body)
        server.close()

        print('Email sent!')
    except Exception as e:
        print('Something went wrong:', e)

if __name__ == '__main__':
    # List of random sentences
    sentences = [
        "Sometimes, the smallest step in the right direction becomes the most significant leap of your life.",
        "Cherish the rhythm of every heartbeat.",
        "Challenges are the universe's way of testing our mettle.",
        "Sometimes, the smallest step in the right direction becomes the most significant leap of your life.",
        "Cherish the rhythm of every heartbeat.",
        "Challenges are the universe's way of testing our mettle.",
        "Discovering oneself is the greatest journey of all.",
        "Embrace every sunset, and be ready for every sunrise.",
        "Stars cannot shine without darkness around them.",
        "Our greatest stories are written in the pages of time.",
        "Every end marks a new beginning.",
        "In the heart of every struggle lies an opportunity waiting to be found.",
        "Dreams paint the canvas of our imagination.",
        "The world is a book, and those who don't travel read only a page.",
        "Music is the poetry of the air.",
        "To find yourself, sometimes you need to get lost.",
        "Time has a way of healing the deepest wounds.",
        "The universe hums a song of endless possibilities.",
        "Happiness is a journey, not a destination.",
        "Behind every moment, there's a story waiting to be told.",
        "Life's melodies are sweeter with love in the air.",
        "Hope is the anchor that keeps us grounded during the stormiest nights.",
        "In the symphony of existence, we all have our unique note to play."
    ]
    
    random_sentence = random.choice(sentences)
    send_email('evcxdedesxf@gmail.com', 'Your Random Sentence', random_sentence)
