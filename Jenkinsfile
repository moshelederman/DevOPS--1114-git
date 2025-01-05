pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')  // Poll SCM every minute
    }

    stages {
        stage('Cleanup') {
            steps {
                echo 'Cleaning up before cloning code...'
                sh '''
                   if [ -d "DevOPS--1114-git" ]; then
                       rm -rf DevOPS--1114-git
                   fi
                '''
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
                    withCredentials([
                        string(credentialsId: 'MYSQL_ROOT_PASSWORD', variable: 'MYSQL_ROOT_PASSWORD'),
                        string(credentialsId: 'MYSQL_DATABASE', variable: 'MYSQL_DATABASE'),
                        string(credentialsId: 'MYSQL_USER', variable: 'MYSQL_USER'),
                        string(credentialsId: 'MYSQL_PASSWORD', variable: 'MYSQL_PASSWORD')
                    ]) {
                        withEnv([
                            "MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}",
                            "MYSQL_DATABASE=${MYSQL_DATABASE}",
                            "MYSQL_USER=${MYSQL_USER}",
                            "MYSQL_PASSWORD=${MYSQL_PASSWORD}"
                        ]) {
                            sh '''
                                docker-compose down -v
                                docker-compose pull
                                docker-compose up --build -d
                            '''
                        }
                    }
                }
            }
        }
        stage('Sleep') {
            steps {
                echo 'Sleeping for 60 seconds...'
                sleep 60
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                script {
                    def isServiceAvailable = false
                    for (int i = 0; i < 5; i++) {
                        try {
                            sh 'curl -f http://localhost:5000'
                            isServiceAvailable = true
                            break
                        } catch (Exception e) {
                            echo 'Service not available, retrying...'
                            sleep 10
                        }
                    }
                    if (!isServiceAvailable) {
                        error 'Service not available after multiple retries.'
                    }
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
