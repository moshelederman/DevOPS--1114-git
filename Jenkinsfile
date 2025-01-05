pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')  // Poll SCM every minute
    }



    stage('Build') {
    steps {
        echo 'Building the project...'
        dir('DevOPS--1114-git/docker-gif-new') {
            withCredentials([string(credentialsId: 'MYSQL_ROOT_PASSWORD', variable: 'MYSQL_ROOT_PASSWORD'),
                             string(credentialsId: 'MYSQL_DATABASE', variable: 'MYSQL_DATABASE'),
                             string(credentialsId: 'MYSQL_USER', variable: 'MYSQL_USER'),
                             string(credentialsId: 'MYSQL_PASSWORD', variable: 'MYSQL_PASSWORD')]) {
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

   
        stage('Build') {
    steps {
        echo 'Building the project...'
        dir('DevOPS--1114-git/docker-gif-new') {
            withCredentials([string(credentialsId: 'MYSQL_ROOT_PASSWORD', variable: 'MYSQL_ROOT_PASSWORD'),
                             string(credentialsId: 'MYSQL_DATABASE', variable: 'MYSQL_DATABASE'),
                             string(credentialsId: 'MYSQL_USER', variable: 'MYSQL_USER'),
                             string(credentialsId: 'MYSQL_PASSWORD', variable: 'MYSQL_PASSWORD')]) {
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
        stage('Sleep') {
            steps {
                echo 'Sleeping for 60 seconds...'
                sleep 60
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'curl http://localhost:5000'  
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
