pipeline {
    agent any

    environment {
        IMAGE_NAME = 'karthik1803/health-assistant_v1'
        IMAGE_TAG = 'v1'
        CONTAINER_NAME = 'health-assistant'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Avulakarthik18/Dockerized-health-assistant.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image using cache..."
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker_hub_credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    bat '''
                        echo Logging in to Docker Hub...
                        echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin
                        docker push %IMAGE_NAME%:%IMAGE_TAG%
                    '''
                }
            }
        }
        stage('Cleanup Existing Container') {
            steps {
                bat """
                for /f %%i in ('docker ps -a -q --filter "name=%CONTAINER_NAME%"') do (
                    docker stop %%i
                    docker rm %%i
                )
                """
            }
        }

        stage('Run New Container') {
            steps {
                bat "docker run -d -p 8501:8501 --name %CONTAINER_NAME% %IMAGE_NAME%:%IMAGE_TAG%"
            }
        }
    }
}
