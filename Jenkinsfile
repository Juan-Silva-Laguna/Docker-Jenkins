pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/Juan-Silva-Laguna/Docker-Jenkins.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'apt-get update && apt-get install -y python3 python3-pip'
                sh 'pip3 install pytest'
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
            echo '❌ Tests fallaron. Revisa errores antes de pasar a producción.'
        }
    }
}
