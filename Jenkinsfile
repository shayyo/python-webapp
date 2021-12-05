pipeline {
    agent any

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
                echo 'BUILD INFORMATION'
                echo "${JENKINS_URL}"
                echo "${BUILD_URL}"
            }
        }
    }
}
