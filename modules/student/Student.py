class StudentClass:

    def __init__(self):
        self.full_name = ''
        self.date_of_birth_or_age = ''
        self.gender = None
        self.mobile_number = ''
        self.email_address = ''
        self.password = ''
        self.preferred_language = ''
        self.school_college_name = ''
        self.class_grade = ''
        self.board_curriculum = ''
        self.academic_year = ''
        self.subjects_for_tuition = []
        self.current_level_by_subject = {}
        self.help_topics = []
        self.parent_guardian_name = ''
        self.parent_guardian_relationship = ''
        self.parent_guardian_mobile_number = ''
        self.parent_guardian_email_address = ''
        self.preferred_communication_method = ''

    def setUserNameAndPassword(self, email, password):
        self.email_address = email
        self.password = password