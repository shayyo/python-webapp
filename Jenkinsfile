pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                echo "${JENKINS_URL}"
                
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
    }
}
