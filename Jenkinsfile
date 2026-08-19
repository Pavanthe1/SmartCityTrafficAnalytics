pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Run Python Program') {
            steps {
                echo 'Running Python program...'
                sh 'python3 main.py'
            }
        }
    }
}
