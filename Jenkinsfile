pipeline {
    
    agent { label 'centos' }
    options { timeout(time: 2, unit: 'MINUTES') }
    
    stages {
        stage('Build') {
            steps {
                echo 'Building....'
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
        
        stage('hello') {
            steps {    
                withAWS(credentials: 'aws-cred', region: 'eu-central-1') {
                sh 'aws ec2 run-instances \
                    --image-id ami-04c21037b3f953d37 \
                    --count 1 \
                    --instance-type t2.micro \
                    --key-name CNDR_key  \
                    --tag-specifications "ResourceType=instance,Tags=[{Key=jenkins,Value=jenkins}]" | grep -i "InstanceId:" | tr -s " " | cut -d " " -f3' 
                }
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
