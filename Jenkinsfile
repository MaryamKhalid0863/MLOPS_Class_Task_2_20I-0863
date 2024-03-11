pipeline {
    agent any
    
    stages {
        stage('Clone') {
            steps {
                // Checkout repository
                git 'https://github.com/MaryamKhalid0863/MLOPS_Class_Task_2_20I-0863.git'
            }
        }
        
        stage('Dependencies') {
            steps {
                // Install dependencies
                sh 'pip3 install -r requirements.txt'
            }
        }
        
        stage('Testing') {
            steps {
                // Run tests
                sh 'pytest test.py'
            }
        }
        
        stage('Deployment') {
            steps {
                // Dummy deployment, you can customize this based on your actual deployment process
                script {
                    if (env.BRANCH_NAME == 'main') {
                        // Deploy to production
                        echo 'Deploying to production...'
                    } else {
                        // Deploy to staging or any other environment
                        echo 'Deploying to staging...'
                       
                    }
                }
            }
        }
    }
}
 
