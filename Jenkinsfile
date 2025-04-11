pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Juan-Silva-Laguna/Docker-Jenkins.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'pip install pytest'
            }
        }

        stage('Ejecutar tests') {
            steps {
                sh 'pytest funcion/test_puntaje.py'
            }
        }
    }

    post {
        success {
            echo '✅ Tests pasaron. Listo para CD.'
        }
        failure {
            echo '❌ Tests fallaron. Revisa el error.'
        }
    }
}
