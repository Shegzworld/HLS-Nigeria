from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator:
    def validate(self, password, user=None):
        # Password length validation (min 8 characters)
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        
        # Password complexity check: must contain both uppercase and lowercase
        if not re.search(r'[a-z]', password):
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Password must contain at least one uppercase letter.")
        
        # Password complexity check: must contain at least one digit
        if not re.search(r'[0-9]', password):
            raise ValidationError("Password must contain at least one digit.")
        
        # Password complexity check: must contain at least one special character
        if not re.search(r'[@$!%*?&]', password):
            raise ValidationError("Password must contain at least one special character: @$!%*?&")
    
    def get_help_text(self):
        return """
        Your password must:
        - Be at least 8 characters long.
        - Contain at least one lowercase letter.
        - Contain at least one uppercase letter.
        - Contain at least one digit.
        - Contain at least one special character (@$!%*?&).
        """
