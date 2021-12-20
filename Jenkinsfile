pipeline {
    
    agent { label 'centos' }
    options { timeout(time: 2, unit: 'MINUTES') }
    
    stages {
        stage('Build') {
            steps {
                echo "Building.....echo"
                sh 'echo "Building......sh"'
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
        /*
        stage('Create AWS EC2 VM') {
            steps {
                withAWS(credentials: 'aws-cred', region: 'eu-central-1') {
                sh 'aws ec2 run-instances \
                    --image-id ami-04c21037b3f953d37 \
                    --count 1 \
                    --instance-type t2.micro \
                    --key-name CNDR_key  \
                    --tag-specifications "ResourceType=instance,Tags=[{Key=jenkins,Value=jenkins}]" > aws_instance_details.txt'
                
                script {
                    instance_id = sh (
                    script: 'cat aws_instance_details.txt | grep InstanceId | tr -s " " | cut -d " " -f 3',
                    returnStdout: true
                    )
                    echo "AWS EC2 instance ID: ${instance_id}"
                    }
                }
            }
        }
        */
        
        stage('Build Information.....') {
            steps {
                echo 'BUILD INFORMATION:'
                echo "Build results can be found in here ${BUILD_URL}"
            }
        }
    }
}
