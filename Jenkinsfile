pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'niharika345'
        DOCKERHUB_PASS = 'Niharika@03'
        IMAGE = "${DOCKERHUB_USER}/event-management"
        TAG = "${env.BUILD_NUMBER}"

        KUBECONFIG = "C:\\Users\\niharika\\.kube\\config"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/V-Niharika/event-management.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "🚀 Building Docker image..."
                    bat "docker build -t ${IMAGE}:${TAG} ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo "📦 Logging into Docker Hub and pushing image..."
                    bat """
                        echo ${DOCKERHUB_PASS} | docker login -u ${DOCKERHUB_USER} --password-stdin
                        docker push ${IMAGE}:${TAG}
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    echo "⚙️ Deploying to Kubernetes with tag ${TAG}..."
                    bat """
                        kubectl apply -f deployment.yaml
                        kubectl apply -f service.yaml
                        kubectl set image deployment/event-management-deployment event-management=${IMAGE}:${TAG} --record
                        kubectl rollout status deployment/event-management-deployment --timeout=180s
                    """
                }
            }
        }

    } 

    post {
        success {
            echo "✅ Pipeline completed successfully! Application deployed on Kubernetes with tag ${TAG}."
        }
        failure {
            echo "❌ Pipeline failed. Check logs for details."
        }
    }
}
