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

![SUCCESS](https://github.com/MaryamKhalid0863/MLOPS_Class_Task_2_20I-0863/assets/159745729/739b8202-7df4-4aea-bf91-b78d13c73269)

# StudentsInMLOps Project

This project is designed to demonstrate a simple Python class implementation for managing student enrollments in an MLOps course. It includes a `StudentsInMLOps` class with methods to enroll and drop students, get total class strength, and retrieve the class name. Automated tests using pytest verify the functionality of these methods.

## Features

- **Enroll Students:** Add students to the class total.
- **Drop Students:** Remove students from the class total.
- **Get Total Strength:** Return the current number of students.
- **Get Class Name:** Return the name of the class.

Additionally, this project is configured with GitHub Actions to automate testing on every push, ensuring code integrity through continuous integration.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Git

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/MaryamKhalid0863/MLOPS_Class_Task_2_20I-0863

## Usage
To use the StudentsInMLOps class in your Python code, simply import the class from the main.py file.
from main import StudentsInMLOps

### Create an instance of the class
classroom = StudentsInMLOps()

### Enroll students
classroom.enrollStudents(5)

### Drop students
classroom.dropStudents(2)

### Get total strength
print(classroom.getTotalStrength())

### Get class name
print(classroom.getClassName())

## Running Tests
This project uses pytest for testing. To run the tests, use the following command:
pytest test.py

Alternatively, you can use the Makefile:
make test

## Continuous Integration
This project is configured with GitHub Actions for continuous integration. On every push to the repository, GitHub Actions will automatically set up a Python environment, install dependencies, and run the test suite.

## License
This project is open-sourced under the MIT License. See the LICENSE file for more details.




