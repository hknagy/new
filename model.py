
from wtforms import Form, StringField, validators, ValidationError

class InputForm(Form):

    str1 = StringField(validators=[validators.InputRequired()])
    str2 = StringField(validators=[validators.InputRequired()])
    metrics = StringField(validators=[validators.InputRequired()])    
      
    def validate_length(self, field1, field2, field3):
        val = Form.validate(self)
        if not val:
           return False
      
        if field3 == 'hamming':
           if len(field1) != len(field2):
              self.message = "The strings must be equal in length for Hamming distance"
              #raise ValidationError("The two strings must be equal in length.")
              self.str2.errors.append(self.message)
              return False
        
