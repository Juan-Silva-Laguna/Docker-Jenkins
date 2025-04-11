pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Juan-Silva-Laguna/Docker-Jenkins.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'pip3 install --user pytest'
            }
        }

        stage('Ejecutar tests') {
            steps {
                sh '~/.local/bin/pytest funcion/test_puntaje.py'
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
