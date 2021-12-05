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
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying.....'
            }
        }
    }
}
