def get_bot_response(message):
    if not message:
        return "say something"
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "hey there welocome to mubas XBot"
    elif "library" in message:
        return "library is in the main campass and its open 24/7"
    elif "fees" in message:
        return"you can pay your fees through students portal orthe accounts office"
    elif "help" in message:
        return"I can help you with directions,fees info and general campuss questions.You can try asking where is the admin office"
    else:
        return"sorry....am not sure about that yet..Try asking something aboutcampus"


