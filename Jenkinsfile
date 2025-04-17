pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Avulakarthik18/Dockerized-health-assistant.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t health-assistant .'
            }
        }

        stage('Stop & Remove Old Container') {
            steps {
                sh 'docker stop health-assistant || true'
                sh 'docker rm health-assistant || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 8501:8501 --name health-assistant health-assistant'
            }
        }
    }

    post {
        always {
            echo '✅ Pipeline finished'
        }
    }
}
