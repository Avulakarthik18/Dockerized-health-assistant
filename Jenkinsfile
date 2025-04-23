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
                echo "Building Docker image..."
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
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

