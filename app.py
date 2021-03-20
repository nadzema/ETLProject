from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, text
from flask import Flask, jsonify, render_template

rds_connection_string = "postgres:@localhost:5432/Quotes"
engine = create_engine(f'postgresql://{rds_connection_string}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

app = Flask(__name__)


@app.route("/home")
def welcome():
    """List all available api routes."""
    return render_template("index.html")

@app.route("/quotes")
def quotes():
   session = Session (engine)

   results = session.query(quotes.id).all()

   session-close()

return jsonify (results)


# @app.route("/authors")
# def authors():
#     session = Session(engine)

#     results = session.query(author_information).all()
# pass
# @app.route("/authors/<author_name>")
# def oneauthor(author_name):
   
#    results = session.query(author_information.name)

# pass    
# @app.route("/tags")
# def tags():
# pass

# @app.route("/tags/<tag_name>")
# def onetag(tag_name):
# pass

# @app.route("/top10tags")
# def top10tags():
# pass


# if __name__ == '__main__':
#     app.run(debug=True)


