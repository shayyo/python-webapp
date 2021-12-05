pipeline {
    agent { label 'centos-slave-nod' }
    options { timeout(time: 2, unit: 'MINUTES') }
    
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
