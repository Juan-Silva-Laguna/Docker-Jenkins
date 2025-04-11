pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Juan-Silva-Laguna/Docker-Jenkins.git'
            }
        }

        stage('Crear entorno virtual') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh './$VENV_DIR/bin/pip install --upgrade pip'
                sh './$VENV_DIR/bin/pip install pytest'
            }
        }

        stage('Ejecutar tests') {
            steps {
                sh './$VENV_DIR/bin/pytest funcion/test_puntaje.py'
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
