import re
from apps.main import db, models

def clear():
    phrases = models.Phrases.query.all()
    srt = models.Srt.query.all()
    words = models.UpperWords.query.all()

    for word in words:
        word.word = re.sub(r'[^A-Za-z0-9\!\?\.\,\s]', '', word.word)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            db.session.delete(word)
            db.session.commit()

    for phrase in phrases:
        phrase.phrase = re.sub(r'[^A-Za-z0-9\!\?\.\,\s]', '', phrase.phrase)

    for s in srt:
        s.set_of_words = re.sub(r'[^A-Za-z0-9\!\?\.\,\s]', '', s.set_of_words)
        s.list_of_words = re.sub(r'[^A-Za-z0-9\!\?\.\,\s]', '', s.list_of_words)

    try:
        db.session.commit()
    except:
        db.session.rollback()

if __name__ == '__main__':
    clear()