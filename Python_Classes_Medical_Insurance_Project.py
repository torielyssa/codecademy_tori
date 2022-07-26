class Patient:
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker

#first method: estimate insurance cost
    def estimated_insurance_cost(self):
        estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
        print("{}'s estimated insurance costs is {} dollars.".format(self.name, estimated_cost))

    def update_age(self, new_age):
        self.age = new_age
        print("{} is now {} years old.".format(self.name, str(self.age)))
        self.estimated_insurance_cost()

    def update_bmi(self, new_bmi):
        self.bmi = new_bmi
        print("{}'s BMI is now {}.".format(self.name, str(self.bmi)))
        self.estimated_insurance_cost()

    def update_num_children(self, new_num_children):
        self.num_of_children = new_num_children
        if self.num_of_children == 1:
          print("{} has {} child.".format(self.name, str(self.num_of_children)))
        else:
          print("{} has {} children.".format(self.name, str(self.num_of_children)))
        self.estimated_insurance_cost()

    def update_smoking_status(self, new_smoking_status):
      self.smoker = new_smoking_status
      print("{}'s smoking status is now: {}".format(self.name, self.smoker))
      self.estimated_insurance_cost()

    def patient_profile(self):
      patient_information = {}
      patient_information["name"] = self.name
      patient_information["age"] = self.age
      patient_information["sex"] = self.sex
      patient_information["bmi"] = self.bmi
      patient_information["num_of_children"] = self.num_of_children
      patient_information["smoker"] = self.smoker   
      return patient_information   

patient1 = Patient("John Doe", 20, 1, 22.2, 0, 0)
patient1.estimated_insurance_cost()
patient1.update_age(26)
patient1.update_bmi(17.2)
patient1.update_num_children(1)
patient1.update_smoking_status(1)
print(patient1.patient_profile())
