pipeline {
    
    agent { label 'centos' }
    options { timeout(time: 2, unit: 'MINUTES') }
    
    environment {
        AWS_ACCESS_KEY_ID     = credentials('jenkins-aws-secret-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('jenkins-aws-secret-access-key')
    }
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'sudo docker-compose up --no-color --build --exit-code-from pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying.....'
            }
        }
        stage('Build Information....') {
            steps {
                echo 'BUILD INFORMATION:'
                echo "Build results can be found in here ${BUILD_URL}"
            }
        }
    }
}
