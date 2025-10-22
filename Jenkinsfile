pipeline {
    agent any

    environment {
        // 🐳 Docker Hub account details (⚠️ NEVER use real password in public repo)
        DOCKERHUB_USER = 'niharika345'
        DOCKERHUB_PASS = 'Niharika@03'
        IMAGE = "${DOCKERHUB_USER}/event-management"
        TAG = "${env.BUILD_NUMBER}"

        // 🌐 Path to your Kubernetes config (local system)
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
                    docker.build("${IMAGE}:${TAG}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo "📦 Logging into Docker Hub and pushing image..."
                    bat """
                        echo "${DOCKERHUB_PASS}" | docker login -u "${DOCKERHUB_USER}" --password-stdin
                        docker tag ${IMAGE}:${TAG} ${IMAGE}:1.1
                        docker push ${IMAGE}:${TAG}
                        docker push ${IMAGE}:1.1
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {

    steps {
        script {
            echo '============================'
            echo '⚙️ Deploying to Kubernetes...'
            echo '============================'
            
            bat '''
            kubectl apply -f deployment.yaml
            kubectl apply -f service.yaml
            kubectl set image deployment/event-management-deployment event-management=niharika345/event-management:1.1 || exit 0
            kubectl rollout status deployment/event-management-deployment --timeout=90s || echo Rollout timed out, continuing...
            '''
            steps {
                script {
                    echo "⚙️ Deploying application to Kubernetes..."
                    sh '''
                        kubectl apply -f deployment.yaml
                        kubectl apply -f service.yaml
                        kubectl set image deployment/event-management-deployment event-management=${IMAGE}:${TAG} --record || true
                        kubectl rollout status deployment/event-management-deployment --timeout=180s
                    '''
                }
            }

        }
    }
}

    } 

    post {
        success {
            echo "✅ Pipeline completed successfully! Application deployed on Kubernetes."
        }
        failure {
            echo "❌ Pipeline failed. Check logs for details."
        }
    }
}
