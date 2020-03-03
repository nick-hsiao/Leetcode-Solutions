class Questionnaire:

	def __init__ (self):
		self.answers = ['yes','no']
		self.age_req = False
		self.residency_req = False
		self.work_req = False
		self.parent_req = False
		self.volunteer_req = False
		self.household_req = False

	def run(self):
		print('Hello, welcome to the scholarship eligibility questionnaire!')
		print('Please answer the following questions with either "Yes" or "No"...')

		ans = input('Are you a student between the age of 18 and 24? (inclusive)')
		self.check_age(ans)
		ans = input('Have you lived in California for at least 2 years?')
		self.check_residency(ans)
		ans = input('Have you worked part-time for at least for 6 months in the relevant field of study?')
		self.check_work(ans)

		if not work_req and not volunteer_req:
			ans = input('Is your household income less than 5000$ per annum?')
			self.check_household(ans)

		result = self.validate_answers()
		print(f'Based on your answers, your scholarship elgibility status is: {result}')
		print('Thank you for filling out the questionnaire, have a nice day!')


	def check_age(self,ans):
		while ans.lower() not in answers:
			ans = input('Invalid input, please try again\n')

		if ans.lower() == 'yes':
			self.age_req = True

	def check_residency(self,ans):
		while ans.lower() not in answers:
			ans = input('Invalid input, please try again\n')

		if ans.lower() == 'yes':
			self.residency_req = True
		else:
			ans = input('Have your parents paid California State tax for at least 1 year in their lifetime?\n')
			self.check_parent(ans)
		

	def check_parent(self,ans):
		while ans.lower() not in answers:
			ans = input('Invalid input, please try again\n')

		if ans.lower() == 'yes':
			self.parent_req = True

	def check_work(self,ans):
		while ans.lower() not in answers:
			ans = input('Invalid input, please try again\n')

		if ans.lower() == 'yes':
			self.work_req = True
		else:
			ans = input('Have you volunteered for a cause and are you able to provide valid proof?\n')
			self.check_volunteer(ans)

	def check_volunteer(self,ans):
		while ans.lower() not in answers:
			ans = input('Invalid input, please try again\n')

		if ans.lower() == 'yes':
			self.volunteer_req = True

	def check_household(self,ans):
		while ans.lower() not in answers:
			ans = input('Invalid input, please try again\n')

		if ans.lower() == 'yes':
			self.household_req = True

	def validate_answers(self):
		if age_req and (residency_req or parent_req) and (work_req or volunteer_req):
			return '1'
		elif age_req and (residency_req or parent_req) and household_req:
			return 'Dean for Consideration'
		else:
			return '0'


q = Questionnaire()
q.run()





		