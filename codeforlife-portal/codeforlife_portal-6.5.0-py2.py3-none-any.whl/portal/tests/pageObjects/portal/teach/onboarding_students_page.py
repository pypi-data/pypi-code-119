from __future__ import absolute_import

from . import onboarding_student_list_page
from .teach_base_page import TeachBasePage


class OnboardingStudentsPage(TeachBasePage):
    def __init__(self, browser):
        super(OnboardingStudentsPage, self).__init__(browser)

        assert self.on_correct_page("onboarding_students_page")

    def create_students(self):
        self._click_create_students()

        return onboarding_student_list_page.OnboardingStudentListPage(self.browser)

    def create_students_empty(self):
        self._click_create_students()

        return self

    def create_students_failure(self):
        self._click_create_students()

        return self

    def _click_create_students(self):
        self.browser.find_element_by_name("new_students").click()

    def type_student_name(self, name):
        self.browser.find_element_by_id("id_names").send_keys(name + "\n")
        return self
