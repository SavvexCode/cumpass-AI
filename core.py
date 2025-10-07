def get_bot_response(message):
    if not message:
        return "say something"
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "hey there welocome to Mubas XBot"
    elif "library" in message:
        return "library is in the main campass and its open 24/7"
    elif "fees" in message:
        return"you can pay your fees through students portal orthe accounts office"
    elif "help" in message:
        return"I can help you with directions,fees info and general campuss questions.You can try asking where is the admin office"
    elif "created" in message or "made" in message:
        return "I was created by Savestar a gamer,dreamer and coder kinda guy you dont wanna mess with"
    elif "Thaku" in message:
        return "you have entered a BRO CODE you are a legitimate member"
    elif "watson" in message:
        return "I know that watson guy an introvert whose first nick name was jg waky gome kkk"
    elif "mike" in message:
        return "aah thats the oldest thakuu obsessed with accounting"
    elif "chakhaza" in message:
        return "Hello Mr THOLO man"
    elif "savestar" in message:
        return "thats the brani behind me geez..respect"

    else:
        return"sorry....am not sure about that yet..Try asking something aboutcampus"


