# MLOPS_Class_Task_2_20I-0863
##  Objective
The primary goal was to establish a GitHub repository for the development and testing of a Python class named StudentsInMLOps. This class is designed to manage student enrollments in a hypothetical MLOps course, allowing for student enrollment, deregistration, and querying of total enrollment and class name. Automated testing using pytest was integrated to ensure the reliability of the class methods. The project was further configured to utilize GitHub Actions for continuous integration, automatically running tests upon each push to the repository.
## Tasks Completed
###  1. Repository Creation
A public GitHub repository was initialized with the addition of a README file. This serves as the foundational step, providing a centralized location for source code, documentation, and version control.

### 2. File Structure and Implementation
The following files were created and added to the repository:
**main.py:** Implements the StudentsInMLOps class with methods for enrolling and dropping students, as well as retrieving the total number of students and the class name.
**test.py:** Contains unit tests for the StudentsInMLOps class using pytest to verify the correctness of the class methods.
requirements.txt: Lists pytest as a dependency for running the unit tests.
**Makefile:** Includes commands for installing dependencies (make install) and running tests (make test), facilitating easy project setup and testing.

![NANO ](https://github.com/MaryamKhalid0863/MLOPS_Class_Task_2_20I-0863/assets/159745729/49801c54-962f-42ce-9fa5-421fe8b331af)

### 3. Github Workflows
Github Workflow is created named test.yml and run the jobs.

![SUCCESS](https://github.com/MaryamKhalid0863/MLOPS_Class_Task_2_20I-0863/assets/159745729/7009da49-f1b3-4b5b-bdc1-1a6ae58378d6)

