from flask import Flask
from master import ascii_print

app = Flask(__name__)

@app.route("/")
def home():
    try:
         info, art = ascii_print()
         printable = info+"\n"+art.get_text()+"\n\n"
    except AttributeError:
         home()
         return None
    except TypeError:
        home()
        return None
    return printable
