pipeline {
    agent any

    environment {
        DOCKER_USER = "jatinnath2023bcd0014"
        REGISTER = "2023bcd0014"
        ROLL = "2023bcd0014"

        BACKEND_IMAGE = "${DOCKER_USER}/${REGISTER}_${ROLL}_backend"
        FRONTEND_IMAGE = "${DOCKER_USER}/${REGISTER}_${ROLL}_frontend"
    }

    stages {

       

        stage('Build Backend Image') {
            steps {
                sh 'docker build -t $BACKEND_IMAGE ./backend'
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh 'docker build -t $FRONTEND_IMAGE ./frontend'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Push Backend Image') {
            steps {
                sh 'docker push $BACKEND_IMAGE'
            }
        }

        stage('Push Frontend Image') {
            steps {
                sh 'docker push $FRONTEND_IMAGE'
            }
        }
    }
}