# -------------------------------- oauth2 configuration -------------------------------------
# LinkedIn Authentication keys
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '77yzbsthwzsrke'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'xphjulTOvyXCh2Q2'

# Add email to requested authorizations.
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress',]
# Add the fields so they will be requested from linkedin.
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['email-address', 'headline', 'industry']
# Arrange to add the fields to UserSocialAuth.extra_data
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [('id', 'id'),
                                   ('firstName', 'first_name'),
                                   ('lastName', 'last_name'),
                                   ('emailAddress', 'email_address'),
                                   ('headline', 'headline'),
                                   ('industry', 'industry')]