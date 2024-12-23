pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')  // Poll SCM every minute
    }
    
    stages {
        stage('Cleanup') {
            steps {
                echo 'Cleaning up before cloning code...'
                sh 'rm -rf DevOPS--1114-git'
            }
        }
        stage('Clone Code') {
            steps {
                echo 'Cloning repository...'
                sh '''
                   git clone https://github.com/moshelederman/DevOPS--1114-git.git
                   cd DevOPS--1114-git
                   cd docker-gif-new || exit 1
                   ls -la
                '''
            }
        }
        stage('Build') {
            steps {
                echo 'Building the project...'
                dir('DevOPS--1114-git/docker-gif-new') {
                    withEnv([
                        'MYSQL_ROOT_PASSWORD=example',
                        'MYSQL_DATABASE=testdb',
                        'MYSQL_USER=user',
                        'MYSQL_PASSWORD=example'
                    ]) {
                        sh 'docker-compose up -d'
                    }
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                dir('DevOPS--1114-git/docker-gif-new') {
                    sh '''
                    if [ -f ./test_script.sh ]; then
                        ./test_script.sh
                    else
                        echo "Test script not found, skipping..."
                    fi
                    '''
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                dir('DevOPS--1114-git/docker-gif-new') {
                    sh '''
                    if [ -f ./deploy_script.sh ]; then
                        ./deploy_script.sh
                    else
                        echo "Deploy script not found, skipping..."
                    fi
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
