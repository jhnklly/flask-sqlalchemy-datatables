"""Flask tutorial models.

Basic example: a User has one or many Addresses.
"""
import datetime
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('../app.cfg')
db = SQLAlchemy(app)

# DataTables warning: table id=dt_110x - (_mysql_exceptions.ProgrammingError) (1146,
# "Table 'miro_dev.users' doesn't exist") [SQL: u'
# SELECT Count(*) AS count_1
# FROM   (SELECT users.id AS users_id
#         FROM   users
#                INNER JOIN addresses
#                        ON users.id = addresses.user_id
#         WHERE  addresses.id > 14) AS anon_1
# '] [parameters: (14,)]



class ModuleBlob(db.Model):

    __tablename__ = 'module_blob'

    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Unicode, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    transcription_text_id = db.Column(db.Integer, db.ForeignKey('transcription_text.id'))

    def __unicode__(self):
        """Give a readable representation of an instance."""
        return '%s' % self.name

    def __repr__(self):
        """Give a unambiguous representation of an instance."""
        return '<%s#%s>' % (self.__class__.__name__, self.id)


class TranscriptionText(db.Model):

    __tablename__ = 'transcription_text'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Unicode, unique=False)
    # transcription_id = db.relationship('ModuleBlob', uselist=False, backref=db.backref('module_blob'))

    def __unicode__(self):
        """Give a readable representation of an instance."""
        return '%s' % (self.id)

    def __repr__(self):
        """Give a unambiguous representation of an instance."""
        return '<%s#%s>' % (self.__class__.__name__, self.id)
