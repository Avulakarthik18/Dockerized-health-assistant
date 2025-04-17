pipeline {
    agent any

    environment {
        IMAGE_NAME = 'health-assistant'
        CONTAINER_NAME = 'health-assistant'
    }

        stage('📦 Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Avulakarthik18/Dockerized-health-assistant.git'
            }
        }

        stage('🐳 Build Docker Image') {
            steps {
                echo "Building Docker image: ${IMAGE_NAME}"
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('🗑️ Stop & Remove Old Container') {
            steps {
                echo "Stopping and removing old container: ${CONTAINER_NAME}"
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
            }
        }

        stage('🚀 Run New Container') {
            steps {
                echo "Running container: ${CONTAINER_NAME}"
                sh "docker run -d -p 8501:8501 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
            }
        }
    }

    post {
        always {
            echo '✅ Jenkins pipeline execution complete.'
        }
        failure {
            echo '❌ Jenkins pipeline failed! Please check the logs above.'
        }
    }
}
