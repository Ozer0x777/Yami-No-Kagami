from flask_wtf import FlaskForm # type: ignore
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField # type: ignore
from wtforms.validators import DataRequired # type: ignore

class AddForm(FlaskForm):
    category = SelectField('Database', choices=[('','Select a database'),(0, 'Group'),(3,'Market'),(5,'Telegram'),(8,'Twitter')],  default='', validators=[DataRequired()])
    groupname = StringField('Group name', validators=[DataRequired()])
    url  = StringField('Url', validators=[DataRequired()])
    submit = SubmitField('Add')

class AlertForm(FlaskForm):
    keywords = TextAreaField()
    submit = SubmitField('Update Keywords')

class DeleteForm(FlaskForm):
    delete = BooleanField('Check to delete', validators=[DataRequired()])
    submit = SubmitField('Delete this group')

class EditForm(FlaskForm):
    groupname = StringField(validators=[DataRequired()])
    galaxy = StringField()
    description = TextAreaField()
    profiles = TextAreaField()
    links = TextAreaField()
    submit = SubmitField('Save changes')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class SelectForm(FlaskForm):
    group = SelectField('Group to edit', coerce=str, validate_choice=True, validators=[DataRequired()])
    submit = SubmitField('Edit this group')

