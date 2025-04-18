pipeline {
    agent any

    environment {
        IMAGE_NAME = 'karthik1803/health-assistant_v1'
        IMAGE_TAG = 'v1'
        CONTAINER_NAME = 'hardcore_gould'
    }

    stages {
        stage('Clone Repo') {
    steps {
        git branch: 'main', url: 'https://github.com/Avulakarthik18/Dockerized-health-assistant.git'
    }
}


        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Push to Docker Hub') {
    steps {
        bat 'docker context use default'
        withDockerRegistry([credentialsId: 'docker_hub_credentials', url: 'https://index.docker.io/v1/']) {
            script {
                docker.image("${IMAGE_NAME}").push("${IMAGE_TAG}")
            }
        }
    }
}


        stage('Cleanup Existing Container') {
            steps {
                bat """
                    docker ps -a -q --filter "name=${CONTAINER_NAME}" > container_id.txt
                    for /f %%i in (container_id.txt) do (
                        docker stop %%i
                        docker rm %%i
                    )
                    del container_id.txt
                """
            }
        }

        stage('Run New Container') {
            steps {
                bat "docker run -d -p 8501:8501 --name ${CONTAINER_NAME} ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }
    }
}

