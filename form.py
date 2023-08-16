from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired

FAI=Flask(__name__)

# Creating Form Class
class WebForms(Form):
    name=StringField(validators=[DataRequired()])
    age=IntegerField(validators=[DataRequired()])
    submit=SubmitField()

@FAI.route('/webforms',methods=["GET","POST"])
def webforms():
    # WF=WebForms()
    if request.method=="POST":
        form_data=WebForms(request.form)
        if form_data.validate():
            return form_data.data
    return render_template('webforms.html',WF=WebForms())

if __name__=="__main__":
    FAI.run(debug=True)